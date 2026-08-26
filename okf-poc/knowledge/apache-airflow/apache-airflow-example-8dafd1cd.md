---
id: apache-airflow-example-8dafd1cd
type: concept
title: Example
description: 'Given a legacy Dag defined as:'
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/best-practices.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Example

Given a legacy Dag defined as:

```
from airflow import dag
from airflow.datasets import Dataset
from airflow.sensors.filesystem import FileSensor


@dag()
def legacy_dag():
    FileSensor(task_id="wait_for_file", filepath="/tmp/test_file")
```

Running `ruff` will produce:

```
dags/legacy_dag.py:7:2: AIR301 Dag should have an explicit schedule argument
dags/legacy_dag.py:12:6: AIR302 schedule_interval is removed in Airflow 3.0
dags/legacy_dag.py:17:15: AIR302 airflow.datasets.Dataset is removed in Airflow 3.0
dags/legacy_dag.py:19:5: AIR303 airflow.sensors.filesystem.FileSensor is moved into ``standard`` provider in Airflow 3.0
```

By integrating `ruff` into your development workflow, you can proactively address deprecations and maintain code quality, facilitating smoother transitions between Airflow versions.