---
id: apache-airflow-logs-a85da58d
type: concept
title: Logs
description: The default tab shows the task logs, which include system output, error
  messages, and traceback information. This is the first place to look when a task
  fails.
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/ui.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Logs

The default tab shows the task logs, which include system output, error messages, and traceback information. This is the first place to look when a task fails.

![Task Logs (light mode)](https://airflow.apache.org/docs/apache-airflow/stable/_images/dag_task_instance_logs1.png)

### Rendered Templates

Displays the rendered version of templated fields in your task. Useful for debugging context variables or verifying
dynamic content.