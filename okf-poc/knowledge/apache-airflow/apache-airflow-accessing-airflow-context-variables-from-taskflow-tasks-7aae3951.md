---
id: apache-airflow-accessing-airflow-context-variables-from-taskflow-tasks-7aae3951
type: concept
title: Accessing Airflow context variables from TaskFlow tasks
description: While `@task` decorated tasks don’t support rendering jinja templates
  passed as arguments,
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/templates-ref.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Accessing Airflow context variables from TaskFlow tasks

While `@task` decorated tasks don’t support rendering jinja templates passed as arguments,
all of the variables listed above can be accessed directly from tasks. The following code block
is an example of accessing a `task_instance` object from its task:

> ```
> from airflow.sdk import TaskInstance
> from airflow.sdk.types import DagRunProtocol
>
>
> @task
> def print_ti_info(task_instance: TaskInstance, dag_run: DagRunProtocol):
>     print(f"Run ID: {task_instance.run_id}")  # Run ID: scheduled__2023-08-09T00:00:00+00:00
>     print(f"Task start date: {task_instance.start_date}")  # 2023-08-10 00:00:01+00:00
>     print(f"Dag Run logical date: {dag_run.logical_date}")  # 2023-08-09 00:00:00+00:00
> ```

Note that you can access the object’s attributes and methods with simple
dot notation. Here are some examples of what is possible:
`{{ task.owner }}`, `{{ task.task_id }}`, `{{ ti.hostname }}`, …
Refer to the models documentation for more information on the objects’
attributes and methods.