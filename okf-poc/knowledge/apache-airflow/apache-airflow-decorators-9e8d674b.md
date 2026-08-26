---
id: apache-airflow-decorators-9e8d674b
type: concept
title: Decorators
description: Dag authors can use decorators to author Dags using the [TaskFlow](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/taskflow.html)
  concept.
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/public-airflow-interface.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Decorators

Dag authors can use decorators to author Dags using the [TaskFlow](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/taskflow.html) concept.
All Decorators derive from `TaskDecorator`.

The primary decorators for Dag authors are now in the airflow.sdk namespace:
[`dag()`](https://airflow.apache.org/docs/task-sdk/stable/api.html#airflow.sdk.dag "(in Apache Airflow Task SDK v1.4.0)"), [`task()`](https://airflow.apache.org/docs/task-sdk/stable/api.html#airflow.sdk.task "(in Apache Airflow Task SDK v1.4.0)"), [`asset()`](https://airflow.apache.org/docs/task-sdk/stable/api.html#airflow.sdk.asset "(in Apache Airflow Task SDK v1.4.0)"),
[`setup()`](https://airflow.apache.org/docs/task-sdk/stable/api.html#airflow.sdk.setup "(in Apache Airflow Task SDK v1.4.0)"), [`task_group()`](https://airflow.apache.org/docs/task-sdk/stable/api.html#airflow.sdk.task_group "(in Apache Airflow Task SDK v1.4.0)"), [`teardown()`](https://airflow.apache.org/docs/task-sdk/stable/api.html#airflow.sdk.teardown "(in Apache Airflow Task SDK v1.4.0)"),
[`chain()`](https://airflow.apache.org/docs/task-sdk/stable/api.html#airflow.sdk.chain "(in Apache Airflow Task SDK v1.4.0)"), [`chain_linear()`](https://airflow.apache.org/docs/task-sdk/stable/api.html#airflow.sdk.chain_linear "(in Apache Airflow Task SDK v1.4.0)"), [`cross_downstream()`](https://airflow.apache.org/docs/task-sdk/stable/api.html#airflow.sdk.cross_downstream "(in Apache Airflow Task SDK v1.4.0)"),
[`get_current_context()`](https://airflow.apache.org/docs/task-sdk/stable/api.html#airflow.sdk.get_current_context "(in Apache Airflow Task SDK v1.4.0)") and [`get_parsing_context()`](https://airflow.apache.org/docs/task-sdk/stable/api.html#airflow.sdk.get_parsing_context "(in Apache Airflow Task SDK v1.4.0)").

Airflow has a set of Decorators that are considered public. You are free to extend their functionality
by extending them:

Note

Decorators are now part of the airflow.sdk namespace.
For detailed API documentation, see the [Task SDK Reference](https://airflow.apache.org/docs/task-sdk/stable/).

You can read more about creating custom Decorators in [Creating Custom @task Decorators](https://airflow.apache.org/docs/apache-airflow/stable/howto/create-custom-decorator.html).