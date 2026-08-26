---
id: apache-airflow-task-instances-dda6bf43
type: concept
title: Task Instances
description: Much in the same way that a Dag is instantiated into a [Dag Run](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/dags.html#concepts-dag-run)
  each time it runs, the tasks under a Da
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/tasks.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Task Instances

Much in the same way that a Dag is instantiated into a [Dag Run](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/dags.html#concepts-dag-run) each time it runs, the tasks under a Dag are instantiated into *Task Instances*.

An instance of a Task is a specific run of that task for a given Dag (and thus for a given data interval). They are also the representation of a Task that has *state*, representing what stage of the lifecycle it is in.

The possible states for a Task Instance are:

- `none`: The Task has not yet been queued for execution (its dependencies are not yet met)
- `scheduled`: The scheduler has determined the Task’s dependencies are met and it should run
- `queued`: The task has been assigned to an Executor and is awaiting a worker
- `running`: The task is running on a worker (or on a local/synchronous executor)
- `success`: The task finished running without errors
- `restarting`: The task was externally requested to restart when it was running
- `failed`: The task had an error during execution and failed to run
- `skipped`: The task was skipped due to branching, LatestOnly, or similar.
- `upstream_failed`: An upstream task failed and the [Trigger Rule](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/dags.html#concepts-trigger-rules) says we needed it
- `up_for_retry`: The task failed, but has retry attempts left and will be rescheduled.
- `up_for_reschedule`: The task is a [Sensor](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/sensors.html) that is in `reschedule` mode
- `deferred`: The task has been [deferred to a trigger](https://airflow.apache.org/docs/apache-airflow/stable/authoring-and-scheduling/deferring.html)
- `awaiting_input`: The task is a [Human-in-the-loop](https://airflow.apache.org/docs/apache-airflow/stable/tutorial/hitl.html) task waiting for a human response. It is managed by the scheduler and uses neither a worker slot nor the triggerer.
- `removed`: The task has vanished from the Dag since the run started

![../_images/diagram_task_lifecycle.png](https://airflow.apache.org/docs/apache-airflow/stable/_images/diagram_task_lifecycle.png)

Ideally, a task should flow from `none`, to `scheduled`, to `queued`, to `running`, and finally to `success`.

When any custom Task (Operator) is running, it will get a copy of the task instance passed to it; as well as being able to inspect task metadata, it also contains methods for things like [XComs](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/xcoms.html).