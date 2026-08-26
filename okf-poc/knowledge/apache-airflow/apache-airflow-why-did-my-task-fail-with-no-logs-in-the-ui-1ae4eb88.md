---
id: apache-airflow-why-did-my-task-fail-with-no-logs-in-the-ui-1ae4eb88
type: concept
title: Why did my task fail with no logs in the UI?
description: Logs are [typically served when a task reaches a terminal state](https://airflow.apache.org/docs/apache-airflow/stable/administration-and-deployment/logging-monitoring/logging-tasks.html#serving-worke
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/faq.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Why did my task fail with no logs in the UI?

Logs are [typically served when a task reaches a terminal state](https://airflow.apache.org/docs/apache-airflow/stable/administration-and-deployment/logging-monitoring/logging-tasks.html#serving-worker-trigger-logs). Sometimes, a task’s normal lifecycle is disrupted, and the task’s
worker is unable to write the task’s logs. This typically happens for one of two reasons:

1. [Task Instance Heartbeat Timeout](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/tasks.html#concepts-task-instance-heartbeat-timeout).
2. Tasks failed after getting stuck in queued (Airflow 2.6.0+). Tasks that are in queued for longer than [scheduler.task\_queued\_timeout](https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html#config-scheduler-task-queued-timeout) will be marked as failed, and there will be no task logs in the Airflow UI.

Setting retries for each task drastically reduces the chance that either of these problems impact a workflow.

### How do I stop the sync perms happening multiple times per webserver?

Set the value of `[fab] update_fab_perms` configuration in `airflow.cfg` to `False`.