---
id: apache-airflow-how-to-trigger-tasks-based-on-another-task-s-failure-1ae4eb88
type: concept
title: How to trigger tasks based on another task’s failure?
description: For tasks that are related through dependency, you can set the `trigger_rule`
  to `TriggerRule.ALL_FAILED` if the
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/faq.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### How to trigger tasks based on another task’s failure?

For tasks that are related through dependency, you can set the `trigger_rule` to `TriggerRule.ALL_FAILED` if the
task execution depends on the failure of ALL its upstream tasks or `TriggerRule.ONE_FAILED` for just one of the
upstream task.

```
import pendulum

from airflow.sdk import dag, task
from airflow.exceptions import AirflowException
from airflow.utils.trigger_rule import TriggerRule


@task()
def a_func():
    raise AirflowException


@task(
    trigger_rule=TriggerRule.ALL_FAILED,
)
def b_func():
    pass


@dag(schedule="@once", start_date=pendulum.datetime(2021, 1, 1, tz="UTC"))
def my_dag():
    a = a_func()
    b = b_func()

    a >> b


dag = my_dag()
```

See [Trigger Rules](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/dags.html#concepts-trigger-rules) for more information.

If the tasks are not related by dependency, you will need to [build a custom Operator](https://airflow.apache.org/docs/apache-airflow/stable/howto/custom-operator.html#custom-operator).

## Airflow UI