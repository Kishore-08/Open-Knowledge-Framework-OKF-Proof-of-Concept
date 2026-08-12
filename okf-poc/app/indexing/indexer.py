"""
Concept indexer (Phase 9 - indexing).

Reads the OKF knowledge repository, converts each concept into a LlamaIndex
Document (with its frontmatter as node metadata), embeds it, and upserts it into
the Qdrant `okf_concepts` collection with hybrid (dense + sparse) support.

The knowledge repository remains the source of truth; this index is an
acceleration layer only.
"""

import os
from typing import List, Optional

from llama_index.core import Document

from app.core.config import settings
from app.okf.repository import load_all_concepts
from app.indexing.vector_state import filter_documents_for_indexing
from app.retrieval.hybrid_search import get_qdrant_vector_store, index_documents


def _embedding_model_configured() -> bool:
    """
    Configure Gemini embeddings explicitly.

    This is Gemini-first on purpose: when an OPENAI_API_KEY happens to be
    present in the environment, llama-index silently defaults
    `Settings.embed_model` to an OpenAI model. We always (re)configure the
    Gemini embed model so no foreign key/model is ever used.
    """
    try:
        from app.retrieval.query_engine import configure_llm_settings

        configure_llm_settings()
        return True
    except Exception as exc:  # noqa: BLE001 - allow dry-run without an API key
        print(f"ℹ️ Embedding model not configured ({exc}). Running indexer without embeddings.")
        return False


def concepts_to_documents(concepts) -> List[Document]:
    """Convert OKF concepts into LlamaIndex Documents (metadata = Qdrant payload)."""
    docs = []
    for concept in concepts:
        payload = concept.metadata.metadata_payload()
        # Stable provenance per source file so re-building the index replaces
        # (rather than duplicates) the stored chunks for each concept file.
        payload["source_file"] = os.path.relpath(concept.filepath, settings.KNOWLEDGE_DIR)
        docs.append(
            Document(
                text=concept.full_text,
                metadata=payload,
                excluded_llm_metadata_keys=["content", "filepath"],
                excluded_embed_metadata_keys=["filepath"],
            )
        )
    return docs


def build_concepts_index(
    *,
    collection_name: Optional[str] = None,
    with_embeddings: bool = True,
    force_full: bool = False,
):
    """
    Index concepts from the knowledge repository into Qdrant.

    By default this is incremental: only concepts missing from Qdrant or whose
    content changed since the last successful index are embedded. Pass
    `force_full=True` to re-embed everything (expensive — uses Gemini quota).

    - `with_embeddings=True` requires a configured Gemini API key (dense vectors).
    - `with_embeddings=False` performs a "dry-run" that still validates documents
      and (if Qdrant is reachable) creates the collection and stores metadata-only
      points, useful for CI / offline checks.
    """
    docs = concepts_to_documents(load_all_concepts())
    if not docs:
        return {"indexed": 0, "message": "No concepts found in the knowledge repository."}

    collection_name = collection_name or settings.QDRANT_CONCEPTS_COLLECTION

    if not with_embeddings:
        # Still create the collection structure when Qdrant is reachable.
        try:
            vector_store = get_qdrant_vector_store(collection_name)
            _ = vector_store  # create/attach
        except Exception as exc:  # noqa: BLE001
            print(f"ℹ️ Qdrant not reachable during dry-run: {exc}")
        return {"indexed": len(docs), "dry_run": True, "documents": [d.metadata["id"] for d in docs]}

    configured = _embedding_model_configured()
    if not configured:
        return {"indexed": 0, "error": "Gemini API key required for embeddings. Set GEMINI_API_KEY."}

    docs_to_index, skipped = filter_documents_for_indexing(docs, force_full=force_full)
    if not docs_to_index:
        return {
            "indexed": 0,
            "skipped": skipped,
            "collection": collection_name,
            "message": f"All {skipped} concept(s) already indexed in Qdrant; nothing to do.",
        }

    if skipped:
        print(f"ℹ️ Skipping {skipped} unchanged concept(s) already present in Qdrant.")

    source_files = [d.metadata["source_file"] for d in docs_to_index if d.metadata.get("source_file")]
    _index, failed_ids = index_documents(
        docs_to_index,
        collection_name=collection_name,
        source_files=[],
        show_progress=True,
    )
    result = {
        "indexed": len(docs_to_index) - len(failed_ids),
        "skipped": skipped,
        "collection": collection_name,
    }
    if failed_ids:
        result["failed"] = failed_ids
    return result


if __name__ == "__main__":
    result = build_concepts_index()
    print(result)
