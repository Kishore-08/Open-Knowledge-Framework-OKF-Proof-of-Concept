---
id: apache-airflow-dags-9e8d674b
type: concept
title: Dags
description: The Dag is Airflow’s core entity that represents a recurring workflow.
  You can create a Dag by
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/public-airflow-interface.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Dags

The Dag is Airflow’s core entity that represents a recurring workflow. You can create a Dag by
instantiating the [`DAG`](https://airflow.apache.org/docs/task-sdk/stable/api.html#airflow.sdk.DAG "(in Apache Airflow Task SDK v1.4.0)") class in your Dag file. Dags can also have parameters
specified via [`Param`](https://airflow.apache.org/docs/task-sdk/stable/api.html#airflow.sdk.Param "(in Apache Airflow Task SDK v1.4.0)") class.

The recommended way to create Dags is using the [`dag()`](https://airflow.apache.org/docs/task-sdk/stable/api.html#airflow.sdk.dag "(in Apache Airflow Task SDK v1.4.0)") decorator
from the airflow.sdk namespace.

Airflow has a set of example Dags that you can use to learn how to write Dags

- [airflow.example\_dags](https://airflow.apache.org/docs/apache-airflow/stable/_api/airflow/example_dags/index.html)

You can read more about Dags in [Dags](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/dags.html).

References for the modules used in Dags are here:

Note

The airflow.sdk namespace provides the primary interface for Dag authors.
For detailed API documentation, see the [Task SDK Reference](https://airflow.apache.org/docs/task-sdk/stable/).

Note

The `DagBag` class is used internally by Airflow for loading Dags
from files and folders. Dag authors should use the [`DAG`](https://airflow.apache.org/docs/task-sdk/stable/api.html#airflow.sdk.DAG "(in Apache Airflow Task SDK v1.4.0)") class from the
airflow.sdk namespace instead.

Note

The `DagRun` class is used internally by Airflow for Dag run
management. Dag authors should access Dag run information through the Task Context via
[`get_current_context()`](https://airflow.apache.org/docs/task-sdk/stable/api.html#airflow.sdk.get_current_context "(in Apache Airflow Task SDK v1.4.0)") or use the `DagRunProtocol`
interface.