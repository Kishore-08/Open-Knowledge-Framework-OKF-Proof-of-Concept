---
id: apache-airflow-creating-a-task-8dafd1cd
type: concept
title: Creating a task
description: You should treat tasks in Airflow equivalent to transactions in a database.
  This
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/best-practices.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Creating a task

You should treat tasks in Airflow equivalent to transactions in a database. This
implies that you should never produce incomplete results from your tasks. An
example is not to produce incomplete data in `HDFS` or `S3` at the end of a
task.

Airflow can retry a task if it fails. Thus, the tasks should produce the same
outcome on every re-run. Some of the ways you can avoid producing a different
result -

- Do not use INSERT during a task re-run, an INSERT statement might lead to
  duplicate rows in your database. Replace it with UPSERT.
- Read and write in a specific partition. Never read the latest available data
  in a task. Someone may update the input data between re-runs, which results in
  different outputs. A better way is to read the input data from a specific
  partition. You can use `data_interval_start` as a partition. You should
  follow this partitioning method while writing data in S3/HDFS as well.
- The Python datetime `now()` function gives the current datetime object. This
  function should never be used inside a task, especially to do the critical
  computation, as it leads to different outcomes on each run. It’s fine to use
  it, for example, to generate a temporary log.

Tip

You should define repetitive parameters such as `connection_id` or S3 paths in `default_args` rather than declaring them for each task.
The `default_args` help to avoid mistakes such as typographical errors. Also, most connection types have unique parameter names in
tasks, so you can declare a connection only once in `default_args` (for example `gcp_conn_id`) and it is automatically
used by all operators that use this connection type.