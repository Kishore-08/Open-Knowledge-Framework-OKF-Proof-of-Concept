---
id: apache-airflow-navigate-7aae3951
type: concept
title: '`↑↓` Navigate'
description: '`↑↓` Navigate'
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/templates-ref.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

`↑↓` Navigate
`⏎` Select
`Esc` Close



# Templates reference

Variables, macros and filters can be used in templates (see the [Jinja Templating](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/operators.html#concepts-jinja-templating) section)
Asset-triggered DAGs
——————–

Asset-triggered Dags in Apache Airflow 3 differ from time-based Dags in the
template context they provide.

Asset-triggered Dags do not have a logical date, and therefore do not provide
time-based context variables such as `logical_date`, `ds`, `ds_nodash`,
or values derived from them.

For asset-triggered Dags, information related to the triggering run can be
accessed via `dag_run`. For example, `dag_run.run_id` can be used to
uniquely identify a Dag run triggered by an asset event.

Added in version 3.0.0.

The variables listed on this page are provided via Airflow’s execution-time context.

When using the Task SDK, the same execution-time context is also available programmatically via the [`airflow.sdk.Context`](https://airflow.apache.org/docs/task-sdk/stable/api.html#airflow.sdk.Context "(in Apache Airflow Task SDK v1.4.0)") object.

The following come for free out of the box with Airflow.
Additional custom macros can be added globally through [Plugins](https://airflow.apache.org/docs/apache-airflow/stable/administration-and-deployment/plugins.html), or at a Dag level through the
`DAG.user_defined_macros` argument.