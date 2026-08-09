"""
Shared Gemini 429/quota retry-detection.

Previously this predicate was only defined inside app.query.engine and only
used to protect answer generation (app.core.gemini_llm.complete). The
embedding calls made during indexing (app.retrieval.hybrid_search.
index_documents -> VectorStoreIndex/GeminiEmbedding) had no equivalent
protection, which is why ingestion silently stopped after ~79/874 documents
on the free tier: the batch just raised on the first 429 and gave up,
leaving the vector index (and therefore semantic search) incomplete. This
module lets both call sites share one retry policy instead of drifting.
"""

from typing import Callable, TypeVar

T = TypeVar("T")


def is_retryable_429(exc: Exception) -> bool:
    """Return True when an exception indicates a Gemini quota/rate-limit error."""
    text = str(exc)
    if "429" in text:
        return True
    lowered = text.lower()
    return "quota" in lowered or "rate limit" in lowered or "resource_exhausted" in lowered


def retry_with_backoff(
    fn: Callable[[], T],
    *,
    max_retries: int,
    base_delay: float,
    sleep: Callable[[float], None],
    on_retry: Callable[[int, float, Exception], None] = lambda attempt, delay, exc: None,
) -> T:
    """
    Call `fn()`, retrying with exponential backoff on retryable 429 errors.

    Raises the last exception once retries are exhausted or the error is not
    retryable. `sleep` is injected so callers can use `time.sleep` (sync
    code); tests can inject a no-op.
    """
    last_exc: Exception = RuntimeError("retry_with_backoff called with max_retries < 1")
    for attempt in range(1, max_retries + 1):
        try:
            return fn()
        except Exception as exc:  # noqa: BLE001 - re-raised below if not retryable/exhausted
            last_exc = exc
            if attempt == max_retries or not is_retryable_429(exc):
                raise
            delay = base_delay * (2 ** (attempt - 1))
            on_retry(attempt, delay, exc)
            sleep(delay)
    raise last_exc
