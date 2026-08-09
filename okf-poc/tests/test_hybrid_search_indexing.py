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
