---
id: apache-airflow-what-is-not-part-of-the-public-interface-of-apache-airflow-9e8d674b
type: concept
title: What is not part of the Public Interface of Apache Airflow?
description: Everything not mentioned in this document should be considered as non-Public
  Interface.
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/public-airflow-interface.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## What is not part of the Public Interface of Apache Airflow?

Everything not mentioned in this document should be considered as non-Public Interface.

Sometimes in other applications those components could be relied on to keep backwards compatibility,
but in Airflow they are not parts of the Public Interface and might change any time:

- [Database structure](https://airflow.apache.org/docs/apache-airflow/stable/database-erd-ref.html) is considered to be an internal implementation
  detail and you should not assume the structure is going to be maintained in a
  backwards-compatible way.
- [Web UI](https://airflow.apache.org/docs/apache-airflow/stable/ui.html) is continuously evolving and there are no backwards
  compatibility guarantees on HTML elements.
- Python classes except those explicitly mentioned in this document, are considered an
  internal implementation detail and you should not assume they will be maintained
  in a backwards-compatible way.

**Direct metadata database access from code authored by Dag Authors is no longer allowed**.
The code authored by Dag Authors cannot directly access the metadata database to query Dag state, task history,
or Dag runs — workers communicate exclusively through the Execution API. Instead, use one
of the following alternatives:

- **Task Context**: Use [`get_current_context()`](https://airflow.apache.org/docs/task-sdk/stable/api.html#airflow.sdk.get_current_context "(in Apache Airflow Task SDK v1.4.0)") to access task instance
  information and methods like `get_dr_count()`,
  `get_dagrun_state()`, and
  `get_task_states()`.
- **REST API**: Use the [Stable REST API](https://airflow.apache.org/docs/apache-airflow/stable/stable-rest-api-ref.html) for programmatic
  access to Airflow metadata.
- **Python Client**: Use the [Python Client](https://github.com/apache/airflow-client-python) for Python-based
  interactions with Airflow.

This change improves architectural separation and enables remote execution capabilities.

Example of using Task Context instead of direct database access:

```
from airflow.sdk import dag, get_current_context, task, DagRunState
from datetime import datetime


@dag(dag_id="example_dag", start_date=datetime(2025, 1, 1), schedule="@hourly", tags=["misc"], catchup=False)
def example_dag():

    @task(task_id="check_dagrun_state")
    def check_state():
        context = get_current_context()
        ti = context["ti"]
        dag_run = context["dag_run"]

        # Use Task Context methods instead of direct DB access
        dr_count = ti.get_dr_count(dag_id="example_dag")
        dagrun_state = ti.get_dagrun_state(dag_id="example_dag", run_id=dag_run.run_id)

        return f"Dag run count: {dr_count}, current state: {dagrun_state}"

    check_state()


example_dag()
```

Was this entry helpful?