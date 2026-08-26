---
id: apache-airflow-home-page-a85da58d
type: concept
title: Home Page
description: The Home Page provides a high-level overview of the system state and
  recent activity. It is the default landing page in
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/ui.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Home Page

The Home Page provides a high-level overview of the system state and recent activity. It is the default landing page in
Airflow 3 and includes:

- **Health indicators** for system components such as the MetaDatabase, Scheduler, Triggerer, and Dag Processor
- **Quick links** to Dags filtered by status (e.g., Failed Dags, Running Dags, Active Dags)
- **Dag and Task Instance history**, showing counts and success/failure rates over a selectable time range
- **Recent asset events**, including materializations and triggered Dags

This page is useful for quickly assessing the health of your environment and identifying recent issues or
asset-triggered events.

![Airflow Home Page showing system health, Dag/task stats, and asset events (Dark Mode)](https://airflow.apache.org/docs/apache-airflow/stable/_images/home_dark.png)
![Airflow Home Page showing system health, Dag/task stats, and asset events (Light Mode)](https://airflow.apache.org/docs/apache-airflow/stable/_images/home_light.png)