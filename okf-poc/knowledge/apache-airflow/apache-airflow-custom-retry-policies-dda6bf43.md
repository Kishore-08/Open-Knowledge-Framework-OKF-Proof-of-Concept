---
id: apache-airflow-custom-retry-policies-dda6bf43
type: concept
title: Custom retry policies
description: For advanced cases, subclass `RetryPolicy`
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/tasks.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Custom retry policies

For advanced cases, subclass `RetryPolicy`
and implement `evaluate()`. Subclassing is the right choice when you need to inspect
exception *attributes* (status codes, response headers, payloads) that the declarative
`ExceptionRetryPolicy` rules cannot capture. The method receives the exception, try
number, max tries, and the full Airflow context (`dag_run`, `params`, etc.):

```
from datetime import timedelta

import requests

from airflow.sdk import RetryDecision, RetryPolicy


class HTTPStatusRetryPolicy(RetryPolicy):
    """Route retry decisions by HTTP status code, honouring Retry-After on 429s."""

    def evaluate(self, exception, try_number, max_tries, context=None):
        if isinstance(exception, requests.HTTPError) and exception.response is not None:
            status = exception.response.status_code
            if status == 429:  # rate limited -- honour Retry-After header
                retry_after = int(exception.response.headers.get("Retry-After", 60))
                return RetryDecision.retry(retry_delay=timedelta(seconds=retry_after))
            if 500 <= status < 600:  # server error -- worth retrying
                return RetryDecision.retry()
            if 400 <= status < 500:  # client error -- not retryable
                return RetryDecision.fail(reason=f"HTTP {status}")
        return RetryDecision.default()
```

A second pattern uses the run `context` to make decisions based on how the
DAG was triggered:

```
from airflow.sdk import RetryDecision, RetryPolicy


class BackfillAwareRetryPolicy(RetryPolicy):
    """Fail fast during backfills so historical errors surface immediately."""

    def evaluate(self, exception, try_number, max_tries, context=None):
        if context and context["dag_run"].run_type == "backfill":
            return RetryDecision.fail(reason="Backfill run -- not retrying")
        return RetryDecision.default()
```