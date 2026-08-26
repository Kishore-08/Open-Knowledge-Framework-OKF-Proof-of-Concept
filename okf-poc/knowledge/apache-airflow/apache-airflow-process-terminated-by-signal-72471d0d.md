---
id: apache-airflow-process-terminated-by-signal-72471d0d
type: concept
title: Process terminated by signal
description: Sometimes, Airflow or some adjacent system will kill a task instance’s
  `TaskRunner`, causing the task instance to fail.
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/troubleshooting.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Process terminated by signal

Sometimes, Airflow or some adjacent system will kill a task instance’s `TaskRunner`, causing the task instance to fail.

Below we discuss a few common cases.

#### Dag run timeout

A dag run timeout can be specified by `dagrun_timeout` in the dag’s definition.
The task process would likely be killed with SIGTERM (exit code -15).

#### Out of memory error (OOM)

When a task process consumes too much memory for a worker, the best case scenario is it is killed
with SIGKILL (exit code -9). Depending on configuration and infrastructure, it is also
possible that the whole worker will be killed due to OOM and then the tasks would be marked as
failed after failing to heartbeat.