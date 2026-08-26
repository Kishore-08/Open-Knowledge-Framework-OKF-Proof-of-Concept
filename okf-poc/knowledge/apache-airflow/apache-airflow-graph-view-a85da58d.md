---
id: apache-airflow-graph-view-a85da58d
type: concept
title: Graph View
description: Shows the Dag’s task dependency structure overlaid with the status of
  each task in this specific run. This is useful for visual debugging of task failure
  paths or identifying downstream blockers.
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/ui.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Graph View

Shows the Dag’s task dependency structure overlaid with the status of each task in this specific run. This is useful for visual debugging of task failure paths or identifying downstream blockers.

Each node includes a visual indicator of task duration.

![Dag Run - Graph View (dark mode)](https://airflow.apache.org/docs/apache-airflow/stable/_images/dag_run_graph.png)
![Dag Run - Graph View (light mode)](https://airflow.apache.org/docs/apache-airflow/stable/_images/dag_run_graph1.png)

## Dag Trigger Window