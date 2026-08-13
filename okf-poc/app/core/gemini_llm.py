from typing import Optional

from google import genai
from google.genai import types

from app.core.config import settings
def _client() -> genai.Client:
    api_key = settings.get_gemini_api_key()

    return genai.Client(
        api_key=api_key,
    )


def complete(
    prompt: str,
    *,
    temperature: Optional[float] = None,
) -> str:

    client = _client()

    candidates = [
        settings.LLM_MODEL,
        settings.LLM_FALLBACK_MODEL,
    ]

    seen: set[str] = set()
    last_exc: Optional[Exception] = None

    for model_name in candidates:

        if not model_name or model_name in seen:
            continue

        seen.add(model_name)

        try:
            response = client.models.generate_content(
                model=model_name,
                contents=prompt,
                config=types.GenerateContentConfig(
                    thinking_config=types.ThinkingConfig(
                        thinking_level="minimal"
                    )
                ),
            )

            if not response.text:
                raise RuntimeError(
                    f"Gemini returned an empty response for {model_name}"
                )

            return response.text

        except Exception as exc:
            last_exc = exc

            print(
                f"⚠️ Gemini model '{model_name}' failed: {exc}"
            )

            continue

    if last_exc is not None:
        raise last_exc

    raise RuntimeError("No Gemini models configured")
