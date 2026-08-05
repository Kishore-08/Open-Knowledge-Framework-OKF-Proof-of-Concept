from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from typing import List
import asyncio
import logging

# Import the retrieval engine we built in Phase 3
from app.retrieval import get_query_engine

router = APIRouter(prefix="/query", tags=["Retrieval"])

# Request/Response Models
class QueryRequest(BaseModel):
    query: str = Field(..., description="The user's question to ask the knowledge base.")

class Citation(BaseModel):
    """
    Represents a specific chunk of an OKF document used to answer the query.
    Fulfills the requirement to 'cite source documents'.
    """
    title: str = Field(description="The title from the OKF YAML frontmatter")
    content: str = Field(description="The actual text chunk retrieved")
    score: float = Field(description="The hybrid search relevance score (0.0 to 1.0)")

class QueryResponse(BaseModel):
    answer: str = Field(description="The generated answer from the LLM")
    citations: List[Citation] = Field(description="List of OKF sources used to construct the answer")


def _run_query(query_text: str) -> dict:
    """
    Synchronous helper that runs the full retrieval + LLM pipeline.
    Called from a thread pool to avoid blocking the async event loop.
    """
    engine = get_query_engine()
    response = engine.query(query_text)

    citations = []
    if response.source_nodes:
        for node_with_score in response.source_nodes:
            node = node_with_score.node
            citations.append({
                "title": node.metadata.get("title", "Unknown OKF Source"),
                "content": node.text.strip(),
                "score": round(node_with_score.score, 4) if node_with_score.score else 0.0,
            })

    return {"answer": str(response), "citations": citations}


@router.post("/", response_model=QueryResponse)
async def query_knowledge_base(request: QueryRequest):
    """
    Queries the Qdrant Vector DB using Hybrid Search and generates an answer via LLM.
    Ensures strict adherence to ingested OKF sources to prevent hallucination.

    The heavy retrieval + LLM work is offloaded to a thread pool so the async
    event loop is never blocked - preventing 60-second timeout errors.
    """
    try:
        print(f"🔍 Received query: {request.query}")

        # asyncio.to_thread runs the synchronous _run_query in a thread pool,
        # keeping FastAPI's event loop free during the embedding + LLM call.
        result = await asyncio.to_thread(_run_query, request.query)

        return QueryResponse(
            answer=result["answer"],
            citations=[Citation(**c) for c in result["citations"]],
        )

    except Exception as e:
        print(f"❌ API Error during query: {e}")
        raise HTTPException(status_code=500, detail=f"Query failed: {str(e)}")