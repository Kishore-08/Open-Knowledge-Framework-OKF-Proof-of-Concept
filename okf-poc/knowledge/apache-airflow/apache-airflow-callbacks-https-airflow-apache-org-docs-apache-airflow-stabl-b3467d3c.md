---
id: apache-airflow-callbacks-https-airflow-apache-org-docs-apache-airflow-stabl-b3467d3c
type: concept
title: '[[callbacks]](https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html#id14)'
description: Configuration for callbacks (deadline alerts, etc.).
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### [[callbacks]](https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html#id14)

Configuration for callbacks (deadline alerts, etc.).

#### callback\_execution\_timeout

> Added in version 3.3.0.

Maximum execution time in seconds for deadline callbacks.
Set to a positive integer to enable. When a callback exceeds this duration,
it is terminated with SIGTERM followed by SIGKILL if it does not exit within 5 seconds.
0 means no timeout (default).

Type:
:   integer

Default:
:   `0`

Environment Variable:
:   `AIRFLOW__CALLBACKS__CALLBACK_EXECUTION_TIMEOUT`

Example:
:   `300`