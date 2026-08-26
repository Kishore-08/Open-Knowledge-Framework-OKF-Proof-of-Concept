---
id: apache-airflow-how-to-reduce-dag-scheduling-latency-task-delay-1ae4eb88
type: concept
title: How to reduce Dag scheduling latency / task delay?
description: Airflow 2.0 has low Dag scheduling latency out of the box (particularly
  when compared with Airflow 1.10.x),
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/faq.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### How to reduce Dag scheduling latency / task delay?

Airflow 2.0 has low Dag scheduling latency out of the box (particularly when compared with Airflow 1.10.x),
however, if you need more throughput you can [start multiple schedulers](https://airflow.apache.org/docs/apache-airflow/stable/administration-and-deployment/scheduler.html#scheduler-ha).