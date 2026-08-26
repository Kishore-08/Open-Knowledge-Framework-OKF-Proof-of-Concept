---
id: apache-airflow-reproducing-task-instance-heartbeat-timeouts-locally-dda6bf43
type: concept
title: Reproducing task instance heartbeat timeouts locally
description: 'If you’d like to reproduce task instance heartbeat timeouts for development/testing
  processes, follow the steps below:'
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/tasks.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Reproducing task instance heartbeat timeouts locally

If you’d like to reproduce task instance heartbeat timeouts for development/testing processes, follow the steps below:

1. Set the below environment variables for your local Airflow setup (alternatively you could tweak the corresponding config values in airflow.cfg)

```
export AIRFLOW__SCHEDULER__TASK_INSTANCE_HEARTBEAT_SEC=600
export AIRFLOW__SCHEDULER__TASK_INSTANCE_HEARTBEAT_TIMEOUT=2
export AIRFLOW__SCHEDULER__TASK_INSTANCE_HEARTBEAT_TIMEOUT_DETECTION_INTERVAL=5
```

2. Have a Dag with a task that takes about 10 minutes to complete(i.e. a long-running task). For example, you could use the below Dag:

```
from airflow.sdk import dag
from airflow.providers.standard.operators.bash import BashOperator
from datetime import datetime


@dag(start_date=datetime(2021, 1, 1), schedule="@once", catchup=False)
def sleep_dag():
    t1 = BashOperator(
        task_id="sleep_10_minutes",
        bash_command="sleep 600",
    )


sleep_dag()
```

Run the above Dag and wait for a while. The `TaskInstance` will be marked failed after <task\_instance\_heartbeat\_timeout> seconds.