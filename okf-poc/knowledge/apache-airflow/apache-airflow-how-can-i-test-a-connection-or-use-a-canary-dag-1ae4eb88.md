---
id: apache-airflow-how-can-i-test-a-connection-or-use-a-canary-dag-1ae4eb88
type: concept
title: How can I test a connection or use a Canary Dag?
description: For security reasons, the test connection functionality is disabled by
  default across the Airflow UI,
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/faq.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### How can I test a connection or use a Canary Dag?

For security reasons, the test connection functionality is disabled by default across the Airflow UI,
API and CLI. This can be modified by setting ref:config:core\_\_test\_connection.

You can utilize a Dag to regularly test connections. This is referred to as a “Canary Dag” and can detect and
alert on failures in external systems that your Dags depend on. You can create a simple Dag that tests connections
such as the following Airflow 3 example:

```
from airflow import DAG
from airflow.sdk import task

with DAG(dag_id="canary", schedule="@daily", doc_md="Canary Dag to regularly test connections to systems."):

    @task(doc_md="Test a connection by its Connection ID.")
    def test_connection(conn_id):
        from airflow.hooks.base import BaseHook

        ok, status = BaseHook.get_hook(conn_id=conn_id).test_connection()
        if ok:
            return status
        raise RuntimeError(status)

    for conn_id in [
        # Add more connections here to create tasks to test them.
        "aws_default",
    ]:
        test_connection.override(task_id="test_" + conn_id)(conn_id)
```

Was this entry helpful?