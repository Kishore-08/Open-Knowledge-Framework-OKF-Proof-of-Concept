from llama_index.core import Document

from app.indexing.vector_state import (
    VectorIndexState,
    content_hash_for_document,
    filter_documents_for_indexing,
    mark_documents_indexed,
)


def _doc(source_file: str, text: str = "body", doc_id: str = "id-1") -> Document:
    return Document(
        text=text,
        metadata={"id": doc_id, "source_file": source_file},
    )


def test_filter_documents_skips_unchanged_when_qdrant_has_them(monkeypatch, tmp_path):
    cache_dir = str(tmp_path / "cache")
    docs = [_doc("architecture/a.md"), _doc("tutorial/b.md", text="other", doc_id="id-2")]

    monkeypatch.setattr(
        "app.retrieval.hybrid_search.get_indexed_source_files",
        lambda collection_name=None: {"architecture/a.md", "tutorial/b.md"},
    )

    state = VectorIndexState()
    for doc in docs:
        state.mark_indexed(doc.metadata["source_file"], content_hash_for_document(doc))
    state.save(cache_dir)

    need, skipped = filter_documents_for_indexing(docs, cache_dir=cache_dir)
    assert need == []
    assert skipped == 2


def test_filter_documents_reindexes_missing_from_qdrant(monkeypatch, tmp_path):
    cache_dir = str(tmp_path / "cache")
    docs = [_doc("architecture/a.md"), _doc("tutorial/b.md", text="other", doc_id="id-2")]

    monkeypatch.setattr(
        "app.retrieval.hybrid_search.get_indexed_source_files",
        lambda collection_name=None: {"architecture/a.md"},
    )

    state = VectorIndexState()
    for doc in docs:
        state.mark_indexed(doc.metadata["source_file"], content_hash_for_document(doc))
    state.save(cache_dir)

    need, skipped = filter_documents_for_indexing(docs, cache_dir=cache_dir)
    assert len(need) == 1
    assert need[0].metadata["source_file"] == "tutorial/b.md"
    assert skipped == 1


def test_filter_documents_reindexes_updated_paths(monkeypatch, tmp_path):
    cache_dir = str(tmp_path / "cache")
    docs = [_doc("architecture/a.md")]

    monkeypatch.setattr(
        "app.retrieval.hybrid_search.get_indexed_source_files",
        lambda collection_name=None: {"architecture/a.md"},
    )

    state = VectorIndexState()
    state.mark_indexed("architecture/a.md", content_hash_for_document(docs[0]))
    state.save(cache_dir)

    need, skipped = filter_documents_for_indexing(
        docs,
        updated_paths={"architecture/a.md"},
        cache_dir=cache_dir,
    )
    assert len(need) == 1
    assert skipped == 0


def test_filter_documents_clears_state_when_qdrant_empty(monkeypatch, tmp_path):
    cache_dir = str(tmp_path / "cache")
    docs = [_doc("architecture/a.md")]

    monkeypatch.setattr(
        "app.retrieval.hybrid_search.get_indexed_source_files",
        lambda collection_name=None: set(),
    )

    state = VectorIndexState()
    state.mark_indexed("architecture/a.md", content_hash_for_document(docs[0]))
    state.save(cache_dir)

    need, skipped = filter_documents_for_indexing(docs, cache_dir=cache_dir)
    assert len(need) == 1
    assert skipped == 0

    reloaded = VectorIndexState.load(cache_dir)
    assert reloaded.entries == {}


def test_mark_documents_indexed_persists_hashes(tmp_path):
    cache_dir = str(tmp_path / "cache")
    docs = [_doc("architecture/a.md")]

    mark_documents_indexed(docs, cache_dir=cache_dir)

    state = VectorIndexState.load(cache_dir)
    assert state.is_current("architecture/a.md", content_hash_for_document(docs[0]))
