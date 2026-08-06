"""
Concept indexer (Phase 9 - indexing).

Reads the OKF knowledge repository, converts each concept into a LlamaIndex
Document (with its frontmatter as node metadata), embeds it, and upserts it into
the Qdrant `okf_concepts` collection with hybrid (dense + sparse) support.

The knowledge repository remains the source of truth; this index is an
acceleration layer only.
"""

from typing import List, Optional

from llama_index.core import Document, StorageContext, VectorStoreIndex
from llama_index.core.node_parser import SentenceSplitter

from app.core.config import settings
from app.okf.repository import load_all_concepts
from app.retrieval.hybrid_search import get_qdrant_vector_store


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


def _to_documents() -> List[Document]:
    docs = []
    for concept in load_all_concepts():
        meta = concept.metadata
        docs.append(
            Document(
                text=concept.full_text,
                metadata=meta.metadata_payload(),
                excluded_llm_metadata_keys=["content", "filepath"],
                excluded_embed_metadata_keys=["filepath"],
            )
        )
    return docs


def build_concepts_index(*, collection_name: Optional[str] = None, with_embeddings: bool = True):
    """
    Index every concept in the knowledge repository into Qdrant.

    - `with_embeddings=True` requires a configured Gemini API key (dense vectors).
    - `with_embeddings=False` performs a "dry-run" that still validates documents
      and (if Qdrant is reachable) creates the collection and stores metadata-only
      points, useful for CI / offline checks.
    """
    docs = _to_documents()
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

    vector_store = get_qdrant_vector_store(collection_name)
    storage_context = StorageContext.from_defaults(vector_store=vector_store)
    splitter = SentenceSplitter(chunk_size=settings.CHUNK_SIZE, chunk_overlap=settings.CHUNK_OVERLAP)
    index = VectorStoreIndex.from_documents(
        docs,
        storage_context=storage_context,
        transformations=[splitter],
        show_progress=True,
    )
    return {"indexed": len(docs), "collection": collection_name}


if __name__ == "__main__":
    result = build_concepts_index()
    print(result)
