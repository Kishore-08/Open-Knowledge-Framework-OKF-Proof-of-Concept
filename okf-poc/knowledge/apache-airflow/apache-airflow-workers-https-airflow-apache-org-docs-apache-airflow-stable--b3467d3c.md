---
id: apache-airflow-workers-https-airflow-apache-org-docs-apache-airflow-stable--b3467d3c
type: concept
title: '[[workers]](https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html#id36)'
description: Configuration related to workers that run Airflow tasks.
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### [[workers]](https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html#id36)

Configuration related to workers that run Airflow tasks.

#### execution\_api\_retries

> Added in version 3.0.0.

The maximum number of retry attempts to the execution API server.

Type:
:   integer

Default:
:   `5`

Environment Variable:
:   `AIRFLOW__WORKERS__EXECUTION_API_RETRIES`

#### execution\_api\_retry\_wait\_max

> Added in version 3.0.0.

The maximum amount of time (in seconds) to wait before retrying a failed API request.

Type:
:   float

Default:
:   `90.0`

Environment Variable:
:   `AIRFLOW__WORKERS__EXECUTION_API_RETRY_WAIT_MAX`

#### execution\_api\_retry\_wait\_min

> Added in version 3.0.0.

The minimum amount of time (in seconds) to wait before retrying a failed API request.

Type:
:   float

Default:
:   `1.0`

Environment Variable:
:   `AIRFLOW__WORKERS__EXECUTION_API_RETRY_WAIT_MIN`

#### execution\_api\_timeout

> Added in version 3.1.1.

The timeout (in seconds) for HTTP requests from workers to the Execution API server.
This controls how long a worker will wait for a response from the API server before
timing out. Increase this value if you experience timeout errors under high load.

Type:
:   float

Default:
:   `5.0`

Environment Variable:
:   `AIRFLOW__WORKERS__EXECUTION_API_TIMEOUT`

#### max\_failed\_heartbeats

> Added in version 3.0.0.

The maximum number of consecutive failed heartbeats before terminating the task instance process.

Type:
:   integer

Default:
:   `3`

Environment Variable:
:   `AIRFLOW__WORKERS__MAX_FAILED_HEARTBEATS`

#### min\_heartbeat\_interval

> Added in version 3.0.0.

The minimum interval (in seconds) at which the worker checks the task instance’s
heartbeat status with the API server to confirm it is still alive.

Type:
:   integer

Default:
:   `5`

Environment Variable:
:   `AIRFLOW__WORKERS__MIN_HEARTBEAT_INTERVAL`

#### missing\_dag\_retries

> Added in version 3.1.7.

Maximum number of times a task will be rescheduled if the worker fails to
load the Dag or task definition during startup.

This situation can occur due to transient infrastructure issues such as
missing Dag files, temporary filesystem or network problems, or bundle
synchronization delays. Rescheduling in this case does not count as a
task retry.

Set this value to 0 to disable rescheduling and fail the task immediately
on startup failures.

Type:
:   integer

Default:
:   `3`

Environment Variable:
:   `AIRFLOW__WORKERS__MISSING_DAG_RETRIES`

#### missing\_dag\_retry\_delay

> Added in version 3.1.7.

Delay in seconds before a task is rescheduled after a worker startup
failure caused by an inability to load the Dag or task definition.

This delay is applied when the task runner requests the scheduler to
reschedule the task instance in UP\_FOR\_RESCHEDULE state.

Type:
:   integer

Default:
:   `60`

Environment Variable:
:   `AIRFLOW__WORKERS__MISSING_DAG_RETRY_DELAY`

#### secrets\_backend

> Added in version 3.0.0.

Full class name of secrets backend to enable for workers (will precede env vars backend)

Type:
:   string

Default:
:   `''`

Environment Variable:
:   `AIRFLOW__WORKERS__SECRETS_BACKEND`

Example:
:   `airflow.providers.amazon.aws.secrets.systems_manager.SystemsManagerParameterStoreBackend`

#### secrets\_backend\_kwargs

> Added in version 3.0.0.

The secrets\_backend\_kwargs param is loaded into a dictionary and passed to `__init__`
of secrets backend class. See documentation for the secrets backend you are using.
JSON is expected.

Example for AWS Systems Manager ParameterStore:
`{"connections_prefix": "/airflow/connections", "profile_name": "default"}`

You can also set individual kwargs via `AIRFLOW__WORKERS__SECRETS_BACKEND_KWARG__<KEY>=value`
environment variables. Per-key variables override the same key in this JSON setting.
Values are raw strings (not JSON-parsed).

Type:
:   string

Default:
:   `''`

Environment Variables:
:   `AIRFLOW__WORKERS__SECRETS_BACKEND_KWARGS`