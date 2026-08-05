"""
OKF Metadata Extractor — Phase 2.

Uses Gemini to extract structured metadata from document text.
Includes exponential backoff for 429 rate-limit errors so the pipeline
remains stable even on free-tier API keys.
"""

import time
import json
from pydantic import BaseModel, Field
from llama_index.llms.gemini import Gemini
from app.core.config import settings


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


def _heuristic_fallback(text: str) -> dict:
    """
    Fast, dependency-free metadata extraction when the LLM is unavailable.
    Uses the first non-empty lines of the document to build a title and
    guesses the category from common technical keywords.
    """
    lines = [l.strip() for l in text.splitlines() if l.strip()]
    title = lines[0][:80] if lines else "Unknown Document"

    # Remove markdown heading markers
    title = title.lstrip("#").strip() or "Unknown Document"

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
    import re
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


def generate_okf_metadata(text: str, max_retries: int = 3) -> dict:
    """
    Passes a preview of the document to an LLM to generate structured metadata.
    Retries with exponential backoff on 429 rate-limit errors.
    Falls back to heuristic extraction if LLM is unavailable after all retries.
    """
    try:
        api_key = settings.get_gemini_api_key()
    except ValueError:
        print("⚠️ No API key — using heuristic metadata extraction.")
        return _heuristic_fallback(text)

    llm = Gemini(model=settings.LLM_MODEL, temperature=settings.TEMPERATURE, api_key=api_key)

    # Only send the first 3000 characters to save tokens and time
    text_preview = text[:3000]

    prompt = (
        "You are an expert technical librarian. Analyze the following document text "
        "and extract the requested metadata. Output valid JSON matching the schema.\n\n"
        f"Text Preview:\n{text_preview}\n"
    )

    from llama_index.core import PromptTemplate
    prompt_tmpl = PromptTemplate(prompt)

    for attempt in range(1, max_retries + 1):
        try:
            print(f"🧠 Calling LLM to extract metadata (attempt {attempt}/{max_retries})...")
            response = llm.structured_predict(OKFMetadata, prompt_tmpl)
            metadata_dict = response.model_dump()
            return metadata_dict

        except Exception as e:
            err_str = str(e)
            if "429" in err_str or "quota" in err_str.lower() or "rate" in err_str.lower():
                wait = 30 * attempt  # 30s, 60s, 90s
                print(f"⚠️ Rate limit hit (429). Waiting {wait}s before retry {attempt}/{max_retries}...")
                time.sleep(wait)
            else:
                # Non-rate-limit error — fall back immediately
                print(f"❌ LLM metadata extraction failed (non-rate-limit): {e}")
                break

    print("⚠️ All LLM retries exhausted — using heuristic fallback.")
    return _heuristic_fallback(text)