---
id: apache-airflow-group-extras-f586a1ea
type: concept
title: Group extras
description: The group extras are convenience extras. Such extra installs many optional
  dependencies together.
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/extra-packages-ref.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Group extras

The group extras are convenience extras. Such extra installs many optional dependencies together.
It is not recommended to use it in production, but it is useful for CI, development and testing purposes.

| extra | install command | enables |
| --- | --- | --- |
| all | `pip install apache-airflow[all]` | All optional dependencies including all providers |
| all-core | `pip install apache-airflow[all-core]` | All optional core dependencies |
| all-task-sdk | `pip install apache-airflow[all-task-sdk]` | All optional task SDK dependencies |

Was this entry helpful?