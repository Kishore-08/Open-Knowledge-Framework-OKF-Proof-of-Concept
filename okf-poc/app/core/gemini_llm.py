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


def _model(model_name: Optional[str] = None):
    """Return a configured GenerativeModel (REST transport)."""
    api_key = settings.get_gemini_api_key()
    genai.configure(api_key=api_key, transport="rest")
    return genai.GenerativeModel(model_name or settings.LLM_MODEL)


def complete(prompt: str, *, temperature: Optional[float] = None) -> str:
    """
    Run a single generation call and return the text.

    If the configured model is unavailable for this key (400 unknown model,
    404, or 429 quota exhausted), transparently retries once with
    ``LLM_FALLBACK_MODEL``, which shares the same key but has a separate
    quota pool. Raises if the fallback also fails; callers that want
    resilience against transient quota exhaustion should wrap this in their
    own short retry loop.
    """
    gen_config = None
    if temperature is not None:
        gen_config = genai_types.GenerationConfig(temperature=temperature)

    candidates = [settings.LLM_MODEL, settings.LLM_FALLBACK_MODEL]
    seen: set = set()
    last_exc: Optional[Exception] = None
    for model_name in candidates:
        if not model_name or model_name in seen:
            continue
        seen.add(model_name)
        try:
            response = _model(model_name).generate_content(
                prompt,
                generation_config=gen_config,
                request_options=_request_options(),
            )
            return response.text
        except Exception as exc:  # noqa: BLE001 - fall back on any model failure
            last_exc = exc
            if model_name == settings.LLM_MODEL:
                # Surface the primary-model error in the final message so the
                # user knows why the configured model was skipped.
                exc.add_note(
                    f"model '{settings.LLM_MODEL}' failed; tried fallback '{settings.LLM_FALLBACK_MODEL}'"
                )
    assert last_exc is not None
    raise last_exc
