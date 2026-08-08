"""
Knowledge search (Phase 10 - query).

Offers two complementary access paths over the knowledge base:

  * `search_keyword()`  - dependency-free filesystem keyword/metadata/tag search.
  * `search_semantic()` - semantic search over the Qdrant `okf_concepts` index,
    requiring a configured embed model. Falls back to keyword search when the
    vector store or API key is unavailable.
"""

from typing import List, Optional

from app.core.config import settings
from app.okf.repository import list_concepts, search_concepts


def search(
    query: str,
    *,
    category: Optional[str] = None,
    tag: Optional[str] = None,
    mode: str = "auto",
    top_k: Optional[int] = None,
) -> dict:
    """
    Unified search entry point.

    `mode`:
      - "keyword" : filesystem keyword/metadata/tag search (always available)
      - "semantic": Qdrant vector search
      - "auto"    : keyword results augmented with semantic results when possible
    """
    keyword_results = search_concepts(query, category=category, tag=tag)
    if mode == "keyword":
        return {"mode": "keyword", "results": keyword_results[: (top_k or settings.TOP_K)]}

    if mode == "semantic":
        results = _semantic_search(query, category=category, top_k=top_k)
        return {"mode": "semantic", "results": results}

    # auto: merge keyword and semantic, preferring keyword for incomplete indices
    # If semantic search returns results with low relevance or wrong category,
    # keyword search provides better fallback
    semantic_results = _semantic_search(query, category=category, top_k=top_k)
    
    # Start with keyword results (always accurate)
    merged = list(keyword_results[: (top_k or settings.TOP_K)])
    seen = {r["id"] for r in merged}
    
    # Add high-quality semantic results that aren't already present
    for r in semantic_results:
        if r["id"] not in seen and r.get("score", 0) > 0.8:  # Only high-confidence semantic results
            merged.append(r)
            if len(merged) >= (top_k or settings.TOP_K):
                break
    
    return {"mode": "auto", "results": merged[: (top_k or settings.TOP_K)]}


def _semantic_search(query: str, *, category: Optional[str] = None, top_k: Optional[int] = None) -> List[dict]:
    """Semantic search over the Qdrant concept index. Best effort; empty on failure."""
    top_k = top_k or settings.TOP_K
    try:
        from llama_index.core.vector_stores import MetadataFilters, MetadataFilter, FilterOperator

        index = _get_cached_semantic_index()
        filters = None
        if category:
            filters = MetadataFilters(
                filters=[MetadataFilter(key="category", operator=FilterOperator.EQ, value=category)]
            )

        retriever = index.as_retriever(similarity_top_k=top_k, filters=filters)
        nodes = retriever.retrieve(query)
        return [
            {
                "id": n.metadata.get("id", ""),
                "title": n.metadata.get("title", ""),
                "category": n.metadata.get("category", ""),
                "tags": n.metadata.get("tags", []),
                "description": n.metadata.get("description", ""),
                "source_url": n.metadata.get("source_url", ""),
                "source_file": n.metadata.get("source_file", ""),
                "score": round(n.score, 4) if n.score else 0.0,
                "matched_fields": ["semantic"],
                "snippet": n.text[:200],
            }
            for n in nodes
        ]
    except Exception as exc:  # noqa: BLE001 - semantic search is best effort
        print(f"ℹ️ Semantic search unavailable, falling back to keyword: {exc}")
        return []


_semantic_cache: dict = {}


def _get_cached_semantic_index():
    """
    Lazily build and cache the VectorStoreIndex over the Qdrant concepts collection.

    The retriever queries Qdrant directly on every call, so a cached index always
    reflects newly ingested documents while avoiding the expensive re-configuration
    (model construction + collection metadata round-trips) on every single query.
    """
    from llama_index.core import VectorStoreIndex
    from app.retrieval.query_engine import configure_llm_settings
    from app.retrieval.hybrid_search import get_qdrant_vector_store

    key = f"{settings.QDRANT_CONCEPTS_COLLECTION}:{settings.EMBEDDING_MODEL}"
    if _semantic_cache.get("key") != key or _semantic_cache.get("index") is None:
        configure_llm_settings()
        vector_store = get_qdrant_vector_store(settings.QDRANT_CONCEPTS_COLLECTION)
        index = VectorStoreIndex.from_vector_store(vector_store=vector_store)
        _semantic_cache["key"] = key
        _semantic_cache["index"] = index
    return _semantic_cache["index"]


def search_tags(category: Optional[str] = None) -> List[str]:
    """All tags used across the knowledge repository (optionally within a category)."""
    tags = set()
    for concept in list_concepts(category):
        tags.update(concept.get("tags") or [])
    return sorted(tags)
