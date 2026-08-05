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
from app.okf.repository import list_categories, list_concepts, search_concepts


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

    # auto: merge, prefer semantic hits but keep keyword hits for coverage
    semantic_results = _semantic_search(query, category=category, top_k=top_k)
    merged = list(semantic_results)
    seen = {r["id"] for r in merged}
    for r in keyword_results:
        if r["id"] not in seen:
            merged.append(r)
    return {"mode": "auto", "results": merged[: (top_k or settings.TOP_K)]}


def _semantic_search(query: str, *, category: Optional[str] = None, top_k: Optional[int] = None) -> List[dict]:
    """Semantic search over the Qdrant concept index. Best effort; empty on failure."""
    top_k = top_k or settings.TOP_K
    try:
        from app.retrieval.query_engine import configure_llm_settings
        from llama_index.core import VectorStoreIndex
        from llama_index.core.vector_stores import MetadataFilters, MetadataFilter, FilterOperator
        from app.retrieval.hybrid_search import get_qdrant_vector_store

        configure_llm_settings()
        vector_store = get_qdrant_vector_store(settings.QDRANT_CONCEPTS_COLLECTION)
        index = VectorStoreIndex.from_vector_store(vector_store=vector_store)

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
                "score": round(n.score, 4) if n.score else 0.0,
                "matched_fields": ["semantic"],
                "snippet": n.text[:200],
            }
            for n in nodes
        ]
    except Exception as exc:  # noqa: BLE001 - semantic search is best effort
        print(f"ℹ️ Semantic search unavailable, falling back to keyword: {exc}")
        return []


def search_categories() -> List[str]:
    """All categories present in the knowledge repository."""
    return list_categories()


def search_tags(category: Optional[str] = None) -> List[str]:
    """All tags used across the knowledge repository (optionally within a category)."""
    tags = set()
    for concept in list_concepts(category):
        tags.update(concept.get("tags") or [])
    return sorted(tags)
