---
id: apache-airflow-task-instance-keys-9e8d674b
type: concept
title: Task Instance Keys
description: Task instance keys are unique identifiers of task instances in a Dag
  (in a Dag Run). A key is a tuple that consists of
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/public-airflow-interface.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Task Instance Keys

Task instance keys are unique identifiers of task instances in a Dag (in a Dag Run). A key is a tuple that consists of
`dag_id`, `task_id`, `run_id`, `try_number`, and `map_index`.

Direct access to task instance keys via the `TaskInstance`
model is no longer allowed from task code. Instead, use the Task Context via [`get_current_context()`](https://airflow.apache.org/docs/task-sdk/stable/api.html#airflow.sdk.get_current_context "(in Apache Airflow Task SDK v1.4.0)")
to access task instance information.

Example of accessing task instance information through Task Context:

```
from airflow.sdk import get_current_context


def my_task():
    context = get_current_context()
    ti = context["ti"]

    dag_id = ti.dag_id
    task_id = ti.task_id
    run_id = ti.run_id
    try_number = ti.try_number
    map_index = ti.map_index

    print(f"Task: {dag_id}.{task_id}, Run: {run_id}, Try: {try_number}, Map Index: {map_index}")
```

Note

The `TaskInstanceKey` class is used internally by Airflow
for identifying task instances. Dag authors should access task instance information through the
Task Context via [`get_current_context()`](https://airflow.apache.org/docs/task-sdk/stable/api.html#airflow.sdk.get_current_context "(in Apache Airflow Task SDK v1.4.0)") instead.