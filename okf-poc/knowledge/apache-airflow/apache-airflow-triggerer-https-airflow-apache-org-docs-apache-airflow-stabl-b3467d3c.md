---
id: apache-airflow-triggerer-https-airflow-apache-org-docs-apache-airflow-stabl-b3467d3c
type: concept
title: '[[triggerer]](https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html#id35)'
description: '> Added in version 3.2.0.'
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### [[triggerer]](https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html#id35)

#### blocked\_main\_thread\_warning\_threshold

> Added in version 3.2.0.

Threshold in seconds for logging a warning when the Triggerer’s async thread appears blocked.
Increase this value if your deployment can tolerate longer delays in the Triggerer’s async
loop before logging a warning.

Type:
:   float

Default:
:   `0.2`

Environment Variable:
:   `AIRFLOW__TRIGGERER__BLOCKED_MAIN_THREAD_WARNING_THRESHOLD`

#### capacity

> Added in version 2.2.0.

How many triggers a single Triggerer will run at once, by default.

Type:
:   integer

Default:
:   `1000`

Environment Variable:
:   `AIRFLOW__TRIGGERER__CAPACITY`

#### job\_heartbeat\_sec

> Added in version 2.6.3.

How often to heartbeat the Triggerer job to ensure it hasn’t been killed.

Type:
:   float

Default:
:   `5`

Environment Variable:
:   `AIRFLOW__TRIGGERER__JOB_HEARTBEAT_SEC`

#### max\_trigger\_to\_select\_per\_loop

> Added in version 3.2.0.

Maximum number of triggers to select per loop. Set this notably lower than `[triggerer] capacity`
to keep load balanced across triggerers in HA deployments.
Benchmarks show that two triggerers can still claim about 1,000 triggers within one second by default.

Type:
:   integer

Default:
:   `50`

Environment Variable:
:   `AIRFLOW__TRIGGERER__MAX_TRIGGER_TO_SELECT_PER_LOOP`

#### on\_kill\_timeout

> Added in version 3.3.0.

Maximum number of seconds the triggerer will wait for `BaseTrigger.on_kill()` to complete
before giving up and logging a warning. Prevents a slow or hung external API call from
blocking the triggerer indefinitely when a deferred task is killed by a user.

Type:
:   integer

Default:
:   `30`

Environment Variable:
:   `AIRFLOW__TRIGGERER__ON_KILL_TIMEOUT`

#### queues\_enabled

> Added in version 3.2.0.

When set to True, deferred tasks will register triggers with the task queue they originated from,
and triggerers can selectively run triggers based on their queue assignment. Only relevant when using
executors which support task queue assignment. For more details, refer to the trigger docs.

Type:
:   boolean

Default:
:   `False`

Environment Variable:
:   `AIRFLOW__TRIGGERER__QUEUES_ENABLED`

#### runner\_health\_check\_threshold

> Added in version 3.2.2.

If the TriggerRunner subprocess’s async event loop sends no communication to the parent
process for more than this many seconds, the parent stops updating the triggerer’s
heartbeat in the database. The triggerer then appears unhealthy to the scheduler, which
will reassign its triggers. This detects a deadlocked or hung event loop that the normal
process-alive check cannot catch. Set to 0 to disable the watchdog.

Type:
:   float

Default:
:   `30`

Environment Variable:
:   `AIRFLOW__TRIGGERER__RUNNER_HEALTH_CHECK_THRESHOLD`

#### shared\_stream\_ack\_timeout

> Added in version 3.3.0.

Per-event ack timeout in seconds for shared-stream triggers running in ack mode (triggers that
override `BaseEventTrigger.create_shared_stream_producer`). A subscriber that has not finished
processing an event (moved past it and had its derived trigger events confirmed persisted) within
this window is force-failed. Other subscribers in the same group are unaffected; once they
resolve, the producer advances normally.

Type:
:   float

Default:
:   `300.0`

Environment Variable:
:   `AIRFLOW__TRIGGERER__SHARED_STREAM_ACK_TIMEOUT`

#### shared\_stream\_cohort\_grace\_period

> Added in version 3.3.0.

Seconds to delay the start of polling after a shared-stream group is created, giving triggers
that share the same key a window to subscribe before any event is broadcast. The default of 0
starts polling immediately (no delay). Set to a small positive value (e.g. 2.0–5.0) to reduce
the chance of triggers missing events on triggerer restart, when multiple triggers sharing a key
re-subscribe concurrently and the first to arrive would otherwise start the poll before the
o