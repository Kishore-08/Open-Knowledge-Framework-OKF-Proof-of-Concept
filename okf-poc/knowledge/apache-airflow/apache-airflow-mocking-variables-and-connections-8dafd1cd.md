---
id: apache-airflow-mocking-variables-and-connections-8dafd1cd
type: concept
title: Mocking variables and connections
description: 'When you write tests for code that uses variables or a connection, you
  must ensure that they exist when you run the tests. The obvious solution is to save
  these objects to the database so they can be '
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/best-practices.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Mocking variables and connections

When you write tests for code that uses variables or a connection, you must ensure that they exist when you run the tests. The obvious solution is to save these objects to the database so they can be read while your code is executing. However, reading and writing objects to the database are burdened with additional time overhead. In order to speed up the test execution, it is worth simulating the existence of these objects without saving them to the database. For this, you can create environment variables with mocking [`os.environ`](https://docs.python.org/3/library/os.html#os.environ "(in Python v3.14)") using `unittest.mock.patch.dict()`.

For variable, use [`AIRFLOW_VAR_{KEY}`](https://airflow.apache.org/docs/apache-airflow/stable/cli-and-env-variables-ref.html#envvar-AIRFLOW_VAR_-KEY).

```
with mock.patch.dict("os.environ", AIRFLOW_VAR_KEY="env-value"):
    assert "env-value" == Variable.get("key")
```

For connection, use [`AIRFLOW_CONN_{CONN_ID}`](https://airflow.apache.org/docs/apache-airflow/stable/cli-and-env-variables-ref.html#envvar-AIRFLOW_CONN_-CONN_ID).

```
from airflow.sdk import Connection

conn = Connection(
    conn_type="gcpssh",
    login="cat",
    host="conn-host",
)
conn_uri = conn.get_uri()
with mock.patch.dict("os.environ", AIRFLOW_CONN_MY_CONN=conn_uri):
    assert "cat" == Connection.get("my_conn").login
```