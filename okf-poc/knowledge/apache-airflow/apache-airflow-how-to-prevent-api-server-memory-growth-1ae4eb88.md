---
id: apache-airflow-how-to-prevent-api-server-memory-growth-1ae4eb88
type: concept
title: How to prevent API server memory growth?
description: The API server caches serialized Dag objects in memory. Over time, as
  Dag versions accumulate
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/faq.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### How to prevent API server memory growth?

The API server caches serialized Dag objects in memory. Over time, as Dag versions accumulate
(see [Why does my Dag version keep increasing?](https://airflow.apache.org/docs/apache-airflow/stable/faq.html#faq-dag-version-inflation)), this cache grows and can consume several gigabytes of memory.

There are two complementary approaches:

**1. Bounded DAG caching (available since Airflow 3.3.0)**

The API server supports LRU+TTL caching that bounds how many serialized Dag versions are kept
in memory. Configure this in the `[api]` section:

```
[api]
dag_cache_size = 64    ; max cached versions (0 = unbounded, pre-3.2 behavior)
dag_cache_ttl = 3600   ; seconds before a cached entry expires (0 = LRU only)
```

The cache is keyed by Dag version ID. After a Dag is updated, the API server may serve the
previous version until the cached entry expires (controlled by `dag_cache_ttl`).

See [dag\_cache\_size](https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html#config-api-dag-cache-size) and [dag\_cache\_ttl](https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html#config-api-dag-cache-ttl) for the full
configuration reference.

**2. Gunicorn with rolling worker restarts (available since Airflow 3.2.0)**

Gunicorn periodically recycles worker processes, releasing all accumulated memory. It also
uses `preload` + `fork`, so workers share read-only memory pages via copy-on-write, reducing overall
memory usage by 40-50% compared to uvicorn’s multiprocess mode.

To enable gunicorn with worker recycling:

```
[api]
server_type = gunicorn
# Restart each worker every 12 hours (43200 seconds)
worker_refresh_interval = 43200
worker_refresh_batch_size = 1
```

This requires the `apache-airflow-core[gunicorn]` extra to be installed.

See [server\_type](https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html#config-api-server-type), [worker\_refresh\_interval](https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html#config-api-worker-refresh-interval), and
[worker\_refresh\_batch\_size](https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html#config-api-worker-refresh-batch-size) for the full configuration reference.

Note

Worker recycling handles memory growth from *any* source, not just the Dag cache.
For production deployments, using both bounded caching and gunicorn worker recycling
provides the best results.

## MySQL and MySQL variant Databases