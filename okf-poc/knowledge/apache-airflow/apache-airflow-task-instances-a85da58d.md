---
id: apache-airflow-task-instances-a85da58d
type: concept
title: Task Instances
description: 'Displays the status and metadata for each task instance within the Dag
  Run. Columns include:'
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/ui.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Task Instances

Displays the status and metadata for each task instance within the Dag Run. Columns include:

- Task ID
- State
- Start and End Dates
- Try Number
- Operator Type
- Duration
- Dag Version

Each row also includes a mini Gantt-style timeline that visually represents the task’s duration.

![Dag Run - Task Instances (light mode)](https://airflow.apache.org/docs/apache-airflow/stable/_images/dag_run_task_instances1.png)

### Events

If available, this tab lists system-level or asset-triggered events that contributed to this Dag Run’s execution.