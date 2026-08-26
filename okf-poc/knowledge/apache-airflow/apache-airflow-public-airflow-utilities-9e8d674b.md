---
id: apache-airflow-public-airflow-utilities-9e8d674b
type: concept
title: Public Airflow utilities
description: When writing or extending Hooks and Operators, Dag authors and developers
  can
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/public-airflow-interface.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Public Airflow utilities

When writing or extending Hooks and Operators, Dag authors and developers can
use the following classes:

- The [`Connection`](https://airflow.apache.org/docs/task-sdk/stable/api.html#airflow.sdk.Connection "(in Apache Airflow Task SDK v1.4.0)"), which provides access to external service credentials and configuration.
- The [`Variable`](https://airflow.apache.org/docs/task-sdk/stable/api.html#airflow.sdk.Variable "(in Apache Airflow Task SDK v1.4.0)"), which provides access to Airflow configuration variables.
- The `XCom` which are used to access to inter-task communication data.

Connection and Variable operations should be performed through the Task Context using
[`get_current_context()`](https://airflow.apache.org/docs/task-sdk/stable/api.html#airflow.sdk.get_current_context "(in Apache Airflow Task SDK v1.4.0)") and the task instance’s methods, or through the airflow.sdk namespace.
Direct database access to `Connection` and `Variable`
models is no longer allowed from task code.

Example of accessing Connections and Variables through Task Context:

```
from airflow.sdk import get_current_context


def my_task():
    context = get_current_context()

    conn = context["conn"]
    my_connection = conn.get("my_connection_id")

    var = context["var"]
    my_variable = var.value.get("my_variable_name")
```

Example of using airflow.sdk namespace directly:

```
from airflow.sdk import Connection, Variable

conn = Connection.get("my_connection_id")
var = Variable.get("my_variable_name")
```

You can read more about the public Airflow utilities in [Managing Connections](https://airflow.apache.org/docs/apache-airflow/stable/howto/connection.html),
[Variables](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/variables.html), [XComs](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/xcoms.html)

Reference for classes used for the utilities are here:

Note

Connection, Variable, and XCom classes are now part of the airflow.sdk namespace.
For detailed API documentation, see the [Task SDK Reference](https://airflow.apache.org/docs/task-sdk/stable/).