---
id: apache-airflow-self-checks-8dafd1cd
type: concept
title: Self-Checks
description: You can also implement checks in a Dag to make sure the tasks are producing
  the results as expected.
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/best-practices.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Self-Checks

You can also implement checks in a Dag to make sure the tasks are producing the results as expected.
As an example, if you have a task that pushes data to S3, you can implement a check in the downstream task. For example, the check could
make sure that the partition is created in S3 and perform some simple checks to determine if the data is correct.

Similarly, if you have a task that starts a microservice in Kubernetes or Mesos, you should check if the service has started or not using [`airflow.providers.http.sensors.http.HttpSensor`](https://airflow.apache.org/docs/apache-airflow-providers-http/stable/_api/airflow/providers/http/sensors/http/index.html#airflow.providers.http.sensors.http.HttpSensor "(in apache-airflow-providers-http v6.0.5)").

```
task = PushToS3(...)
check = S3KeySensor(
    task_id="check_parquet_exists",
    bucket_key="s3://bucket/key/foo.parquet",
    poke_interval=0,
    timeout=0,
)
task >> check
```