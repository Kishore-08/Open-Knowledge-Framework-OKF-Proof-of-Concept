"""
Regression test for a bug hit in production after the initial retry-with-
backoff fix to app.retrieval.hybrid_search.index_documents:

    api-1 | Failed to index 'kubernetes-what-s-next-5445bee6' after retries,
    skipping: run_transformations() got multiple values for argument
    'transformations'

Root cause: `index_documents` constructs `VectorStoreIndex(..., transformations=
[splitter])`, which stores `splitter` as `self._transformations` on the index.
`index.insert(doc, transformations=[splitter])` then passed `transformations`
a *second* time - `BaseIndex.insert()` already forwards `self._transformations`
positionally into `run_transformations(...)`, so the extra keyword collided.
Every single document failed to index as a result (600/649 failed in the
observed run), which is worse than the original "no retry at all" bug this
was meant to fix, and failed silently past `except Exception` per-document
handling with no test catching it.

This test drives the real `index_documents()` function (not a reimplementation
of it) with the real llama-index `VectorStoreIndex`/`SentenceSplitter`, but
swaps out the Qdrant-backed vector store for an in-memory one and the Gemini
embedding model for a deterministic mock, so it runs fully offline.
"""

from llama_index.core import Document, Settings
from llama_index.core.embeddings import MockEmbedding
from llama_index.core.vector_stores.simple import SimpleVectorStore

from app.retrieval import hybrid_search


def test_index_documents_inserts_without_transformations_collision(monkeypatch):
    Settings.embed_model = MockEmbedding(embed_dim=8)

    in_memory_store = SimpleVectorStore()
    monkeypatch.setattr(hybrid_search, "get_qdrant_vector_store", lambda name=None: in_memory_store)
    monkeypatch.setattr(hybrid_search, "reset_hybrid_collection", lambda name=None: None)
    monkeypatch.setattr(hybrid_search, "delete_points_by_field", lambda *a, **k: None)

    docs = [
        Document(
            text="Kubernetes is a container orchestration platform. " * 10,
            metadata={"id": f"kubernetes-what-s-next-{i}", "source_file": f"k8s-{i}.md"},
        )
        for i in range(3)
    ]

    index, failed_ids = hybrid_search.index_documents(docs, collection_name="test_collection")

    # Before the fix, every insert() call raised the transformations TypeError
    # and every document ended up in failed_ids.
    assert failed_ids == []
    assert len(index.docstore.docs) > 0


def _fake_vector_store(monkeypatch):
    Settings.embed_model = MockEmbedding(embed_dim=8)
    in_memory_store = SimpleVectorStore()
    monkeypatch.setattr(hybrid_search, "get_qdrant_vector_store", lambda name=None: in_memory_store)
    monkeypatch.setattr(hybrid_search, "reset_hybrid_collection", lambda name=None: None)
    monkeypatch.setattr(hybrid_search, "delete_points_by_field", lambda *a, **k: None)


def test_index_documents_reports_live_progress_per_document(monkeypatch):
    """
    Regression test for the bug reported after deploying the retry-with-
    backoff fix: `index_documents` ran its entire embedding loop without ever
    calling `update_status()` again until the very end, so every UI counter
    (Discovered/Fetched/Processed/Indexed/Failed) and the progress bar froze
    for the whole indexing phase - which can take many minutes when Gemini's
    free-tier rate limit kicks in. This asserts `update_status` is actually
    called once per document with the running indexed count, not just once
    at the very end.
    """
    _fake_vector_store(monkeypatch)

    calls = []
    monkeypatch.setattr("app.ingestion.status.update_status", lambda **kw: calls.append(kw))

    docs = [
        Document(text="kubernetes pod " * 10, metadata={"id": f"doc-{i}", "title": f"Doc {i}"})
        for i in range(4)
    ]

    index, failed_ids = hybrid_search.index_documents(docs, collection_name="test_collection")

    assert failed_ids == []
    # One call up front to report the total, plus one per document.
    indexed_progress_calls = [c for c in calls if c.get("stage") == "indexing" and "indexed" in c]
    assert len(indexed_progress_calls) == len(docs)
    assert [c["indexed"] for c in indexed_progress_calls] == [1, 2, 3, 4]
    assert all(c.get("total_documents") == len(docs) for c in indexed_progress_calls)


def test_index_documents_surfaces_rate_limit_hits_to_status(monkeypatch):
    """
    Regression test: 429 retry warnings previously only ever reached
    `print()`/container logs, never `update_status()`, so a rate-limited run
    was indistinguishable from a stuck one in the UI. This asserts a retry
    increments `rate_limit_hits` and is reported via `update_status`.
    """
    _fake_vector_store(monkeypatch)

    calls = []
    monkeypatch.setattr("app.ingestion.status.update_status", lambda **kw: calls.append(kw))
    monkeypatch.setattr(hybrid_search.time, "sleep", lambda s: None)  # don't actually wait out the backoff

    doc = Document(text="kubernetes pod " * 10, metadata={"id": "flaky-doc", "title": "Flaky Doc"})

    call_count = {"n": 0}
    orig_insert = hybrid_search.VectorStoreIndex.insert

    def flaky_insert(self, d, **kw):
        if d.metadata.get("id") == "flaky-doc" and call_count["n"] == 0:
            call_count["n"] += 1
            raise Exception("429 Too Many Requests")
        return orig_insert(self, d, **kw)

    monkeypatch.setattr(hybrid_search.VectorStoreIndex, "insert", flaky_insert)

    index, failed_ids = hybrid_search.index_documents([doc], collection_name="test_collection")

    assert failed_ids == []
    rate_limit_calls = [c for c in calls if c.get("rate_limit_hits")]
    assert len(rate_limit_calls) == 1
    assert rate_limit_calls[0]["rate_limit_hits"] == 1
    assert "flaky-doc" in rate_limit_calls[0]["message"]


def test_index_documents_stops_promptly_on_cancel(monkeypatch):
    """
    Regression test: cancellation was only checked once *before*
    `index_documents` was called, never between documents, so the Stop
    button had no effect during a long (rate-limit-heavy) indexing run until
    the entire batch finished on its own. This asserts cancellation is
    honored mid-batch.
    """
    import threading
    from app.jobs.manager import JobCancelledError

    _fake_vector_store(monkeypatch)
    monkeypatch.setattr("app.ingestion.status.update_status", lambda **kw: None)

    docs = [Document(text="x", metadata={"id": f"doc-{i}"}) for i in range(5)]
    cancel_event = threading.Event()

    inserted = {"n": 0}
    orig_insert = hybrid_search.VectorStoreIndex.insert

    def counting_insert(self, d, **kw):
        inserted["n"] += 1
        if inserted["n"] == 2:
            cancel_event.set()  # cancel partway through the batch
        return orig_insert(self, d, **kw)

    monkeypatch.setattr(hybrid_search.VectorStoreIndex, "insert", counting_insert)

    try:
        hybrid_search.index_documents(docs, collection_name="test_collection", cancel_event=cancel_event)
        assert False, "expected JobCancelledError"
    except JobCancelledError:
        pass

    assert inserted["n"] < len(docs)  # stopped before processing every document
