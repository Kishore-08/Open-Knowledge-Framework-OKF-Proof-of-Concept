---
id: apache-airflow-communication-8dafd1cd
type: concept
title: Communication
description: Airflow executes tasks of a Dag on different servers in case you are
  using [Kubernetes executor](https://airflow.apache.org/docs/apache-airflow-providers-cncf-kubernetes/stable/kubernetes_executor.htm
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/best-practices.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Communication

Airflow executes tasks of a Dag on different servers in case you are using [Kubernetes executor](https://airflow.apache.org/docs/apache-airflow-providers-cncf-kubernetes/stable/kubernetes_executor.html "(in apache-airflow-providers-cncf-kubernetes v10.21.0)") or [Celery executor](https://airflow.apache.org/docs/apache-airflow-providers-celery/stable/celery_executor.html "(in apache-airflow-providers-celery v3.23.1)").
Therefore, you should not store any file or config in the local filesystem as the downstream task is likely to run on a different server without access to it — for example, a task that downloads the data file that the downstream task processes.
In the case of `Local executor`,
storing a file on disk can make retries harder e.g., your task requires a config file that is deleted by another task in Dag.

If possible, use `XCom` to communicate small messages between tasks and a good way of passing larger data between tasks is to use a remote storage such as S3/HDFS.
For example, if we have a task that stores processed data in S3 that task can push the S3 path for the output data in `Xcom`,
and the downstream tasks can pull the path from XCom and use it to read the data.

The tasks should also not store any authentication parameters such as passwords or token inside them.
Where at all possible, use [Connections](https://airflow.apache.org/docs/apache-airflow/stable/authoring-and-scheduling/connections.html) to store data securely in Airflow backend and retrieve them using a unique connection id.