---
id: apache-airflow-scheduler-https-airflow-apache-org-docs-apache-airflow-stabl-b3467d3c
type: concept
title: '[[scheduler]](https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html#id27)'
description: '> Added in version 2.6.3.'
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### [[scheduler]](https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html#id27)

#### allowed\_run\_id\_pattern

> Added in version 2.6.3.

The run\_id pattern used to verify the validity of user input to the run\_id parameter when
triggering a DAG. This pattern cannot change the pattern used by scheduler to generate run\_id
for scheduled DAG runs or DAG runs triggered without changing the run\_id parameter.

Type:
:   string

Default:
:   `^[A-Za-z0-9_.~:+-]+$`

Environment Variable:
:   `AIRFLOW__SCHEDULER__ALLOWED_RUN_ID_PATTERN`

#### catchup\_by\_default

Turn on scheduler catchup by setting this to `True`.
Default behavior is unchanged and
Command Line Backfills still work, but the scheduler
will not do scheduler catchup if this is `False`,
however it can be set on a per DAG basis in the
DAG definition (catchup)

Type:
:   boolean

Default:
:   `False`

Environment Variable:
:   `AIRFLOW__SCHEDULER__CATCHUP_BY_DEFAULT`

#### create\_cron\_data\_intervals

> Added in version 2.9.0.

Whether to create DAG runs that span an interval or one single point in time for cron schedules, when
a cron string is provided to `schedule` argument of a DAG.

- `True`: **CronDataIntervalTimetable** is used, which is suitable
  for DAGs with well-defined data interval. You get contiguous intervals from the end of the previous
  interval up to the scheduled datetime.
- `False`: **CronTriggerTimetable** is used, which is closer to the behavior of cron itself.

Notably, for **CronTriggerTimetable**, the logical date is the same as the time the DAG Run will
try to schedule, while for **CronDataIntervalTimetable**, the logical date is the beginning of
the data interval, but the DAG Run will try to schedule at the end of the data interval.

When a DAG is switched from **CronTriggerTimetable** to **CronDataIntervalTimetable** (for example,
by flipping this setting from `False` to `True`), the next scheduled run skips one period past
the most recent **CronTriggerTimetable** run to avoid colliding with its logical date.

See also

[Differences between “trigger” and “data interval” timetables](https://airflow.apache.org/docs/apache-airflow/stable/authoring-and-scheduling/timetable.html#differences-between-trigger-and-data-interval-timetables)

Type:
:   boolean

Default:
:   `False`

Environment Variable:
:   `AIRFLOW__SCHEDULER__CREATE_CRON_DATA_INTERVALS`

#### create\_delta\_data\_intervals

> Added in version 2.11.0.

Whether to create DAG runs that span an interval or one single point in time when a timedelta or
relativedelta is provided to `schedule` argument of a DAG.

- `True`: **DeltaDataIntervalTimetable** is used, which is suitable for DAGs with well-defined data
  interval. You get contiguous intervals from the end of the previous interval up to the scheduled
  datetime.
- `False`: **DeltaTriggerTimetable** is used, which is suitable for DAGs that simply want to say
  e.g. “run this every day” and do not care about the data interval.

Notably, for **DeltaTriggerTimetable**, the logical date is the same as the time the DAG Run will
try to schedule, while for **DeltaDataIntervalTimetable**, the logical date is the beginning of
the data interval, but the DAG Run will try to schedule at the end of the data interval.

See also

[Differences between “trigger” and “data interval” timetables](https://airflow.apache.org/docs/apache-airflow/stable/authoring-and-scheduling/timetable.html#differences-between-trigger-and-data-interval-timetables)

Type:
:   boolean

Default:
:   `False`

Environment Variable:
:   `AIRFLOW__SCHEDULER__CREATE_DELTA_DATA_INTERVALS`

#### dagrun\_metrics\_interval

> Added in version 3.1.0.

How often (in seconds) the scheduler emits metrics on running DAG runs
to StatsD (if statsd\_on is enabled)

Type:
:   float

Default:
:   `30.0`

Environment Variable:
:   `AIRFLOW__SCHEDULER__DAGRUN_METRICS_INTERVAL`

#### enable\_health\_check

> Added in version 2.4.0.

When you start a scheduler, airflow sta