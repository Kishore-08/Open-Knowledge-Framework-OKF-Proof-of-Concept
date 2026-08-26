---
id: apache-airflow-how-it-works-dda6bf43
type: concept
title: How it works
description: The policy runs in the **task worker process** (never the scheduler)
  between catching the
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/tasks.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### How it works

The policy runs in the **task worker process** (never the scheduler) between catching the
exception and deciding the task’s next state. Each policy decision is logged in the task
logs as `Retry policy decision action=<action> reason=<reason>`.

When a task fails, the policy evaluates the exception and returns one of three actions:

- **RETRY** – retry the task, optionally with a custom delay that overrides `retry_delay`.
  The retry is still subject to the task’s `retries` count – a policy can fail earlier but
  cannot extend past the configured maximum.
- **FAIL** – fail immediately, skipping any remaining retries.
- **DEFAULT** – fall through to the standard retry logic (`retries` count and `retry_delay`).

Rules are evaluated in order; the first matching rule wins.
If no rule matches, the policy returns **DEFAULT** (standard retry behaviour).