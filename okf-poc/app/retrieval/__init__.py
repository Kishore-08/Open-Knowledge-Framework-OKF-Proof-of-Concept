# This __init__.py makes imports much cleaner in our FastAPI routers later.
# Instead of: from app.retrieval.query_engine import get_query_engine
# We can do:  from app.retrieval import get_query_engine, get_qdrant_vector_store

from .hybrid_search import get_qdrant_vector_store, get_qdrant_client
from .query_engine import get_query_engine, get_retriever

__all__ = [
    "get_qdrant_vector_store",
    "get_qdrant_client",
    "get_query_engine",
    "get_retriever"
]