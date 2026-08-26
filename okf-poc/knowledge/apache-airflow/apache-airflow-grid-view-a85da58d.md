---
id: apache-airflow-grid-view-a85da58d
type: concept
title: Grid View
description: The Grid View is the primary interface for inspecting Dag runs and task
  states. It offers an interactive way to debug,
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/ui.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Grid View

The Grid View is the primary interface for inspecting Dag runs and task states. It offers an interactive way to debug,
retry, or monitor workflows over time.

Use Grid View to:

- **Understand the status of recent Dag runs** at a glance
- **Identify failed or retried tasks** by color and tooltip
- **Take action** by clicking a task cell to view logs or mark task instances as successful, failed, or cleared
- **Filter tasks** by name or partial ID
- **Select a run range**, like “last 25 runs” using the dropdown above the grid

Each row represents a task, and each column represents a Dag run. You can hover over any task instance for more detail,
or click to drill down into logs and metadata.

![Grid View showing Dag run status matrix with varied task states (Dark Mode)](https://airflow.apache.org/docs/apache-airflow/stable/_images/dag_overview_grid.png)
![Grid View showing Dag run status matrix with varied task states (Light Mode)](https://airflow.apache.org/docs/apache-airflow/stable/_images/dag_overview_grid1.png)