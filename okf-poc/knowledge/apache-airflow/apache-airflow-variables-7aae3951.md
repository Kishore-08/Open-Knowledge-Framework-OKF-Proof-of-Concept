---
id: apache-airflow-variables-7aae3951
type: concept
title: Variables
description: The Airflow engine passes a few variables by default that are accessible
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/templates-ref.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Variables

The Airflow engine passes a few variables by default that are accessible
in all templates

| Variable | Type | Description |
| --- | --- | --- |
| `{{ data_interval_start }}` | [pendulum.DateTime](https://pendulum.eustace.io/docs/#introduction) | Start of the data interval. Added in version 2.2. |
| `{{ data_interval_end }}` | [pendulum.DateTime](https://pendulum.eustace.io/docs/#introduction) | End of the data interval. Added in version 2.2. |
| `{{ logical_date }}` | [pendulum.DateTime](https://pendulum.eustace.io/docs/#introduction) | A date-time that logically identifies the current Dag run. This value does not contain any semantics, but is simply a value for identification.  Use `data_interval_start` and `data_interval_end` instead if you want a value that has real-world semantics,  such as to get a slice of rows from the database based on timestamps. |
| `{{ exception }}` | None | str | Exception KeyboardInterrupt | Error occurred while running task instance. |
| `{{ prev_data_interval_start_success }}` | [pendulum.DateTime](https://pendulum.eustace.io/docs/#introduction) | `None` | Start of the data interval of the prior successful `DagRun`.  Added in version 2.2. |
| `{{ prev_data_interval_end_success }}` | [pendulum.DateTime](https://pendulum.eustace.io/docs/#introduction) | `None` | End of the data interval of the prior successful `DagRun`.  Added in version 2.2. |
| `{{ prev_start_date_success }}` | [pendulum.DateTime](https://pendulum.eustace.io/docs/#introduction) | `None` | Start date from prior successful `DagRun` (if available). |
| `{{ prev_end_date_success }}` | [pendulum.DateTime](https://pendulum.eustace.io/docs/#introduction)  `None` | End date from prior successful `DagRun` (if available). |
| `{{ inlets }}` | list | List of inlets declared on the task. |
| `{{ inlet_events }}` | dict[str, …] | Access past events of inlet assets. See [Assets](https://airflow.apache.org/docs/apache-airflow/stable/authoring-and-scheduling/asset-scheduling.html). Added in version 2.10. |
| `{{ outlets }}` | list | List of outlets declared on the task. |
| `{{ outlet_events }}` | dict[str, …] | Accessors to attach information to asset events that will be emitted by the current task.  See [Assets](https://airflow.apache.org/docs/apache-airflow/stable/authoring-and-scheduling/asset-scheduling.html). Added in version 2.10. |
| `{{ dag }}` | DAG | The currently running `DAG`. You can read more about Dags in [Dags](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/dags.html). |
| `{{ task }}` | BaseOperator | The currently running `BaseOperator`. You can read more about Tasks in [Operators](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/operators.html) |
| `{{ task_reschedule_count }}` | int | How many times current task has been rescheduled. Relevant to `mode="reschedule"` sensors. |
| `{{ macros }}` |  | A reference to the macros package. See [Macros](https://airflow.apache.org/docs/apache-airflow/stable/templates-ref.html#macros) below. |
| `{{ task_instance }}` | TaskInstance | The currently running `TaskInstance`. |
| `{{ ti }}` | TaskInstance | Same as `{{ task_instance }}`. |
| `{{ params }}` | dict[str, Any] | The user-defined params. This can be overridden by the mapping  passed to `trigger_dag -c` if `dag_run_conf_overrides_params`  is enabled in `airflow.cfg`. |
| `{{ partition_key }}` | str | None | The partition key from the current `DagRun`.  Returns `None` if no partition key was set. Added in version 3.3.0. |
| `{{ partition_date }}` | datetime | None | The partition datetime from the current `DagRun`.  Use `{{ partition_date | ds }}` and related filters for formatting.  Returns `None` if no partition date was set. Added in version 3.3.0. |
| `{{ var.value }}` |  | Airflow variables. See [Airflow Variables in Templates](https://airflow.apache.org/docs/apache-airflow/stable/templates-ref.html#airflow-variables-in-templates) below. |
| `{{ var.json }}` |  | Airflow