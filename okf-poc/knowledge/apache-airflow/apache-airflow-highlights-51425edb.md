---
id: apache-airflow-highlights-51425edb
type: concept
title: Highlights
description: '- **Service-Oriented Architecture**: A new Task Execution API and `airflow
  api-server` enable task execution in remote environments with improved isolation
  and flexibility (AIP-72).'
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/release_notes.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Highlights

- **Service-Oriented Architecture**: A new Task Execution API and `airflow api-server` enable task execution in remote environments with improved isolation and flexibility (AIP-72).
- **Edge Executor**: A new executor that supports distributed, event-driven, and edge-compute workflows (AIP-69), now generally available.
- **Stable Authoring Interface**: DAG authors should now use the new `airflow.sdk` namespace to import core DAG constructs like `@dag`, `@task`, and `DAG`.
- **Scheduler-Managed Backfills**: Backfills are now scheduled and tracked like regular DAG runs, with native UI and API support (AIP-78).
- **DAG Versioning**: Airflow now tracks structural changes to DAGs over time, enabling inspection of historical DAG definitions via the UI and API (AIP-66).
- **Asset-Based Scheduling**: The dataset model has been renamed and redesigned as assets, with a new `@asset` decorator and cleaner event-driven DAG definition (AIP-74, AIP-75).
- **Support for ML and AI Workflows**: DAGs can now run with `logical_date=None`, enabling use cases such as model inference, hyperparameter tuning, and non-interval workflows (AIP-83).
- **Removal of Legacy Features**: SLAs, SubDAGs, DAG and Xcom pickling, and several internal context variables have been removed. Use the upgrade tools to detect deprecated usage.
- **Split CLI and API Changes**: The CLI has been split into `airflow` and `airflowctl` (AIP-81), and REST API now defaults to `logical_date=None` when triggering a new DAG run.
- **Modern React UI**: A complete UI overhaul built on React and FastAPI includes version-aware views, backfill management, and improved DAG and task introspection (AIP-38, AIP-84).
- **Migration Tooling**: Use **ruff** and **airflow config update** to validate DAGs and configurations. Upgrade requires Airflow 2.7 or later and Python 3.9–3.12.