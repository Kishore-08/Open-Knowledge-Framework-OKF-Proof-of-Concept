from typing import Optional

from google import genai
from google.genai import types

from app.core.config import settings
from app.core.gcp_auth import get_vertex_credentials


def _client() -> genai.Client:
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
            )
        ),
    )

    if not response.text:
        raise RuntimeError("Vertex AI returned an empty response")

    return response.text
