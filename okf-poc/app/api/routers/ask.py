"""Ask the OKF knowledge base an AI-grounded question (Phase 12)."""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from typing import List, Optional

from app.query.engine import generate_answer

router = APIRouter(prefix="/ask", tags=["AI Assistant"])


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


@router.post("/", response_model=AskResponse)
async def ask(request: AskRequest):
    """
    Retrieves the most relevant concepts from the knowledge base and generates a
    grounded answer that cites its sources. Requires GEMINI_API_KEY for the
    LLM step; retrieval itself works without one.
    """
    try:
        result = generate_answer(
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
