---
id: apache-airflow-dag-details-page-a85da58d
type: concept
title: Dag Details Page
description: Clicking a Dag from the list opens the Dag Details Page. This view offers
  centralized access to a Dag’s metadata, recent
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/ui.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Dag Details Page

Clicking a Dag from the list opens the Dag Details Page. This view offers centralized access to a Dag’s metadata, recent
activity, and task-level diagnostics.

Key elements include:

- **Dag metadata**, including ID, owner, tags, schedule, and latest Dag version
- **Action buttons** to trigger the Dag, reparse it, or pause/resume
- **Tabbed interface**: Overview (recent failures, run counts, task logs); Grid View (status heatmap); Graph View (task dependencies); Runs (full run history); Tasks (aggregated stats); Events (system- or asset-triggered); Code (Dag source); and Details (extended metadata)

This page also includes a visual **timeline of recent Dag runs** and a **log preview for failures**, helping users quickly identify issues across runs.

![Dag Details Page in dark mode showing overview dashboard and failure diagnostics](https://airflow.apache.org/docs/apache-airflow/stable/_images/dag_overview_dashboard.png)
![Dag Details Page in light mode showing overview dashboard and failure diagnostics](https://airflow.apache.org/docs/apache-airflow/stable/_images/dag_overview_dashboard1.png)