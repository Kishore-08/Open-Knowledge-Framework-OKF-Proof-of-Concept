---
id: apache-airflow-navigate-9e8d674b
type: concept
title: '`↑↓` Navigate'
description: '`↑↓` Navigate'
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/public-airflow-interface.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

`↑↓` Navigate
`⏎` Select
`Esc` Close

# Public Interface for Airflow 3.0+

Warning

This documentation covers the Public Interface for Airflow 3.0+

If you are using Airflow 2.x, please refer to the
[Airflow 2.11 Public Interface Documentation](https://airflow.apache.org/docs/apache-airflow/2.11.0/public-airflow-interface.html)
for the legacy interface.

The Public Interface of Apache Airflow is the collection of interfaces and behaviors in Apache Airflow
whose changes are governed by semantic versioning. A user interacts with Airflow’s public interface
by creating and managing Dags, managing tasks and dependencies,
and extending Airflow capabilities by writing new executors, plugins, operators and providers. The
Public Interface can be useful for building custom tools and integrations with other systems,
and for automating certain aspects of the Airflow workflow.

The primary public interface for Dag authors and task execution is using task SDK
Airflow task SDK is the primary public interface for Dag authors and for task execution
[airflow.sdk namespace](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/taskflow.html). Direct access to the metadata database
from task code is no longer allowed. Instead, use the [Stable REST API](https://airflow.apache.org/docs/apache-airflow/stable/stable-rest-api-ref.html),
[Python Client](https://github.com/apache/airflow-client-python), or Task Context methods.

For comprehensive Task SDK documentation, see the [Task SDK Reference](https://airflow.apache.org/docs/task-sdk/stable/).