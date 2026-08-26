---
id: apache-airflow-example-of-watcher-pattern-with-trigger-rules-8dafd1cd
type: concept
title: Example of watcher pattern with trigger rules
description: The watcher pattern is how we call a Dag with a task that is “watching”
  the states of the other tasks.
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/best-practices.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Example of watcher pattern with trigger rules

The watcher pattern is how we call a Dag with a task that is “watching” the states of the other tasks.
Its primary purpose is to fail a Dag Run when any other task fail.
The need came from the Airflow system tests that are Dags with different tasks (similarly like a test containing steps).

Normally, when any task fails, all other tasks are not executed and the whole Dag Run gets failed status too. But
when we use trigger rules, we can disrupt the normal flow of running tasks and the whole Dag may represent different
status that we expect. For example, we can have a teardown task (with trigger rule set to `TriggerRule.ALL_DONE`)
that will be executed regardless of the state of the other tasks (e.g. to clean up the resources). In such
situation, the Dag would always run this task and the Dag Run will get the status of this particular task, so we can
potentially lose the information about failing tasks. If we want to ensure that the Dag with teardown task would fail
if any task fails, we need to use the watcher pattern. The watcher task is a task that will always fail if
triggered, but it needs to be triggered only if any other task fails. It needs to have a trigger rule set to
`TriggerRule.ONE_FAILED` and it needs also to be a downstream task for all other tasks in the Dag. Thanks to
this, if every other task will pass, the watcher will be skipped, but when something fails, the watcher task will be
executed and fail making the Dag Run fail too.

Note

Be aware that trigger rules only rely on the direct upstream (parent) tasks, e.g. `TriggerRule.ONE_FAILED`
will ignore any failed (or `upstream_failed`) tasks that are not a direct parent of the parameterized task.

It’s easier to grab the concept with an example. Let’s say that we have the following Dag:

```
from datetime import datetime

from airflow.sdk import DAG
from airflow.sdk import task
from airflow.exceptions import AirflowException
from airflow.providers.standard.operators.bash import BashOperator
from airflow.utils.trigger_rule import TriggerRule


@task(trigger_rule=TriggerRule.ONE_FAILED, retries=0)
def watcher():
    raise AirflowException("Failing task because one or more upstream tasks failed.")


with DAG(
    dag_id="watcher_example",
    schedule="@once",
    start_date=datetime(2021, 1, 1),
    catchup=False,
) as dag:
    failing_task = BashOperator(task_id="failing_task", bash_command="exit 1", retries=0)
    passing_task = BashOperator(task_id="passing_task", bash_command="echo passing_task")
    teardown = BashOperator(
        task_id="teardown",
        bash_command="echo teardown",
        trigger_rule=TriggerRule.ALL_DONE,
    )

    failing_task >> passing_task >> teardown
    list(dag.tasks) >> watcher()
```

The visual representation of this Dag after execution looks like this:

![_images/watcher.png](https://airflow.apache.org/docs/apache-airflow/stable/_images/watcher.png)

We have several tasks that serve different purposes:

- `failing_task` always fails,
- `passing_task` always succeeds (if executed),
- `teardown` is always triggered (regardless the states of the other tasks) and it should always succeed,
- `watcher` is a downstream task for each other task, i.e. it will be triggered when any task fails and thus fail the whole Dag Run, since it’s a leaf task.

It’s important to note, that without `watcher` task, the whole Dag Run will get the `success` state, since the only failing task is not the leaf task, and the `teardown` task will finish with `success`.
If we want the `watcher` to monitor the state of all tasks, we need to make it dependent on all of them separately. Thanks to this, we can fail the Dag Run if any of the tasks fail. Note that the watcher task has a trigger rule set to `"one_failed"`.
On the other hand, without the `teardown` task, the `watcher` task will not be needed, because `failing_task` will propagate its `failed` state to downstream task `passed_task` and the whole