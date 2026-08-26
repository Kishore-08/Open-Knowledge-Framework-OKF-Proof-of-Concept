---
id: apache-airflow-state-store-https-airflow-apache-org-docs-apache-airflow-sta-b3467d3c
type: concept
title: '[[state\_store]](https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html#id33)'
description: Configuration for task and asset state storage backend.
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### [[state\_store]](https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html#id33)

Configuration for task and asset state storage backend.

#### backend

> Added in version 3.3.0.

Full dotted path to the class that implements state storage for tasks and assets.
The class must be a subclass of `BaseStoreBackend`.
The default implementation persists state in the Airflow metadata database.

Type:
:   string

Default:
:   `airflow.state.metastore.MetastoreBackend`

Environment Variable:
:   `AIRFLOW__STATE_STORE__BACKEND`

Example:
:   `mypackage.state.CustomStoreBackend`

#### clear\_on\_success

> Added in version 3.3.0.

If set to True, all task state keys for a task instance are automatically cleared
when that task instance moved to SUCCESS.

Defaults to False so that task state persists after success for observability —
operators and the UI can inspect what the task wrote (e.g. submitted job IDs,
advanced watermarks) after the run completes.
Consider setting to True if you do not need post-success visibility and want automatic
cleanup without waiting for the global retention period.

Type:
:   boolean

Default:
:   `False`

Environment Variable:
:   `AIRFLOW__STATE_STORE__CLEAR_ON_SUCCESS`

Example:
:   `True`

#### default\_retention\_days

> Added in version 3.3.0.

Number of days to retain task state after their last update.
Rows older than this are removed when cleanup is triggered.
This config does not affect asset\_state\_store rows.
Set to 0 to disable time-based cleanup entirely.

Type:
:   integer

Default:
:   `30`

Environment Variable:
:   `AIRFLOW__STATE_STORE__DEFAULT_RETENTION_DAYS`

Example:
:   `7`

#### max\_value\_storage\_bytes

> Added in version 3.3.0.

Maximum size in bytes that a single task or asset store value may have when written via
the public REST API. Values that exceed this limit are rejected with a 422 error.

Workers writing via the execution API are not blocked, they log a warning and the write
proceeds, so tasks are never interrupted mid-execution. Set to 0 to disable the limit entirely.

The default of 65535 bytes (64 KB) is a policy default suited for coordination state such as
job IDs, cursors, and small status maps — the underlying database column (MEDIUMTEXT on MySQL,
unbounded Text on Postgres) does not enforce this limit. For larger payloads, configure a custom
[workers] state\_store\_backend to offload values to external storage.

Type:
:   integer

Default:
:   `65535`

Environment Variable:
:   `AIRFLOW__STATE_STORE__MAX_VALUE_STORAGE_BYTES`

Example:
:   `1048576`

#### state\_cleanup\_batch\_size

> Added in version 3.3.0.

Number of rows deleted per batch during cleanup. Defaults to 0 (no batching).
Tune this on deployments with large task\_state\_store tables to improve performance per transaction.

Type:
:   integer

Default:
:   `0`

Environment Variable:
:   `AIRFLOW__STATE_STORE__STATE_CLEANUP_BATCH_SIZE`

Example:
:   `10000`