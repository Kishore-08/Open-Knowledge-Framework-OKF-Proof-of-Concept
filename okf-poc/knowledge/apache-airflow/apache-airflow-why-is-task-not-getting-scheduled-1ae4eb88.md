---
id: apache-airflow-why-is-task-not-getting-scheduled-1ae4eb88
type: concept
title: Why is task not getting scheduled?
description: 'There are very many reasons why your task might not be getting scheduled.
  Here are some of the common causes:'
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/faq.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Why is task not getting scheduled?

There are very many reasons why your task might not be getting scheduled. Here are some of the common causes:

- Does your script “compile”, can the Airflow engine parse it and find your
  Dag object? To test this, you can run `airflow dags list` and
  confirm that your Dag shows up in the list. You can also run
  `airflow dags show foo_dag_id` and confirm that your task
  shows up in the graphviz format as expected. If you use the CeleryExecutor, you
  may want to confirm that this works both where the scheduler runs as well
  as where the worker runs.
- Does the file containing your Dag contain the string `airflow` and `DAG` somewhere
  in the contents? When searching the Dag directory, Airflow ignores files not containing
  `airflow` and `DAG` in order to prevent the DagBag parsing from importing all python
  files collocated with user’s Dags.
- Is your `start_date` set properly? For time-based Dags, the task won’t be triggered until the
  the first schedule interval following the start date has passed.
- Is your `schedule` argument set properly? The default
  is one day (`datetime.timedelta(1)`). You must specify a different `schedule`
  directly to the Dag object you instantiate, not as a `default_param`, as task instances
  do not override their parent Dag’s `schedule`.
- Is your `start_date` beyond where you can see it in the UI? If you
  set your `start_date` to some time say 3 months ago, you won’t be able to see
  it in the main view in the UI, but you should be able to see it in the
  `Menu -> Browse ->Task Instances`.
- Are the dependencies for the task met? The task instances directly
  upstream from the task need to be in a `success` state. Also,
  if you have set `depends_on_past=True`, the previous task instance
  needs to have succeeded or been skipped (except if it is the first run for that task).
  Also, if `wait_for_downstream=True`, make sure you understand
  what it means - all tasks *immediately* downstream of the *previous*
  task instance must have succeeded or been skipped.
  You can view how these properties are set from the `Task Instance Details`
  page for your task.
- Are the DagRuns you need created and active? A DagRun represents a specific
  execution of an entire Dag and has a state (running, success, failed, …).
  The scheduler creates new DagRun as it moves forward, but never goes back
  in time to create new ones. The scheduler only evaluates `running` DagRuns
  to see what task instances it can trigger. Note that clearing tasks
  instances (from the UI or CLI) does set the state of a DagRun back to
  running. You can bulk view the list of DagRuns and alter states by clicking
  on the schedule tag for a Dag.
- Is the `concurrency` parameter of your Dag reached? `concurrency` defines
  how many `running` task instances a Dag is allowed to have, beyond which
  point things get queued.
- Is the `max_active_runs` parameter of your Dag reached? `max_active_runs` defines
  how many `running` concurrent instances of a Dag there are allowed to be.

You may also want to read about the [Scheduler](https://airflow.apache.org/docs/apache-airflow/stable/administration-and-deployment/scheduler.html#scheduler) and make
sure you fully understand how the scheduler cycle.