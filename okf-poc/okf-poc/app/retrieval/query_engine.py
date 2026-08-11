import logging
import os
from llama_index.core import Settings
from llama_index.llms.gemini import Gemini
from llama_index.embeddings.gemini import GeminiEmbedding
from google.api_core.retry import Retry
from google.generativeai import types as genai_types

from app.core.config import settings

logger = logging.getLogger(__name__)

# Disable the SDK's internal retry so quota (429) errors surface immediately
# instead of blocking the request thread for a minute or more.
_NO_RETRY = Retry(predicate=lambda exc: False)


def _request_options() -> genai_types.RequestOptions:
    return genai_types.RequestOptions(
        retry=_NO_RETRY,
        timeout=settings.LLM_TIMEOUT_SECONDS,
    )


def configure_llm_settings():
    """
    Configures the global LLM and Embedding models for LlamaIndex.
    We use fast, cost-effective models ideal for a PoC.
    Note: Ensure GEMINI_API_KEY or GOOGLE_API_KEY is set in your .env file.
    Uses transport='rest' for both Gemini (LLM) and GeminiEmbedding to bypass
    gRPC credentials plugin validation which fails for some API key formats.
    """
    api_key = settings.get_gemini_api_key()

    # Force the GOOGLE_API_KEY env var so google.generativeai picks it up
    os.environ["GOOGLE_API_KEY"] = api_key

    # gemini-flash-lite-latest: verified working on the free tier for fresh keys.
    # Using transport="rest" to prevent gRPC plugin_credentials header rejection errors,
    # plus request_options that disable google-api-core's blocking 429 retry.
    # Note: live answer generation goes through app/core/gemini_llm.complete();
    # this llama-index Settings wiring only serves consumers that build their
    # own index/retriever (e.g. semantic search in app.query.search).
    # Some SDK versions eagerly call genai.get_model() in the constructor and
    # raise a 400 for model names that do not resolve, so guard construction.
    try:
        Settings.llm = Gemini(
            model=settings.LLM_MODEL,
            temperature=settings.TEMPERATURE,
            api_key=api_key,
            transport="rest",
            request_options=_request_options(),
        )
    except Exception as exc:  # noqa: BLE001 - non-fatal; answer gen uses gemini_llm
        logger.warning(
            "llama-index Gemini LLM unavailable for model '%s' (%s); "
            "answer generation will use app.core.gemini_llm instead",
            settings.LLM_MODEL,
            exc,
        )
        Settings.llm = None

    # Gemini embeddings: use transport="rest" to prevent gRPC metadata header rejection issues
    embed_model = settings.EMBEDDING_MODEL
    if not embed_model.startswith("models/"):
        embed_model = f"models/{embed_model}"
    Settings.embed_model = GeminiEmbedding(
        model_name=embed_model,
        api_key=api_key,
        transport="rest",
    )
