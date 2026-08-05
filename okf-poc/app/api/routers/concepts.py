"""
Knowledge Base REST API.

Exposes the filesystem knowledge repository (Phases 5-11) over HTTP:
concept browsing, metadata, keyword/tag/category search, and statistics.
"""

from fastapi import APIRouter, HTTPException, Query as FastAPIQuery
from typing import List, Optional

from app.okf import repository

router = APIRouter(prefix="/knowledge", tags=["Knowledge Base"])


@router.get("/stats")
async def stats():
    """Statistics over the knowledge repository."""
    return repository.knowledge_stats()


@router.get("/categories", response_model=List[str])
async def categories():
    """All knowledge categories."""
    return repository.list_categories()


@router.get("/concepts", response_model=List[dict])
async def concepts(category: Optional[str] = FastAPIQuery(None, description="Filter by category")):
    """Concept metadata summaries, optionally filtered by category."""
    return repository.list_concepts(category=category)


@router.get("/concepts/{concept_id}")
async def concept(concept_id: str):
    """Full detail of a single concept (metadata + Markdown body)."""
    result = repository.get_concept_dict(concept_id)
    if result is None:
        raise HTTPException(status_code=404, detail=f"Concept '{concept_id}' not found.")
    return result


@router.get("/search")
async def search(
    q: str = FastAPIQuery(..., description="Search query"),
    category: Optional[str] = FastAPIQuery(None, description="Filter by category"),
    tag: Optional[str] = FastAPIQuery(None, description="Filter by tag"),
):
    """Keyword + metadata + tag search over the knowledge repository."""
    results = repository.search_concepts(q, category=category, tag=tag)
    return {"query": q, "category": category, "tag": tag, "total": len(results), "results": results}


@router.get("/tags")
async def tags(category: Optional[str] = FastAPIQuery(None, description="Filter by category")):
    """All tags used in the knowledge base."""
    from app.query.search import search_tags

    return search_tags(category=category)
