---
id: apache-airflow-deprecations-removals-51425edb
type: concept
title: Deprecations & Removals
description: A number of deprecated features, modules, and interfaces have been removed
  in Airflow 3.0, completing long-standing
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/release_notes.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Deprecations & Removals

A number of deprecated features, modules, and interfaces have been removed in Airflow 3.0, completing long-standing
migrations and cleanups.

Users are encouraged to review the following removals to ensure compatibility:

- **SubDag support has been removed** entirely, including the `SubDagOperator`, related CLI and API interfaces. TaskGroups are now the recommended alternative for nested DAG structures.
- **SLAs have been removed**: The legacy SLA feature, including SLA callbacks and metrics, has been removed. A more flexible replacement mechanism, `DeadlineAlerts`, is planned for a future version of Airflow. Users who relied on SLA-based notifications should consider implementing custom alerting using task-level success/failure hooks or external monitoring integrations.
- **Pickling support has been removed**: All legacy features related to DAG pickling have been fully removed. This includes the `PickleDag` CLI/API, as well as implicit behaviors around `store_serialized_dags = False`. DAGs must now be serialized using the JSON-based serialization system. Ensure any custom Python objects used in DAGs are JSON-serializable.
- **Context parameter cleanup**: Several previously available context variables have been removed from the task execution context, including `conf`, `execution_date`, and `dag_run.external_trigger`. These values are either no longer applicable or have been renamed (e.g., use `dag_run.logical_date` instead of `execution_date`). DAG authors should ensure that templated fields and Python callables do not reference these deprecated keys.
- **Deprecated core imports** have been fully removed. Any use of `airflow.operators.*`, `airflow.hooks.*`, or similar legacy import paths should be updated to import from their respective providers.
- **Configuration cleanup**: Several legacy config options have been removed, including:

  - `scheduler.allow_trigger_in_future`: DAG runs can no longer be triggered with a future logical date. Use `logical_date=None` instead.
  - `scheduler.use_job_schedule` and `scheduler.use_local_tz` have also been removed. These options were deprecated and no longer had any effect.
- **Deprecated utility methods** such as those in `airflow.utils.helpers`, `airflow.utils.process_utils`, and `airflow.utils.timezone` have been removed. Equivalent functionality can now be found in the standard Python library or Airflow provider modules.
- **Removal of deprecated CLI flags and behavior**: Several CLI entrypoints and arguments that were marked for removal in earlier versions have been cleaned up.

To assist with the upgrade, tools like `ruff` (e.g., rule `AIR302`) and `airflow config lint` can help identify
obsolete imports and configuration keys. These utilities are recommended for locating and resolving common
incompatibilities during migration. Please see [Upgrade Guide](https://airflow.apache.org/docs/apache-airflow/stable/installation/upgrading_to_airflow3.html) for more
information.

#### Summary of Removed Features

The following table summarizes user-facing features removed in 3.0 and their recommended replacements. Not all of these
are called out individually above.

| **Feature** | **Replacement / Notes** |
| --- | --- |
| SubDagOperator / SubDAGs | Use TaskGroups |
| SLA callbacks / metrics | Deadline Alerts (planned post-3.0) |
| DAG Pickling | Use JSON serialization; pickling is no longer supported |
| Xcom Pickling | Use custom Xcom backend; pickling is no longer supported |
| `execution_date` context var | Use `dag_run.logical_date` |
| `conf` and `dag_run.external_trigger` | Removed from context; use DAG params or `dag_run` APIs |
| Core `EmailOperator` | Use `EmailOperator` from the `smtp` provider |
| `none_failed_or_skipped` rule | Use `none_failed_min_one_success` |
| `dummy` trigger rule | Use `always` |
| `fail_stop` argument | Use `fail_fast` |
| `store_serialized_dags=False` | DAGs are always serialized; config has no effect |
| Deprecated core i