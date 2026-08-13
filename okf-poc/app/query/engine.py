"""
AI answer generation over the OKF knowledge base (Phase 12 - AI).

Retrieves the most relevant concepts from the repository/index and generates a
grounded answer using the Gemini LLM, citing the concept source URLs.

The LLM is the last layer of the pipeline: everything before it (crawl, clean,
convert, index, search) works without an API key. Answer generation is the only
step that requires `GEMINI_API_KEY`.
"""

from dataclasses import dataclass, field
from pathlib import Path
import time
from typing import List, Optional

import yaml

from app.core.config import settings
from app.core.retry import retry_with_backoff
from app.okf.repository import get_concept_dict
from app.query.search import search


@dataclass
class QueryResult:
    """Structured result of an AI query: the answer plus its grounding evidence."""

    answer: str
    sources: List[dict] = field(default_factory=list)
    retrieval_mode: str = ""


def _matching_supplements(query: str) -> List[dict]:
    """Load source-backed context supplements matching the user's wording."""
    path = Path("config/context_supplements.yaml")
    if not path.exists():
        return []
    entries = (yaml.safe_load(path.read_text(encoding="utf-8")) or {}).get(
        "supplements", []
    )
    query_lower = query.lower()
    return [
        {
            "id": entry["id"],
            "title": entry["title"],
            "category": entry.get("category", ""),
            "description": entry["content"],
            "source_url": entry["source_url"],
            "score": 1.0,
            "snippet": entry["content"],
        }
        for entry in entries
        if any(term.lower() in query_lower for term in entry.get("match_terms", []))
    ]


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

    # Some upstream pages are split into narrow concepts, so a definition and
    # its key behavioral sentence can fall outside the top-k window. Merge
    # small, explicitly sourced supplements before truncating the context.
    supplements = _matching_supplements(query)
    if supplements:
        supplement_ids = {item["id"] for item in supplements}
        results = supplements + [r for r in results if r.get("id") not in supplement_ids]
        results = results[:top_k]

    # Search results intentionally carry short previews, and semantic results
    # may represent a chunk from the middle of a concept. Answer generation
    # needs the complete authoritative concept; otherwise a relevant hit can
    # omit the exact list or definition the user asked for. Keep the context
    # bounded by the existing per-concept size setting.
    for result in results:
        concept = get_concept_dict(result.get("id") or "")
        if concept and concept.get("content"):
            result["snippet"] = concept["content"][: settings.CONCEPT_MAX_CHARS]

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
            f"generation is currently unavailable: {exc}. Check the configured "
            "AI provider credentials and quota, then try again.\n\n"
            + "\n".join(f"- {r.get('title')} ({r.get('source_url')})" for r in results)
        )

    return QueryResult(answer=answer, sources=sources, retrieval_mode=retrieved.get("mode", ""))


def _call_llm(query: str, context_block: str) -> str:
    """Call the Gemini LLM with a strict grounding prompt."""
    if settings.AI_PROVIDER.lower() == "vertex":
        from app.core.vertex_llm import complete as llm_complete
    else:
        from app.core.gemini_llm import complete as llm_complete

    prompt_text = (
        "You are an enterprise AI assistant powered by the Open Knowledge Framework (OKF).\n"
        "Context information from our OKF knowledge base is provided below.\n"
        "---------------------\n"
        f"{context_block}\n"
        "---------------------\n"
        "Given the context information and strictly NO prior knowledge, answer the user's query.\n"
        "RULES:\n"
        "1. You MUST strictly base your answer on the provided context.\n"
        "2. Every time you use information, you MUST cite the source document inline using its title.\n"
        "3. If the context does not contain the answer, you must say: "
        "'I cannot answer this based on the OKF knowledge base.' Do not guess or hallucinate.\n"
        "4. Answer only what the user asked. Lead with the direct definition or conclusion, "
        "and include every part of the question.\n"
        "5. Before answering, silently identify the requested answer slots and fill each one "
        "from the context. For an object, include its canonical definition, primary purpose, "
        "and the main way it is used when those are relevant. For a failure or process, name "
        "the actor, immediate action, and resulting behavior. For an architecture, name each "
        "core component and its role. For a comparison, state the defining mechanism of both sides.\n"
        "6. Be concise: normally use one or two sentences (at most three for a comparison "
        "or multi-part summary). Preserve distinct facts needed to fill the requested slots, "
        "but do not add examples, implementation details, caveats, recommendations, or related "
        "facts unless the question explicitly asks for them.\n"
        "7. Prefer a close paraphrase of the shortest, most directly relevant source passages. "
        "Do not replace a precise source definition with a broader description.\n\n"
        f"Query: {query}\n"
        "Answer: "
    )

    # Retry with exponential backoff on Gemini 429 quota/rate-limit errors.
    # The free tier reports `limit: 0` for generate_content_free_tier_requests,
    # so transient quota exhaustion is retried before degrading gracefully.
    def _on_retry(attempt: int, delay: float, exc: Exception) -> None:
        print(
            f"⚠️ Gemini rate limit (429) hit, retrying in {delay:.0f}s "
            f"(attempt {attempt}/{settings.LLM_MAX_RETRIES})"
        )

    return retry_with_backoff(
        lambda: llm_complete(prompt_text, temperature=settings.TEMPERATURE),
        max_retries=settings.LLM_MAX_RETRIES,
        base_delay=settings.LLM_RETRY_BASE_DELAY,
        sleep=time.sleep,
        on_retry=_on_retry,
    )
