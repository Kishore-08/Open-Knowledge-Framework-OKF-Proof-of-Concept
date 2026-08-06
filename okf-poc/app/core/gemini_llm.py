"""
Robust Gemini generation helper.

The bundled llama-index Gemini integration (`llama_index.llms.gemini`) is
deprecated and, by default, uses the gRPC transport. When the free-tier quota
is exhausted, the underlying google-api-core retry logic can block for a minute
or longer per call, which is exactly what caused the 60-second search timeouts
and the hanging ingestion pipeline.

This thin wrapper configures `google.generativeai` with:
  * REST transport (no gRPC hangs),
  * `request_options` that disable the SDK's built-in retry so quota (429)
    errors surface immediately instead of blocking,
  * an explicit timeout.

Callers implement their own short, bounded retry loops when they care about
transient quota exhaustion.
"""

from typing import Optional

from google.api_core.retry import Retry
from google.generativeai import types as genai_types
import google.generativeai as genai

from app.core.config import settings

# Disable the SDK's internal retry so a 429 raises immediately rather than
# blocking for minutes inside google-api-core.
_NO_RETRY = Retry(predicate=lambda exc: False)


def _request_options() -> genai_types.RequestOptions:
    return genai_types.RequestOptions(
        retry=_NO_RETRY,
        timeout=settings.LLM_TIMEOUT_SECONDS,
    )


def _model():
    """Return a configured GenerativeModel (REST transport)."""
    api_key = settings.get_gemini_api_key()
    genai.configure(api_key=api_key, transport="rest")
    return genai.GenerativeModel(settings.LLM_MODEL)


def complete(prompt: str, *, temperature: Optional[float] = None) -> str:
    """
    Run a single generation call and return the text.

    Raises on failure (429 quota errors surface immediately). Callers that want
    resilience against transient quota exhaustion should wrap this in their own
    short retry loop.
    """
    gen_config = None
    if temperature is not None:
        gen_config = genai_types.GenerationConfig(temperature=temperature)

    response = _model().generate_content(
        prompt,
        generation_config=gen_config,
        request_options=_request_options(),
    )
    return response.text
