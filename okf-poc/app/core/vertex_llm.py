from functools import lru_cache
from typing import Optional

from google import genai
from google.genai import types

from app.core.config import settings
from app.core.gcp_auth import get_vertex_credentials


@lru_cache(maxsize=1)
def _client() -> genai.Client:
    """Reuse the Vertex client and its HTTP connection pool across queries."""
    settings.validate_vertex_config()

    return genai.Client(
        vertexai=True,
        project=settings.VERTEX_AI_PROJECT_ID,
        location=settings.VERTEX_AI_LOCATION,
        credentials=get_vertex_credentials(),
        http_options=types.HttpOptions(
            api_version="v1"
        ),
    )


def complete(
    prompt: str,
    *,
    temperature: Optional[float] = None,
) -> str:

    client = _client()

    response = client.models.generate_content(
        model=settings.VERTEX_LLM_MODEL,
        contents=prompt,
        config=types.GenerateContentConfig(
            temperature=(
                settings.TEMPERATURE
                if temperature is None
                else temperature
            ),
            max_output_tokens=settings.LLM_MAX_OUTPUT_TOKENS,
            thinking_config=types.ThinkingConfig(thinking_level="minimal"),
        ),
    )

    if not response.text:
        raise RuntimeError("Vertex AI returned an empty response")

    usage = response.usage_metadata

    print("Input/context tokens:", usage.prompt_token_count)
    print("Visible output tokens:", usage.candidates_token_count)
    print("Thinking tokens:", usage.thoughts_token_count or 0)
    print("Tool-result tokens:", usage.tool_use_prompt_token_count or 0)
    print("Total tokens:", usage.total_token_count)

    return response.text
