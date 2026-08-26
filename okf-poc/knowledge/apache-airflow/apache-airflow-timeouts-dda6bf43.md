---
id: apache-airflow-timeouts-dda6bf43
type: concept
title: Timeouts
description: If you want a task to have a maximum runtime, set its `execution_timeout`
  attribute to a `datetime.timedelta` value
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/tasks.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Timeouts

If you want a task to have a maximum runtime, set its `execution_timeout` attribute to a `datetime.timedelta` value
that is the maximum permissible runtime. This applies to all Airflow tasks, including sensors. `execution_timeout` controls the
maximum time allowed for every execution. If `execution_timeout` is breached, the task times out and
`AirflowTaskTimeout` is raised.

In addition, sensors have a `timeout` parameter. This only matters for sensors in `reschedule` mode. `timeout` controls the maximum
time allowed for the sensor to succeed. If `timeout` is breached, `AirflowSensorTimeout` will be raised and the sensor fails immediately
without retrying.

The following `SFTPSensor` example illustrates this. The `sensor` is in `reschedule` mode, meaning it
is periodically executed and rescheduled until it succeeds.

- Each time the sensor pokes the SFTP server, it is allowed to take maximum 60 seconds as defined by `execution_timeout`.
- If it takes the sensor more than 60 seconds to poke the SFTP server, `AirflowTaskTimeout` will be raised.
  The sensor is allowed to retry when this happens. It can retry up to 2 times as defined by `retries`.
- From the start of the first execution, till it eventually succeeds (i.e. after the file ‘root/test’ appears),
  the sensor is allowed maximum 3600 seconds as defined by `timeout`. In other words, if the file
  does not appear on the SFTP server within 3600 seconds, the sensor will raise `AirflowSensorTimeout`.
  It will not retry when this error is raised.
- If the sensor fails due to other reasons such as network outages during the 3600 seconds interval,
  it can retry up to 2 times as defined by `retries`. Retrying does not reset the `timeout`. It will
  still have up to 3600 seconds in total for it to succeed.

```
sensor = SFTPSensor(
    task_id="sensor",
    path="/root/test",
    execution_timeout=timedelta(seconds=60),
    timeout=3600,
    retries=2,
    mode="reschedule",
)
```