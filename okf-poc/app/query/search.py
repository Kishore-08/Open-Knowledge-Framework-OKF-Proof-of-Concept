"""
Knowledge search (Phase 10 - query).

Offers two complementary access paths over the knowledge base:

  * `search_keyword()`  - dependency-free filesystem keyword/metadata/tag search.
  * `search_semantic()` - semantic search over the Qdrant `okf_concepts` index,
    requiring a configured embed model. Falls back to keyword search when the
    vector store or API key is unavailable.
"""

import re
from typing import List, Optional

from app.core.config import settings
from app.okf.repository import list_concepts, search_concepts


_JOB_STATUS_MARKERS = (
    '"progress_percent"',
    '"stage_message"',
    '"indexed_documents"',
    '"rate_limit_hits"',
)


def _is_internal_job_record(result: dict) -> bool:
    """Return true for ingestion status JSON accidentally indexed as knowledge."""
    title = str(result.get("title") or "").strip()
    text = " ".join(
        str(result.get(field) or "")
        for field in ("title", "description", "snippet")
    ).lower()
    marker_count = sum(marker in text for marker in _JOB_STATUS_MARKERS)
    return (
        marker_count >= 2
        or "knowledge ingestion job status" in text
        or bool(re.fullmatch(r"[0-9a-f]{12}", title, re.IGNORECASE))
    )


def _rank_and_filter(results: List[dict], limit: int) -> List[dict]:
    """Deduplicate, order, and remove weak/non-citable retrieval results."""
    best_by_id: dict[str, dict] = {}
    for result in results:
        if _is_internal_job_record(result):
            continue
        key = str(result.get("id") or result.get("source_file") or result.get("title") or "")
        score = float(result.get("score") or 0.0)
        if key and (key not in best_by_id or score > float(best_by_id[key].get("score") or 0.0)):
            best_by_id[key] = result

    ranked = sorted(best_by_id.values(), key=lambda item: float(item.get("score") or 0.0), reverse=True)
    if not ranked:
        return []
    best_score = float(ranked[0].get("score") or 0.0)
    cutoff = max(settings.CITATION_MIN_SCORE, best_score * settings.CITATION_RELATIVE_SCORE)
    return [item for item in ranked if float(item.get("score") or 0.0) >= cutoff][: min(limit, 5)]


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
        limit = min(top_k or settings.TOP_K, 5)
        return {"mode": "keyword", "results": _rank_and_filter(keyword_results, limit)}

    if mode == "semantic":
        limit = min(top_k or settings.TOP_K, 5)
        results = _semantic_search(query, category=category, top_k=limit)
        results = _rank_and_filter(results, limit)
        return {"mode": "semantic", "results": results}

    # Auto mode combines both independent rankings. Scores from filesystem
    # keyword matching and vector similarity are not directly comparable, so
    # interleave by rank instead of applying one shared score threshold. This
    # also lets semantic retrieval recover misspellings that have zero keyword
    # matches (for example, "kubernets").
    limit = min(top_k or settings.TOP_K, 5)
    # Ask Qdrant for extra candidates because legacy internal records may be
    # discarded before the final five citations are selected.
    semantic_results = _semantic_search(query, category=category, top_k=max(limit * 3, limit))

    merged = _rank_and_filter(semantic_results + keyword_results, limit)

    # Report what actually served the request so callers can make the fallback
    # visible instead of presenting keyword-only results as hybrid search.
    if semantic_results and keyword_results:
        retrieval_mode = "hybrid"
    elif semantic_results:
        retrieval_mode = "semantic"
    else:
        retrieval_mode = "keyword"
    return {"mode": retrieval_mode, "results": merged}


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
