---
id: apache-airflow-navigate-9acbc545
type: concept
title: '`↑↓` Navigate'
description: '`↑↓` Navigate'
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/index.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

`↑↓` Navigate
`⏎` Select
`Esc` Close



# What is Airflow®?

[Apache Airflow®](https://github.com/apache/airflow) is an open-source platform for developing, scheduling,
and monitoring workflows, such as traditional time based or event-triggered batch-oriented data pipelines, machine learning, model training,
and agentic or LLM-based workloads. Airflow’s extensible Python framework enables you to build workflows
connecting with virtually any technology, with a growing set of providers for orchestrating AI and agentic
tools alongside the rest of your pipeline. A web-based UI helps you visualize, manage, and debug your workflows.
You can run Airflow in a variety of configurations — from a single process on your laptop to a distributed system
capable of handling massive workloads.

# Workflows as code

Airflow workflows are defined entirely in Python. This “workflows as code” approach brings several advantages:

- **Dynamic**: Pipelines are defined in code, enabling dynamic Dag generation and parameterization.
- **Extensible**: The Airflow framework includes a wide range of built-in operators and can be extended to fit your needs.
- **Flexible**: Airflow leverages the [Jinja](https://jinja.palletsprojects.com) templating engine, allowing rich customizations.

# Task SDK

For Airflow Task SDK, see the standalone reference & tutorial site:

[Apache Airflow Task SDK](https://airflow.apache.org/docs/task-sdk/stable/index.html "(in Apache Airflow Task SDK v1.4.0)")