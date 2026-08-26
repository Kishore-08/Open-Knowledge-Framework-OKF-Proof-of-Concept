---
id: apache-airflow-reusable-policies-dda6bf43
type: concept
title: Reusable policies
description: 'Define a policy once and share it across DAGs via `default_args` or
  a shared module:'
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/tasks.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Reusable policies

Define a policy once and share it across DAGs via `default_args` or a shared module:

airflow/example\_dags/example\_retry\_policy.py[[source]](https://airflow.apache.org/docs/apache-airflow/stable/_modules/airflow/example_dags/example_retry_policy.html)

```
# policies.py -- import in any DAG
STANDARD_RETRY_POLICY = ExceptionRetryPolicy(
    rules=[
        RetryRule(exception="requests.exceptions.HTTPError", action=RetryAction.FAIL),
        RetryRule(exception=ConnectionError, retry_delay=timedelta(seconds=10)),
    ],
)
```