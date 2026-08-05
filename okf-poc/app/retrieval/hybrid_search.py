import os
import qdrant_client
from llama_index.vector_stores.qdrant import QdrantVectorStore

from app.core.config import settings
 
def get_qdrant_vector_store(collection_name: str = None) -> QdrantVectorStore:
    """
    Initializes a connection to the Qdrant Vector Database running in Docker.
    Configures the collection to support Hybrid Search (Dense + Sparse vectors).
    """
    
    if collection_name is None:
        collection_name = settings.QDRANT_COLLECTION
 
    # 1. Fetch the Qdrant URL from the environment variables (defaults to localhost for dev)
    # In docker-compose, this will be http://qdrant:6333. Locally it's http://localhost:6333
    qdrant_url = os.getenv("QDRANT_URL", settings.QDRANT_URL)
    
    print(f"🔌 Connecting to Qdrant at {qdrant_url}...")
    
    # 2. Create the Qdrant Client
    client = qdrant_client.QdrantClient(
        url=qdrant_url,
        # We don't need an API key for local docker deployment
    )
    
    # 3. Wrap it in LlamaIndex's QdrantVectorStore
    # enable_hybrid=True tells Qdrant to generate Sparse Vectors (keywords) alongside Dense Vectors (semantics)
    vector_store = QdrantVectorStore(
        client=client,
        collection_name=collection_name,
        enable_hybrid=True,
        # fastembed handles sparse vector generation locally without needing an extra API call
        batch_size=20 
    )
    
    return vector_store

def get_qdrant_client() -> qdrant_client.QdrantClient:
    """Utility function to get the raw client for checking collection stats."""
    qdrant_url = os.getenv("QDRANT_URL", "http://localhost:6333")
    return qdrant_client.QdrantClient(url=qdrant_url)