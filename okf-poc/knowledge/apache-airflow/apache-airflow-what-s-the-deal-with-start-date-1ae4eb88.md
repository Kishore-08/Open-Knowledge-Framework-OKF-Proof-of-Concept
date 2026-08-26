---
id: apache-airflow-what-s-the-deal-with-start-date-1ae4eb88
type: concept
title: What’s the deal with `start_date`?
description: '`start_date` is partly legacy from the pre-DagRun era, but it is still'
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/faq.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### What’s the deal with `start_date`?

`start_date` is partly legacy from the pre-DagRun era, but it is still
relevant in many ways. When creating a new Dag, you probably want to set
a global `start_date` for your tasks. This can be done by declaring your
`start_date` directly in the `DAG()` object. A Dag’s first
DagRun will be created based on the first complete `data_interval`
after `start_date`. For example, for a Dag with
`start_date=datetime(2024, 1, 1)` and `schedule="0 0 3 * *"`, the
first Dag run will be triggered at midnight on 2024-02-03 with
`data_interval_start=datetime(2024, 1, 3)` and
`data_interval_end=datetime(2024, 2, 3)`. From that point on, the scheduler
creates new DagRuns based on your `schedule` and the corresponding task
instances run as your dependencies are met. When introducing new tasks to
your Dag, you need to pay special attention to `start_date`, and may want
to reactivate inactive DagRuns to get the new task onboarded properly.

We recommend against using dynamic values as `start_date`, especially
`datetime.now()` as it can be quite confusing. The task is triggered
once the period closes, and in theory an `@hourly` Dag would never get to
an hour after now as `now()` moves along.

Previously, we also recommended using rounded `start_date` in relation to your
Dag’s `schedule`. This meant an `@hourly` would be at `00:00`
minutes:seconds, a `@daily` job at midnight, a `@monthly` job on the
first of the month. This is no longer required. Airflow will now auto align
the `start_date` and the `schedule`, by using the `start_date`
as the moment to start looking.

You can use any sensor or a `TimeDeltaSensor` to delay
the execution of tasks within the schedule interval.
While `schedule` does allow specifying a `datetime.timedelta`
object, we recommend using the macros or cron expressions instead, as
it enforces this idea of rounded schedules.

When using `depends_on_past=True`, it’s important to pay special attention
to `start_date`, as the past dependency is not enforced only on the specific
schedule of the `start_date` specified for the task. It’s also
important to watch DagRun activity status in time when introducing
new `depends_on_past=True`, unless you are planning on running a backfill
for the new task(s).

It is also important to note that the task’s `start_date` is ignored in backfills.