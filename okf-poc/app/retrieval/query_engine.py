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


def _configure_gemini_settings():
    api_key = settings.get_gemini_api_key()

    os.environ["GOOGLE_API_KEY"] = api_key

    Settings.llm = Gemini(
        model=settings.LLM_MODEL,
        temperature=settings.TEMPERATURE,
        api_key=api_key,
        transport="rest",
        request_options=_request_options(),
    )

    embed_model = settings.EMBEDDING_MODEL

    if not embed_model.startswith("models/"):
        embed_model = f"models/{embed_model}"

    Settings.embed_model = GeminiEmbedding(
        model_name=embed_model,
        api_key=api_key,
        transport="rest",
    )

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

def _configure_vertex_settings():
    settings.validate_vertex_config()
    from app.core.vertex_embeddings import VertexAIEmbedding

    Settings.llm = None
    Settings.embed_model = VertexAIEmbedding(
        model_name=settings.VERTEX_EMBEDDING_MODEL,
        embed_batch_size=10,
    )


def configure_llm_settings():
    """Configure LlamaIndex for the selected Google AI API surface."""
    if settings.is_vertex_enabled():
        _configure_vertex_settings()
    elif settings.is_gemini_enabled():
        _configure_gemini_settings()
    else:
        raise ValueError("AI_PROVIDER must be either 'vertex' or 'gemini'")
