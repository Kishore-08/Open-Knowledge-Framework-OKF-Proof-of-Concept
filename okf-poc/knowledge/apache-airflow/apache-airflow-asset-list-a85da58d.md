---
id: apache-airflow-asset-list-a85da58d
type: concept
title: Asset List
description: 'The Asset List shows all known assets, grouped by name. For each asset,
  you can see:'
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/ui.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Asset List

The Asset List shows all known assets, grouped by name. For each asset, you can see:

- The group the asset belongs to (if any)
- The Dags that consume the asset
- The tasks that produce the asset

Hovering over a count of Dags or tasks shows a tooltip with the full list of producers or consumers.

![Asset Graph View (dark mode)](https://airflow.apache.org/docs/apache-airflow/stable/_images/asset_list_consuming_dags.png)
![Asset Graph View (light mode)](https://airflow.apache.org/docs/apache-airflow/stable/_images/asset_list_consuming_dags1.png)

Clicking on the link takes you to the Asset Graph View.