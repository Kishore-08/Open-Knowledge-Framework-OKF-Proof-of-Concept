---
id: apache-airflow-triggers-9e8d674b
type: concept
title: Triggers
description: Airflow uses Triggers to implement `asyncio` compatible Deferrable Operators.
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/public-airflow-interface.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Triggers

Airflow uses Triggers to implement `asyncio` compatible Deferrable Operators.
All Triggers derive from [`BaseTrigger`](https://airflow.apache.org/docs/apache-airflow/stable/_api/airflow/triggers/base/index.html#airflow.triggers.base.BaseTrigger "airflow.triggers.base.BaseTrigger").

Airflow has a set of Triggers that are considered public. You are free to extend their functionality
by extending them:

- [airflow.triggers](https://airflow.apache.org/docs/apache-airflow/stable/_api/airflow/triggers/index.html)

You can read more about Triggers in [Deferrable Operators & Triggers](https://airflow.apache.org/docs/apache-airflow/stable/authoring-and-scheduling/deferring.html).