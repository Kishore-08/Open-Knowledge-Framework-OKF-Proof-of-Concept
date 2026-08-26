---
id: apache-airflow-using-the-public-interface-for-dag-authors-9e8d674b
type: concept
title: Using the Public Interface for Dag authors
description: The primary interface for Dag authors is the `airflow.sdk` namespace.
  See the [Task SDK Reference](https://airflow.apache.org/docs/task-sdk/stable/) for
  comprehensive documentation.
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/public-airflow-interface.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Using the Public Interface for Dag authors

The primary interface for Dag authors is the `airflow.sdk` namespace. See the [Task SDK Reference](https://airflow.apache.org/docs/task-sdk/stable/) for comprehensive documentation.
This provides a stable, well-defined interface for creating Dags and tasks that is not subject to internal
implementation changes. The goal of this change is to decouple Dag authoring from Airflow internals (Scheduler,
API Server, etc.), providing a version-agnostic, stable interface for writing and maintaining Dags across Airflow versions.

**Key Imports from airflow.sdk:**

**Classes:**

- [`airflow.sdk.Asset`](https://airflow.apache.org/docs/task-sdk/stable/api.html#airflow.sdk.Asset "(in Apache Airflow Task SDK v1.4.0)")
- [`airflow.sdk.BaseHook`](https://airflow.apache.org/docs/task-sdk/stable/api.html#airflow.sdk.BaseHook "(in Apache Airflow Task SDK v1.4.0)")
- [`airflow.sdk.BaseNotifier`](https://airflow.apache.org/docs/task-sdk/stable/api.html#airflow.sdk.BaseNotifier "(in Apache Airflow Task SDK v1.4.0)")
- [`airflow.sdk.BaseOperator`](https://airflow.apache.org/docs/task-sdk/stable/api.html#airflow.sdk.BaseOperator "(in Apache Airflow Task SDK v1.4.0)")
- [`airflow.sdk.BaseOperatorLink`](https://airflow.apache.org/docs/task-sdk/stable/api.html#airflow.sdk.BaseOperatorLink "(in Apache Airflow Task SDK v1.4.0)")
- [`airflow.sdk.BaseSensorOperator`](https://airflow.apache.org/docs/task-sdk/stable/api.html#airflow.sdk.BaseSensorOperator "(in Apache Airflow Task SDK v1.4.0)")
- [`airflow.sdk.Connection`](https://airflow.apache.org/docs/task-sdk/stable/api.html#airflow.sdk.Connection "(in Apache Airflow Task SDK v1.4.0)")
- [`airflow.sdk.Context`](https://airflow.apache.org/docs/task-sdk/stable/api.html#airflow.sdk.Context "(in Apache Airflow Task SDK v1.4.0)")
- [`airflow.sdk.DAG`](https://airflow.apache.org/docs/task-sdk/stable/api.html#airflow.sdk.DAG "(in Apache Airflow Task SDK v1.4.0)")
- [`airflow.sdk.EdgeModifier`](https://airflow.apache.org/docs/task-sdk/stable/api.html#airflow.sdk.EdgeModifier "(in Apache Airflow Task SDK v1.4.0)")
- [`airflow.sdk.Label`](https://airflow.apache.org/docs/task-sdk/stable/api.html#airflow.sdk.Label "(in Apache Airflow Task SDK v1.4.0)")
- [`airflow.sdk.ObjectStoragePath`](https://airflow.apache.org/docs/task-sdk/stable/api.html#airflow.sdk.ObjectStoragePath "(in Apache Airflow Task SDK v1.4.0)")
- [`airflow.sdk.Param`](https://airflow.apache.org/docs/task-sdk/stable/api.html#airflow.sdk.Param "(in Apache Airflow Task SDK v1.4.0)")
- [`airflow.sdk.TaskGroup`](https://airflow.apache.org/docs/task-sdk/stable/api.html#airflow.sdk.TaskGroup "(in Apache Airflow Task SDK v1.4.0)")
- [`airflow.sdk.Variable`](https://airflow.apache.org/docs/task-sdk/stable/api.html#airflow.sdk.Variable "(in Apache Airflow Task SDK v1.4.0)")

**Decorators and Functions:**

- [`airflow.sdk.asset()`](https://airflow.apache.org/docs/task-sdk/stable/api.html#airflow.sdk.asset "(in Apache Airflow Task SDK v1.4.0)")
- [`airflow.sdk.dag()`](https://airflow.apache.org/docs/task-sdk/stable/api.html#airflow.sdk.dag "(in Apache Airflow Task SDK v1.4.0)")
- [`airflow.sdk.task()`](https://airflow.apache.org/docs/task-sdk/stable/api.html#airflow.sdk.task "(in Apache Airflow Task SDK v1.4.0)")
- [`airflow.sdk.task_group()`](https://airflow.apache.org/docs/task-sdk/stable/api.html#airflow.sdk.task_group "(in Apache Airflow Task SDK v1.4.0)")
- [`airflow.sdk.setup()`](https://airflow.apache.org/docs/task-sdk/stable/api.html#airflow.sdk.setup "(in Apache Airflow Task SDK v1.4.0)")
- [`airflow.sdk.teardown()`](https://airflow.apache.org/docs/task-sdk/stable/api.html#airflow.sdk.teardown "(in Apache Airflow Task SDK v1.4.0)")
- [`airflow.sdk.result()`](https://airflow.apache.org/docs/task-sdk/stable/api.html#airflow.sdk.result "(in Apache Airflow Task SDK v1.4.0)")
- [`airflow.sdk.chain()`](https://airflow.apache.org/docs/task-sdk/stable/api.html#airflow.sdk.chain "(in Apache Airflow Task SDK v1.4.0)")