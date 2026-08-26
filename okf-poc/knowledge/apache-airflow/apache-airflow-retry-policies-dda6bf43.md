---
id: apache-airflow-retry-policies-dda6bf43
type: concept
title: Retry Policies
description: By default, Airflow retries failed tasks with a fixed count and delay
  regardless of the error type.
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/tasks.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Retry Policies

By default, Airflow retries failed tasks with a fixed count and delay regardless of the error type.
A **retry policy** lets you configure per-exception retry behaviour as a parameter on any task or operator,
without modifying task code.

Define a policy with rules that map exception types to actions, then apply it to a task:

airflow/example\_dags/example\_retry\_policy.py[[source]](https://airflow.apache.org/docs/apache-airflow/stable/_modules/airflow/example_dags/example_retry_policy.html)

```
from airflow.sdk import DAG, ExceptionRetryPolicy, RetryAction, RetryRule, task

API_RETRY_POLICY = ExceptionRetryPolicy(
    rules=[
        RetryRule(
            exception="requests.exceptions.HTTPError",
            action=RetryAction.RETRY,
            retry_delay=timedelta(minutes=5),
            reason="Rate limit, backing off",
        ),
        RetryRule(
            exception="google.auth.exceptions.RefreshError",
            action=RetryAction.FAIL,
            reason="Auth failure, not retryable",
        ),
        RetryRule(
            exception=ConnectionError,
            action=RetryAction.RETRY,
            retry_delay=timedelta(seconds=30),
        ),
    ],
)
```

airflow/example\_dags/example\_retry\_policy.py[[source]](https://airflow.apache.org/docs/apache-airflow/stable/_modules/airflow/example_dags/example_retry_policy.html)

```
with DAG(
    dag_id="example_retry_policy",
    schedule=None,
    catchup=False,
    tags=["example", "retry_policy"],
):

    @task(retries=5, retry_delay=timedelta(minutes=1), retry_policy=API_RETRY_POLICY)
    def call_external_api():
        import requests

        response = requests.get("https://api.example.com/data")
        response.raise_for_status()
        return response.json()

    call_external_api()
```