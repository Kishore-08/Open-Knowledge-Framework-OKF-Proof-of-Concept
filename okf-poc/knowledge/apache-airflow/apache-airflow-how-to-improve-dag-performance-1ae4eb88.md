---
id: apache-airflow-how-to-improve-dag-performance-1ae4eb88
type: concept
title: How to improve Dag performance?
description: 'There are some Airflow configuration to allow for a larger scheduling
  capacity and frequency:'
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/faq.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### How to improve Dag performance?

There are some Airflow configuration to allow for a larger scheduling capacity and frequency:

- [parallelism](https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html#config-core-parallelism)
- [max\_active\_tasks\_per\_dag](https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html#config-core-max-active-tasks-per-dag)
- [max\_active\_runs\_per\_dag](https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html#config-core-max-active-runs-per-dag)

Dags have configurations that improves efficiency:

- `max_active_tasks`: Overrides [max\_active\_tasks\_per\_dag](https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html#config-core-max-active-tasks-per-dag).
- `max_active_runs`: Overrides [max\_active\_runs\_per\_dag](https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html#config-core-max-active-runs-per-dag).

Operators or tasks also have configurations that improves efficiency and scheduling priority:

- `max_active_tis_per_dag`: This parameter controls the number of concurrent running task instances across `dag_runs`
  per task.
- `pool`: See [Pools](https://airflow.apache.org/docs/apache-airflow/stable/administration-and-deployment/pools.html#concepts-pool).
- `priority_weight`: See [Priority Weights](https://airflow.apache.org/docs/apache-airflow/stable/administration-and-deployment/priority-weight.html#concepts-priority-weight).
- `queue`: See [Queues](https://airflow.apache.org/docs/apache-airflow-providers-celery/stable/celery_executor.html#celery-executor-queue "(in apache-airflow-providers-celery v3.23.1)") for CeleryExecutor deployments only.