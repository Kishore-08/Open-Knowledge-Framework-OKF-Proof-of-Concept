---
id: apache-airflow-lingering-task-supervisor-processes-72471d0d
type: concept
title: Lingering task supervisor processes
description: Under very high concurrency the socket handlers inside the task supervisor
  may
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/troubleshooting.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Lingering task supervisor processes

Under very high concurrency the socket handlers inside the task supervisor may
miss the final EOF events from the task process. When this occurs the supervisor
believes sockets are still open and will not exit. The
[workers.socket\_cleanup\_timeout](https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html#config-workers-socket-cleanup-timeout) option controls how long the supervisor
waits after the task finishes before force-closing any remaining sockets. If you
observe leftover `supervisor` processes, consider increasing this delay.

Was this entry helpful?