---
id: apache-airflow-hooks-9e8d674b
type: concept
title: Hooks
description: Hooks are interfaces to external platforms and databases, implementing
  a common
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/public-airflow-interface.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Hooks

Hooks are interfaces to external platforms and databases, implementing a common
interface when possible and acting as building blocks for operators. All hooks
are derived from `BaseHook`.

Airflow has a set of Hooks that are considered public. You are free to extend their functionality
by extending them:

- [airflow.hooks](https://airflow.apache.org/docs/apache-airflow/stable/_api/airflow/hooks/index.html)