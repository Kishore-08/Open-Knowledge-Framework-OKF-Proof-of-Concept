import os
from typing import List, Optional

import qdrant_client
from qdrant_client.http import models as qdrant_models
from llama_index.vector_stores.qdrant import QdrantVectorStore

from app.core.config import settings


def get_qdrant_vector_store(collection_name: str = None) -> QdrantVectorStore:
    """
    Initializes a connection to the Qdrant Vector Database.

    NOTE: enable_hybrid is intentionally set to False.
    fastembed 0.8.x + qdrant-client 1.18.x + llama-index-vector-stores-qdrant 0.10.x
    have a payload API mismatch that causes Qdrant to return '503 Illegal metadata'
    whenever fastembed tries to configure sparse-vector metadata on a collection.
    Dense semantic search via Gemini embeddings is used instead - it provides
    equally strong retrieval quality without the version-compatibility issue.
    """
    if collection_name is None:
        collection_name = settings.QDRANT_CONCEPTS_COLLECTION

    qdrant_url = os.getenv("QDRANT_URL", settings.QDRANT_URL)

    print(f"🔌 Connecting to Qdrant at {qdrant_url}...")

    # Use a generous timeout (300 s) so large ingestion batches don't trigger
    # "Timeout of 60.0s exceeded" errors during embedding + upsert.
    client = qdrant_client.QdrantClient(
        url=qdrant_url,
        timeout=300,
    )

    # enable_hybrid=False — avoids fastembed / Qdrant-payload 503 errors.
    # batch_size=10 keeps per-request payloads small to reduce transient failures.
    vector_store = QdrantVectorStore(
        client=client,
        collection_name=collection_name,
        enable_hybrid=False,
        batch_size=10,
    )

    return vector_store


def get_qdrant_client() -> qdrant_client.QdrantClient:
    """Utility function to get the raw client for checking collection stats."""
    qdrant_url = os.getenv("QDRANT_URL", "http://localhost:6333")
    return qdrant_client.QdrantClient(url=qdrant_url, timeout=300)


def reset_hybrid_collection(collection_name: str = None) -> None:
    """
    Delete a Qdrant collection that was created with hybrid (sparse) vectors.

    A collection created by an earlier `enable_hybrid=True` run (or by a different
    library version) keeps sparse-vector configuration that conflicts with the
    dense-only points this codebase upserts, producing Qdrant's '503 Illegal
    metadata' error. Because the filesystem knowledge repository is the source of
    truth, it is safe to drop and rebuild such a collection.
    """
    if collection_name is None:
        collection_name = settings.QDRANT_CONCEPTS_COLLECTION
    try:
        client = get_qdrant_client()
        if not client.collection_exists(collection_name):
            print(f"ℹ️ Collection '{collection_name}' does not exist; nothing to reset.")
            return

        info = client.get_collection(collection_name)
        params = info.config.params if info.config else None
        sparse_vectors = getattr(params, "sparse_vectors", None) if params else None

        if sparse_vectors:
            print(
                f"⚠️ Collection '{collection_name}' has hybrid sparse-vector config "
                "(known cause of '503 Illegal metadata'); deleting so it is rebuilt dense-only."
            )
            client.delete_collection(collection_name)
        else:
            print(f"ℹ️ Collection '{collection_name}' is dense-only; keeping it.")
    except Exception as exc:  # noqa: BLE001 - best-effort cleanup
        print(f"ℹ️ Could not inspect/reset collection '{collection_name}': {exc}")


def delete_points_by_field(
    collection_name: str,
    field: str,
    values: List[str],
) -> None:
    """
    Delete every Qdrant point whose payload `field` matches one of `values`.

    Used to make ingestion idempotent: re-ingesting the same source file removes
    the previously stored chunks (whose node ids are random UUIDs) before the new
    chunks are upserted, preventing duplicate documents in the vector store.
    """
    values = [v for v in values if v]
    if not values:
        return
    client = get_qdrant_client()
    if not client.collection_exists(collection_name):
        return
    client.delete(
        collection_name=collection_name,
        points_selector=qdrant_models.FilterSelector(
            filter=qdrant_models.Filter(
                must=[
                    qdrant_models.FieldCondition(
                        key=field,
                        match=qdrant_models.MatchAny(any=values),
                    )
                ]
            )
        ),
    )
    print(f"🗑️ Removed previous points for {len(values)} source file(s) from '{collection_name}'.")