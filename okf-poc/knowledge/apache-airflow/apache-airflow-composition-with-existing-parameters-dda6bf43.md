---
id: apache-airflow-composition-with-existing-parameters-dda6bf43
type: concept
title: Composition with existing parameters
description: '| Parameter | Behaviour when `retry_policy` is set |'
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/tasks.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Composition with existing parameters

| Parameter | Behaviour when `retry_policy` is set |
| --- | --- |
| `retries` | Still the maximum retry count. Policy can fail earlier but not exceed it. |
| `retry_delay` / `retry_exponential_backoff` / `max_retry_delay` | Used when the policy returns DEFAULT or when `RetryDecision.retry_delay` is None. |
| `on_retry_callback` | Fires on all retries, including policy-driven retries. |
| `AirflowFailException` | Always takes precedence. The policy is never consulted for this exception. |