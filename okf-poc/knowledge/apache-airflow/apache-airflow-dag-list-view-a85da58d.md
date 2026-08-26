---
id: apache-airflow-dag-list-view-a85da58d
type: concept
title: Dag List View
description: The Dag List View appears when you click the **Dags** tab in the main
  navigation bar. It displays all Dags available in
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/ui.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Dag List View

The Dag List View appears when you click the **Dags** tab in the main navigation bar. It displays all Dags available in
your environment, with a clear summary of their status, recent runs, and configuration.

Each row includes:

- **Dag ID**
- **Schedule** and next run time
- **Status of the latest Dag run**
- **Bar chart of recent runs**
- **Tags**, which can be used for grouping or filtering Dags (e.g., `example`, `produces`)
- **Pause/resume toggle**
- Links to access Dag-level views

At the top of the view, you can:

- Use **filters** for Dag status, schedule state, and tags
- Use **search** or **advanced search (⌘+K)** to find specific Dags
- Sort the list using the dropdown (e.g., Latest Run Start Date)

![Dag List View in dark mode showing search, filters, and Dag-level controls](https://airflow.apache.org/docs/apache-airflow/stable/_images/dag_list.png)
![Dag List View in light mode showing the same Dags and actions for comparison](https://airflow.apache.org/docs/apache-airflow/stable/_images/dag_list1.png)

Some Dags in this list may interact with data assets. For example, Dags that are triggered by asset conditions may
display popups showing upstream asset inputs.

![Dag List View showing asset condition popup (Dark Mode)](https://airflow.apache.org/docs/apache-airflow/stable/_images/dag_list_asset_condition_popup.png)
![Dag List View showing asset condition popup (Light Mode)](https://airflow.apache.org/docs/apache-airflow/stable/_images/dag_list_asset_condition_popup1.png)