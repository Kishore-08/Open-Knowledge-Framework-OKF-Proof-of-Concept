---
id: apache-airflow-task-instance-heartbeat-timeout-dda6bf43
type: concept
title: Task Instance Heartbeat Timeout
description: No system runs perfectly, and task instances are expected to die once
  in a while.
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/tasks.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Task Instance Heartbeat Timeout

No system runs perfectly, and task instances are expected to die once in a while.

`TaskInstances` may get stuck in a `running` state despite their associated jobs being inactive
(for example if the `TaskInstance`’s worker ran out of memory). Such tasks were formerly known as zombie tasks. Airflow will find these
periodically, clean them up, and mark the `TaskInstance` as failed or retry it if it has available retries. The `TaskInstance`’s heartbeat can timeout for
many reasons, including:

- The Airflow worker ran out of memory and was OOMKilled.
- The Airflow worker failed its liveness probe, so the system (for example, Kubernetes) restarted the worker.
- The system (for example, Kubernetes) scaled down and moved an Airflow worker from one node to another.