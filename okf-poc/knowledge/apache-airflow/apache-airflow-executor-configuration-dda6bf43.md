---
id: apache-airflow-executor-configuration-dda6bf43
type: concept
title: Executor Configuration
description: Some [Executors](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/executor/index.html)
  allow optional per-task configuration - such as the `KubernetesExecutor`, which
  lets you set a
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/tasks.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Executor Configuration

Some [Executors](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/executor/index.html) allow optional per-task configuration - such as the `KubernetesExecutor`, which lets you set an image to run the task on.

This is achieved via the `executor_config` argument to a Task or Operator. Here’s an example of setting the Docker image for a task that will run on the `KubernetesExecutor`:

```
MyOperator(...,
    executor_config={
        "KubernetesExecutor":
            {"image": "myCustomDockerImage"}
    }
)
```

The settings you can pass into `executor_config` vary by executor, so read the [individual executor documentation](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/executor/index.html) in order to see what you can set.

Was this entry helpful?