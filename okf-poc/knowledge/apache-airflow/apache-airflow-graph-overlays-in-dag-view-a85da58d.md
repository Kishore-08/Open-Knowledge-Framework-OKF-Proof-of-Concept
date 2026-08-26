---
id: apache-airflow-graph-overlays-in-dag-view-a85da58d
type: concept
title: Graph Overlays in Dag View
description: 'When a Dag contains asset-producing or asset-consuming tasks, you can
  enable asset overlays on the Dag Graph view. Toggle the switches next to each asset
  to:'
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/ui.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Graph Overlays in Dag View

When a Dag contains asset-producing or asset-consuming tasks, you can enable asset overlays on the Dag Graph view. Toggle the switches next to each asset to:

- See how assets flow between Dags
- Inspect asset-triggered dependencies

Two graph modes are available:

- **All Dag Dependencies**: Shows all Dag-to-Dag and task-level connections

  ![Dag Graph View - All Dependencies (dark mode)](https://airflow.apache.org/docs/apache-airflow/stable/_images/dag_graph_all_dependencies.png)
  ![Dag Graph View - All Dependencies (light mode)](https://airflow.apache.org/docs/apache-airflow/stable/_images/dag_graph_all_dependencies1.png)
- **External Conditions**: Shows only Dags triggered via asset events

  ![Dag Graph View - External Conditions Only (dark mode)](https://airflow.apache.org/docs/apache-airflow/stable/_images/dag_graph_external_conditions.png)
  ![Dag Graph View - External Conditions Only (light mode)](https://airflow.apache.org/docs/apache-airflow/stable/_images/dag_graph_external_conditions1.png)