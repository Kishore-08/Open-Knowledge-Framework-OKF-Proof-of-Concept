---
id: apache-airflow-special-exceptions-dda6bf43
type: concept
title: Special Exceptions
description: 'If you want to control your task’s state from within custom Task/Operator
  code, Airflow provides two special exceptions you can raise:'
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/tasks.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Special Exceptions

If you want to control your task’s state from within custom Task/Operator code, Airflow provides two special exceptions you can raise:

- `AirflowSkipException` will mark the current task as skipped
- `AirflowFailException` will mark the current task as failed *ignoring any remaining retry attempts*

These can be useful if your code has extra knowledge about its environment and wants to fail/skip faster - e.g., skipping when it knows there’s no data available, or fast-failing when it detects its API key is invalid (as that will not be fixed by a retry).