---
id: apache-airflow-task-instances-9e8d674b
type: concept
title: Task Instances
description: Task instances are the individual runs of a single task in a Dag (in
  a Dag Run). Task instances are accessed through
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/public-airflow-interface.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Task Instances

Task instances are the individual runs of a single task in a Dag (in a Dag Run). Task instances are accessed through
the Task Context via [`get_current_context()`](https://airflow.apache.org/docs/task-sdk/stable/api.html#airflow.sdk.get_current_context "(in Apache Airflow Task SDK v1.4.0)"). Direct database access is not possible.

Note

Task Context is part of the airflow.sdk namespace.
For detailed API documentation, see the [Task SDK Reference](https://airflow.apache.org/docs/task-sdk/stable/).