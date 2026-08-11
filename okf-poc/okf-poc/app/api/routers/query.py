"""
Q&A endpoints over the OKF knowledge base (consolidated module).

Both `/api/v1/query/` (used by the Streamlit chat UI) and `/api/v1/ask/`
(richer assistant endpoint) delegate to the single grounded answer engine,
`app.query.engine.generate_answer`. This removes the old duplicate
LlamaIndex query-engine path (`app.retrieval.query_engine.get_query_engine`)
that bypassed 429/backoff handling and returned HTTP 500 on quota errors.

The heavy retrieval + LLM work runs in a thread pool so FastAPI's event loop
is never blocked - preventing 60-second timeout errors.
"""

import asyncio
from typing import List, Optional

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from app.query.engine import generate_answer


# ---------------------------------------------------------------------------
# /api/v1/query/ - legacy endpoint used by the Streamlit chat UI
# ---------------------------------------------------------------------------

router = APIRouter(prefix="/query", tags=["Retrieval"])


class QueryRequest(BaseModel):
    query: str = Field(..., description="The user's question to ask the knowledge base.")


class Citation(BaseModel):
    """
    Represents a specific OKF concept used to answer the query.
    Fulfills the requirement to 'cite source documents'.
    """
    title: str = Field(description="The title from the OKF YAML frontmatter")
    content: str = Field(description="The actual text chunk retrieved")
    score: float = Field(description="The retrieval relevance score (0.0 to 1.0)")


class QueryResponse(BaseModel):
    answer: str = Field(description="The generated answer from the LLM")
    citations: List[Citation] = Field(description="List of OKF sources used to construct the answer")


@router.post("/", response_model=QueryResponse)
async def query_knowledge_base(request: QueryRequest):
    """
    Queries the OKF knowledge base and generates a grounded answer via LLM.
    Retrieval works without an API key; answer generation degrades gracefully
    (returns the retrieved sources) when Gemini is unavailable or rate-limited.
    """
    try:
        print(f"🔍 Received query: {request.query}")
        result = await asyncio.to_thread(generate_answer, request.query)
        return QueryResponse(
            answer=result.answer,
            citations=[
                Citation(
                    title=s.get("title") or "Unknown OKF Source",
                    content=s.get("snippet") or s.get("description") or "",
                    score=float(s.get("score") or 0.0),
                )
                for s in result.sources
            ],
        )
    except Exception as e:
        print(f"❌ API Error during query: {e}")
        raise HTTPException(status_code=500, detail=f"Query failed: {str(e)}")


# ---------------------------------------------------------------------------
# /api/v1/ask/ - richer assistant endpoint (optional category + top_k)
# ---------------------------------------------------------------------------

ask_router = APIRouter(prefix="/ask", tags=["AI Assistant"])


class AskRequest(BaseModel):
    question: str = Field(..., description="The question to ask the OKF knowledge base.")
    category: Optional[str] = Field(None, description="Optionally restrict to one category.")
    top_k: Optional[int] = Field(None, description="Number of concepts to retrieve.")


class SourceEvidence(BaseModel):
    id: str
    title: str
    category: str = ""
    description: str = ""
    source_url: str = ""
    score: float = 0.0
    snippet: str = ""


class AskResponse(BaseModel):
    question: str
    answer: str
    retrieval_mode: str = ""
    sources: List[SourceEvidence] = Field(default_factory=list)


@ask_router.post("/", response_model=AskResponse)
async def ask(request: AskRequest):
    """
    Retrieves the most relevant concepts from the knowledge base and generates a
    grounded answer that cites its sources. Requires GEMINI_API_KEY for the
    LLM step; retrieval itself works without one.
    """
    try:
        result = await asyncio.to_thread(
            generate_answer,
            request.question,
            category=request.category,
            top_k=request.top_k,
        )
        return AskResponse(
            question=request.question,
            answer=result.answer,
            retrieval_mode=result.retrieval_mode,
            sources=[SourceEvidence(**s) for s in result.sources],
        )
    except Exception as e:
        print(f"❌ API Error during ask: {e}")
        raise HTTPException(status_code=500, detail=f"Ask failed: {str(e)}")
