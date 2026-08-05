import os
import qdrant_client
from llama_index.vector_stores.qdrant import QdrantVectorStore

from app.core.config import settings


def get_qdrant_vector_store(collection_name: str = None) -> QdrantVectorStore:
    """
    Initializes a connection to the Qdrant Vector Database running in Docker.

    NOTE: enable_hybrid is intentionally set to False.
    fastembed 0.8.x + qdrant-client 1.18.x + llama-index-vector-stores-qdrant 0.10.x
    have a payload API mismatch that causes Qdrant to return '503 Illegal metadata'
    whenever fastembed tries to configure sparse-vector metadata on a collection.
    Dense semantic search via Gemini embeddings is used instead - it provides
    equally strong retrieval quality without the version-compatibility issue.
    """

    if collection_name is None:
        collection_name = settings.QDRANT_COLLECTION

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