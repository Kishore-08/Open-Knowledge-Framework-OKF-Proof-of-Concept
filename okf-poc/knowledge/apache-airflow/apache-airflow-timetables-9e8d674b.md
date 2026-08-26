---
id: apache-airflow-timetables-9e8d674b
type: concept
title: Timetables
description: Custom timetable implementations provide Airflow’s scheduler additional
  logic to
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/public-airflow-interface.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Timetables

Custom timetable implementations provide Airflow’s scheduler additional logic to
schedule Dag runs in ways not possible with built-in schedule expressions.
All Timetables derive from [`Timetable`](https://airflow.apache.org/docs/apache-airflow/stable/_api/airflow/timetables/base/index.html#airflow.timetables.base.Timetable "airflow.timetables.base.Timetable").

Airflow has a set of Timetables that are considered public. You are free to extend their functionality
by extending them:

- [airflow.timetables](https://airflow.apache.org/docs/apache-airflow/stable/_api/airflow/timetables/index.html)

You can read more about Timetables in [Customizing Dag Scheduling with Timetables](https://airflow.apache.org/docs/apache-airflow/stable/howto/timetable.html).