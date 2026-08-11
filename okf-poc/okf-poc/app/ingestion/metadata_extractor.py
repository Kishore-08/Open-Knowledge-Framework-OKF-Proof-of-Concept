"""
OKF Metadata Extractor — Phase 2.

Uses Gemini to extract structured metadata from document text.
Includes exponential backoff for 429 rate-limit errors so the pipeline
remains stable even on free-tier API keys.

Uses a plain text-completion call plus JSON parsing instead of LlamaIndex's
`structured_predict` (function calling), which is an order of magnitude slower
and hangs when the free-tier Gemini quota is exhausted.
"""

import time
import json
import re
from typing import Optional
from pydantic import BaseModel, Field
from app.core.config import settings
from app.core.gemini_llm import complete as gemini_complete
from app.ingestion.status import update_status


class OKFMetadata(BaseModel):
    """
    Pydantic schema defining the strict metadata we want to extract from every document.
    This will become the YAML frontmatter in our OKF documents.
    """
    title: str = Field(description="A clear, concise title for the document.")
    summary: str = Field(description="A 2-3 sentence summary of the document's content.")
    document_type: str = Field(
        description="The category of the document (e.g., 'Kubernetes', 'Linux', 'Architecture', 'API Spec', 'FAQ', 'Tutorial')."
    )
    topics: list[str] = Field(description="A list of 3-5 key technical tags or topics covered in the text.")
    trust_level: str = Field(
        description="Assign 'High' if it looks like official docs, 'Medium' if general text, 'Low' if ambiguous."
    )


def _heuristic_fallback(text: str, source_name: str = None) -> Optional[dict]:
    """
    Fast, dependency-free metadata extraction when the LLM is unavailable.
    Uses the first heading (or first non-empty line) of the document to build
    a real title and guesses the category from common technical keywords.

    Returns None when the document has no usable content, so the ingestion
    pipeline can skip it instead of writing a placeholder "Unknown Document".
    """
    import re

    lines = [l.strip() for l in text.splitlines() if l.strip()]
    if not lines:
        return None

    def _clean_title(raw: str) -> str:
        # Strip leading punctuation-only tokens (e.g. a JSON '[' on its own line).
        raw = re.sub(r"^[\W_]+", "", raw or "").strip()
        return re.sub(r"\s+", " ", raw)[:80]

    # Prefer the first markdown heading; fall back to the first non-empty line.
    heading = next((l for l in lines if l.startswith("#")), None)
    title = _clean_title(re.sub(r"^#+\s*", "", heading) if heading else lines[0])

    # For JSON documents, try to derive a title from the first object's "title".
    if not title and (text.lstrip().startswith("[") or text.lstrip().startswith("{")):
        try:
            import json as _json

            data = _json.loads(text[:10000])
            if isinstance(data, list) and data and isinstance(data[0], dict):
                title = _clean_title(str(data[0].get("title") or ""))
            elif isinstance(data, dict):
                title = _clean_title(str(data.get("title") or ""))
        except Exception:  # noqa: BLE001
            pass

    # Fall back to the source filename when the body gives no usable title.
    if not title and source_name:
        stem = re.sub(r"\.(json|txt|md|pdf)$", "", source_name, flags=re.IGNORECASE)
        title = _clean_title(stem.replace("_", " ").replace("-", " "))

    if not title or title.lower() in ("unknown document", "unknown", "unclassified"):
        return None

    # Guess a category from the first 500 chars
    preview = text[:500].lower()
    if any(k in preview for k in ("kubernetes", "k8s", "pod", "deployment", "kubectl")):
        doc_type = "Kubernetes"
    elif any(k in preview for k in ("linux", "bash", "chmod", "systemd", "ubuntu")):
        doc_type = "Linux"
    elif any(k in preview for k in ("langchain", "llm", "chain", "agent", "prompt")):
        doc_type = "LangChain"
    elif any(k in preview for k in ("apache", "httpd", "nginx", "virtualhost")):
        doc_type = "Apache"
    elif any(k in preview for k in ("api", "rest", "endpoint", "swagger", "openapi")):
        doc_type = "API Spec"
    elif any(k in preview for k in ("architecture", "design", "component", "service mesh")):
        doc_type = "Architecture"
    else:
        doc_type = "Reference"

    # Extract simple topics from first 300 chars
    words = re.findall(r"\b[A-Za-z][a-z]{2,}\b", text[:300])
    topics = list(dict.fromkeys(w.lower() for w in words if len(w) > 3))[:5]

    summary = " ".join(lines[1:4]) if len(lines) > 1 else title

    return {
        "title": title,
        "summary": summary[:300],
        "document_type": doc_type,
        "topics": topics,
        "trust_level": "Medium",
    }


def _parse_json_response(text: str) -> Optional[dict]:
    """Best-effort parse of an LLM response into a dict, tolerating markdown fences."""
    if not text:
        return None
    cleaned = text.strip()
    # Strip markdown code fences if the model wrapped the JSON in them.
    cleaned = re.sub(r"^```(?:json)?\s*", "", cleaned, flags=re.IGNORECASE)
    cleaned = re.sub(r"\s*```\s*$", "", cleaned)
    # Fall back to the outermost {...} block if there is any prose around it.
    start = cleaned.find("{")
    end = cleaned.rfind("}")
    if start != -1 and end != -1 and end > start:
        candidate = cleaned[start : end + 1]
        try:
            data = json.loads(candidate)
            if isinstance(data, dict):
                return data
        except json.JSONDecodeError:
            pass
    try:
        data = json.loads(cleaned)
        return data if isinstance(data, dict) else None
    except json.JSONDecodeError:
        return None


def _estimate_token_counts(prompt: str, response_text: str = "") -> dict:
    """Very lightweight token usage estimate for UI reporting."""
    prompt_tokens = max(0, len(prompt) // 4)
    completion_tokens = max(0, len(response_text or "") // 4)
    return {
        "prompt_tokens_estimate": prompt_tokens,
        "completion_tokens_estimate": completion_tokens,
        "total_tokens_estimate": prompt_tokens + completion_tokens,
    }


def generate_okf_metadata(
    text: str,
    max_retries: int = 3,
    source_name: str = None,
) -> Optional[dict]:
    """
    Passes a preview of the document to an LLM to generate structured metadata.
    Retries with exponential backoff on 429 rate-limit errors.
    Falls back to heuristic extraction if the LLM is unavailable after all
    retries. Returns None when the document has no usable content.
    """
    if not text or not text.strip():
        print("⚠️ Empty document text — skipping metadata extraction.")
        return None

    try:
        settings.get_gemini_api_key()
    except ValueError:
        print("⚠️ No API key — using heuristic metadata extraction.")
        return _heuristic_fallback(text, source_name)

    # Only send the first 3000 characters to save tokens and time
    text_preview = text[:3000]

    prompt = (
        "You are an expert technical librarian. Analyze the following document text "
        "and output a SINGLE valid JSON object with exactly these keys:\n"
        '- "title": a clear, concise title for the document\n'
        '- "summary": a 2-3 sentence summary of the document content\n'
        '- "document_type": the category of the document (e.g. "Kubernetes", "Linux", '
        '"Apache", "LangChain", "Architecture", "API Spec", "FAQ", "Tutorial")\n'
        '- "topics": a JSON array of 3-5 key technical tags or topics covered\n'
        '- "trust_level": "High" if it looks like official docs, "Medium" for general '
        'text, "Low" if ambiguous\n\n'
        "Output ONLY the JSON object. No markdown, no explanations, no prose.\n\n"
        f"Source file name: {source_name or 'unknown'}\n"
        f"Text Preview:\n{text_preview}\n"
    )

    for attempt in range(1, max_retries + 1):
        try:
            print(f"🧠 Calling LLM to extract metadata (attempt {attempt}/{max_retries})...")
            response_text = gemini_complete(prompt, temperature=settings.TEMPERATURE)
            token_estimate = _estimate_token_counts(prompt, response_text)
            update_status(**token_estimate)
            parsed = _parse_json_response(response_text)
            if parsed is None:
                print("⚠️ LLM response was not valid JSON — falling back to heuristic.")
                return _heuristic_fallback(text, source_name)

            # Validate against the schema; tolerate missing/unexpected keys.
            metadata = OKFMetadata.model_validate(parsed)
            return metadata.model_dump()

        except Exception as e:
            err_str = str(e)
            if "429" in err_str or "quota" in err_str.lower() or "rate" in err_str.lower():
                # Short backoff (2s, 4s) so ingestion stays fast; a prolonged
                # wait here is what caused the 300s read timeouts in the UI.
                wait = min(2 * attempt, 4)
                print(f"⚠️ Rate limit hit (429). Waiting {wait}s before retry {attempt}/{max_retries}...")
                time.sleep(wait)
            else:
                # Non-rate-limit error — fall back immediately
                print(f"❌ LLM metadata extraction failed (non-rate-limit): {e}")
                break

    print("⚠️ All LLM retries exhausted — using heuristic fallback.")
    return _heuristic_fallback(text, source_name)