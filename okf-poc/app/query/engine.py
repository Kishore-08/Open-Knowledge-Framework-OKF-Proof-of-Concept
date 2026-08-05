"""
AI answer generation over the OKF knowledge base (Phase 12 - AI).

Retrieves the most relevant concepts from the repository/index and generates a
grounded answer using the Gemini LLM, citing the concept source URLs.

The LLM is the last layer of the pipeline: everything before it (crawl, clean,
convert, index, search) works without an API key. Answer generation is the only
step that requires `GEMINI_API_KEY`.
"""

from dataclasses import dataclass, field
from typing import List, Optional

from app.core.config import settings
from app.okf.repository import get_concept_dict
from app.query.search import search


@dataclass
class QueryResult:
    """Structured result of an AI query: the answer plus its grounding evidence."""

    answer: str
    sources: List[dict] = field(default_factory=list)
    retrieval_mode: str = ""


def generate_answer(
    query: str,
    *,
    category: Optional[str] = None,
    top_k: Optional[int] = None,
) -> QueryResult:
    """
    Answer a question grounded strictly in the OKF knowledge base.

    1. Retrieval: run hybrid search (semantic + keyword) over the repository.
    2. Prompting: give the LLM only the retrieved concept texts + source URLs.
    3. Answering: the LLM must answer from context and cite its sources.
    """
    top_k = top_k or settings.TOP_K

    # 1. Retrieval (works without an API key)
    retrieved = search(query, category=category, mode="auto", top_k=top_k)
    results = retrieved["results"]
    sources = [
        {
            "id": r.get("id"),
            "title": r.get("title"),
            "category": r.get("category"),
            "description": r.get("description"),
            "source_url": r.get("source_url"),
            "score": r.get("score"),
            "snippet": r.get("snippet", ""),
        }
        for r in results
    ]

    if not sources:
        return QueryResult(
            answer="I could not find any matching concepts in the OKF knowledge base "
                   "for your question. Please rephrase it or browse the knowledge base.",
            sources=[],
            retrieval_mode=retrieved.get("mode", ""),
        )

    # 2. Build a strict context block.
    context_parts = []
    for idx, r in enumerate(results, start=1):
        title = r.get("title") or r.get("id")
        url = r.get("source_url") or ""
        snippet = r.get("snippet") or r.get("description") or ""
        context_parts.append(f"[{idx}] {title}\nSource: {url}\n{snippet}")
    context_block = "\n\n".join(context_parts)

    # 3. Generate the grounded answer with the LLM.
    try:
        answer = _call_llm(query, context_block)
    except Exception as exc:  # noqa: BLE001
        answer = (
            "The knowledge base returned the following relevant concepts, but answer "
            f"generation requires a Gemini API key (set GEMINI_API_KEY): {exc}\n\n"
            + "\n".join(f"- {r.get('title')} ({r.get('source_url')})" for r in results)
        )

    return QueryResult(answer=answer, sources=sources, retrieval_mode=retrieved.get("mode", ""))


def _call_llm(query: str, context_block: str) -> str:
    """Call the Gemini LLM through LlamaIndex with a strict grounding prompt."""
    from llama_index.core import Settings, PromptTemplate
    from llama_index.llms.gemini import Gemini

    api_key = settings.get_gemini_api_key()
    llm = Gemini(model=settings.LLM_MODEL, temperature=settings.TEMPERATURE, api_key=api_key)

    prompt_tmpl = PromptTemplate(
        "You are an enterprise AI assistant powered by the Open Knowledge Framework (OKF).\n"
        "Context information from our OKF knowledge base is provided below.\n"
        "---------------------\n"
        "{context_str}\n"
        "---------------------\n"
        "Given the context information and strictly NO prior knowledge, answer the user's query.\n"
        "RULES:\n"
        "1. You MUST strictly base your answer on the provided context.\n"
        "2. Every time you use information, you MUST cite the source document inline using its title.\n"
        "3. If the context does not contain the answer, you must say: "
        "'I cannot answer this based on the OKF knowledge base.' Do not guess or hallucinate.\n\n"
        "Query: {query_str}\n"
        "Answer: "
    )
    response = llm.complete(
        prompt_tmpl.format(query_str=query, context_str=context_block)
    )
    return response.text
