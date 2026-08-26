---
id: apache-airflow-mapped-tasks-dda6bf43
type: concept
title: Mapped tasks
description: Policies work with dynamic task mapping via `.partial()`. The policy
  applies
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/tasks.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Mapped tasks

Policies work with dynamic task mapping via `.partial()`. The policy applies
per mapped task instance – if instance 2 of 10 hits FAIL, the other 9 continue
independently:

```
@task.partial(retry_policy=my_policy).expand(input=[1, 2, 3])
def my_mapped_task(input): ...
```

The policy is set at the task level via `.partial()`; all mapped instances
share one policy. Per-index variation is not supported on `.expand()`, but the
policy’s `evaluate()` method receives the exception, `try_number`, and full
context, so per-index branching can be done inside the policy if needed.