---
id: apache-airflow-dag-run-view-a85da58d
type: concept
title: Dag Run View
description: Each Dag Run has its own view, accessible by selecting a specific row
  in the Dag’s **Runs** tab. The Dag Run view
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/ui.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Dag Run View

Each Dag Run has its own view, accessible by selecting a specific row in the Dag’s **Runs** tab. The Dag Run view
displays metadata about the selected run, as well as task-level details, rendered code, and more.

![Dag Run - Task Instances tab (dark mode)](https://airflow.apache.org/docs/apache-airflow/stable/_images/dag_run_task_instances.png)

Key elements include:

- **Dag Run metadata**, including logical date, run type, duration, Dag version, and parsed time
- **Action buttons** to clear or mark the run, or add a note
- A persistent **Grid View sidebar**, which shows task durations and states across recent Dag runs. This helps spot recurring issues or performance trends at a glance.

## Dag Run Tabs