---
id: apache-airflow-using-multiple-docker-images-and-celery-queues-8dafd1cd
type: concept
title: Using multiple Docker Images and Celery Queues
description: There is a possibility (though it requires a deep knowledge of Airflow
  deployment) to run Airflow tasks
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/best-practices.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Using multiple Docker Images and Celery Queues

There is a possibility (though it requires a deep knowledge of Airflow deployment) to run Airflow tasks
using multiple, independent Docker images. This can be achieved via allocating different tasks to different
Queues and configuring your Celery workers to use different images for different Queues. This, however,
(at least currently) requires a lot of manual deployment configuration and intrinsic knowledge of how
Airflow, Celery and Kubernetes works. Also it introduces quite some overhead for running the tasks - there
are less chances for resource reuse and it’s much more difficult to fine-tune such a deployment for
cost of resources without impacting the performance and stability.

One of the possible ways to make it more useful is
[AIP-46 Runtime isolation for Airflow tasks and Dag parsing](https://cwiki.apache.org/confluence/display/AIRFLOW/AIP-46+Runtime+isolation+for+airflow+tasks+and+dag+parsing).
and completion of [AIP-43 Dag Processor Separation](https://cwiki.apache.org/confluence/display/AIRFLOW/AIP-43+DAG+Processor+separation)
Until those are implemented, there are very few benefits of using this approach and it is not recommended.

When those AIPs are implemented, however, this will open up the possibility of a more multi-tenant approach,
where multiple teams will be able to have completely isolated sets of dependencies that will be used across
the full lifecycle of a Dag - from parsing to execution.

Was this entry helpful?