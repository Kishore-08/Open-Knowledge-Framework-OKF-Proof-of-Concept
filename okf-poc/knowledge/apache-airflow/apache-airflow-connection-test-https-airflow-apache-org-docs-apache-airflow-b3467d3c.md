---
id: apache-airflow-connection-test-https-airflow-apache-org-docs-apache-airflow-b3467d3c
type: concept
title: '[[connection\_test]](https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html#id15)'
description: Configuration for the deferred connection-test workflow that dispatches
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### [[connection\_test]](https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html#id15)

Configuration for the deferred connection-test workflow that dispatches
test requests to workers via the executor (instead of running them
in-process on the API server).

#### max\_concurrency

> Added in version 3.3.0.

Maximum number of connection tests that can be active
(QUEUED + RUNNING) at the same time. Excess tests will remain in
PENDING state until slots become available. This cap is enforced
per-scheduler, not globally: with N HA schedulers the worst-case
per-tick dispatch is `N * max_concurrency`. Connection tests are
user-initiated and rare, so the overshoot self-corrects via the
reaper.

Type:
:   integer

Default:
:   `4`

Environment Variable:
:   `AIRFLOW__CONNECTION_TEST__MAX_CONCURRENCY`

#### reaper\_interval

> Added in version 3.3.0.

How often (in seconds) the scheduler should check for stale
connection tests (QUEUED or RUNNING past their timeout + grace
period) and mark them as failed.

Type:
:   float

Default:
:   `30.0`

Environment Variable:
:   `AIRFLOW__CONNECTION_TEST__REAPER_INTERVAL`

#### timeout

> Added in version 3.3.0.

Maximum number of seconds a worker-dispatched connection test is
allowed to run before it is considered timed out. The scheduler
reaper uses this value plus a grace period to mark stale tests as
failed.

Type:
:   integer

Default:
:   `60`

Environment Variable:
:   `AIRFLOW__CONNECTION_TEST__TIMEOUT`