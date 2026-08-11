"""
Tests for app.core.retry: the shared 429/quota retry policy used by both
answer generation (app.query.engine) and, as of this fix, document indexing
(app.retrieval.hybrid_search.index_documents). This is a regression test for
the root cause of the "only 79/874 documents indexed" bug: indexing used to
have no retry/backoff at all around embedding calls.
"""

import pytest

from app.core.retry import is_retryable_429, retry_with_backoff


@pytest.mark.parametrize(
    "message,expected",
    [
        ("429 Too Many Requests", True),
        ("google.api_core.exceptions.ResourceExhausted: 429 Quota exceeded", True),
        ("quota exceeded for this model", True),
        ("Rate limit hit, slow down", True),
        ("400 Bad Request: unknown model", False),
        ("connection reset by peer", False),
    ],
)
def test_is_retryable_429(message, expected):
    assert is_retryable_429(Exception(message)) is expected


def test_retry_with_backoff_succeeds_after_transient_429():
    calls = {"n": 0}
    sleeps = []

    def flaky():
        calls["n"] += 1
        if calls["n"] < 3:
            raise Exception("429 quota exceeded")
        return "ok"

    result = retry_with_backoff(
        flaky,
        max_retries=5,
        base_delay=1.0,
        sleep=sleeps.append,
    )

    assert result == "ok"
    assert calls["n"] == 3
    # exponential backoff: 1.0, 2.0 for the two retried attempts
    assert sleeps == [1.0, 2.0]


def test_retry_with_backoff_gives_up_after_max_retries():
    calls = {"n": 0}

    def always_fails():
        calls["n"] += 1
        raise Exception("429 quota exceeded")

    with pytest.raises(Exception, match="429"):
        retry_with_backoff(always_fails, max_retries=3, base_delay=0.01, sleep=lambda _: None)

    assert calls["n"] == 3  # no more attempts than max_retries


def test_retry_with_backoff_does_not_retry_non_429_errors():
    calls = {"n": 0}

    def not_retryable():
        calls["n"] += 1
        raise ValueError("bad input")

    with pytest.raises(ValueError):
        retry_with_backoff(not_retryable, max_retries=5, base_delay=0.01, sleep=lambda _: None)

    assert calls["n"] == 1  # fails fast, no retries burned on a non-quota error
