---
id: apache-airflow-significant-changes-51425edb
type: concept
title: Significant Changes
description: In order to make `airflow dags test` more useful as a testing and debugging
  tool, we no
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/release_notes.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Significant Changes

#### `airflow dags test` no longer performs a backfill job (#26400)

In order to make `airflow dags test` more useful as a testing and debugging tool, we no
longer run a backfill job and instead run a “local task runner”. Users can still backfill
their DAGs using the `airflow dags backfill` command.

#### Airflow config section `kubernetes` renamed to `kubernetes_executor` (#26873)

KubernetesPodOperator no longer considers any core kubernetes config params, so this section now only applies to kubernetes executor. Renaming it reduces potential for confusion.

#### `AirflowException` is now thrown as soon as any dependent tasks of ExternalTaskSensor fails (#27190)

`ExternalTaskSensor` no longer hangs indefinitely when `failed_states` is set, an `execute_date_fn` is used, and some but not all of the dependent tasks fail.
Instead, an `AirflowException` is thrown as soon as any of the dependent tasks fail.
Any code handling this failure in addition to timeouts should move to caching the `AirflowException` `BaseClass` and not only the `AirflowSensorTimeout` subclass.

#### The Airflow config option `scheduler.deactivate_stale_dags_interval` has been renamed to `scheduler.parsing_cleanup_interval` (#27828).

The old option will continue to work but will issue deprecation warnings, and will be removed entirely in Airflow 3.