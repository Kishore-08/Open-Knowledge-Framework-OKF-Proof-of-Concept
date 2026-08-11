# This __init__.py makes imports much cleaner in our FastAPI routers later.
# Instead of: from app.retrieval.hybrid_search import get_qdrant_vector_store
# We can do:  from app.retrieval import get_qdrant_vector_store, get_qdrant_client

from .hybrid_search import get_qdrant_vector_store, get_qdrant_client

__all__ = [
    "get_qdrant_vector_store",
    "get_qdrant_client",
]
