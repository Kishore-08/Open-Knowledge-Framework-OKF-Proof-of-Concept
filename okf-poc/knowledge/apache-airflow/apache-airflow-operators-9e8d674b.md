---
id: apache-airflow-operators-9e8d674b
type: concept
title: Operators
description: The base classes [`BaseOperator`](https://airflow.apache.org/docs/task-sdk/stable/api.html#airflow.sdk.BaseOperator
  "(in Apache Airflow Task SDK v1.4.0)") and [`BaseSensorOperator`](https://airflow.ap
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/public-airflow-interface.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Operators

The base classes [`BaseOperator`](https://airflow.apache.org/docs/task-sdk/stable/api.html#airflow.sdk.BaseOperator "(in Apache Airflow Task SDK v1.4.0)") and [`BaseSensorOperator`](https://airflow.apache.org/docs/task-sdk/stable/api.html#airflow.sdk.BaseSensorOperator "(in Apache Airflow Task SDK v1.4.0)") are public and may be extended to make new operators.

The base class for new operators is [`BaseOperator`](https://airflow.apache.org/docs/task-sdk/stable/api.html#airflow.sdk.BaseOperator "(in Apache Airflow Task SDK v1.4.0)")
from the airflow.sdk namespace.

Subclasses of BaseOperator which are published in Apache Airflow are public in *behavior* but not in *structure*. That is to say, the Operator’s parameters and behavior is governed by semver but the methods are subject to change at any time.