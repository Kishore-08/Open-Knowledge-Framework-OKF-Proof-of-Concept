---
id: apache-airflow-navigate-dda6bf43
type: concept
title: '`↑↓` Navigate'
description: '`↑↓` Navigate'
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/tasks.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

`↑↓` Navigate
`⏎` Select
`Esc` Close



# Tasks

A Task is the basic unit of execution in Airflow. Tasks are arranged into [Dags](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/dags.html), and then have upstream and downstream dependencies set between them in order to express the order they should run in.

There are three basic kinds of Task:

- [Operators](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/operators.html), predefined task templates that you can string together quickly to build most parts of your Dags.
- [Sensors](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/sensors.html), a special subclass of Operators which are entirely about waiting for an external event to happen.
- A [TaskFlow](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/taskflow.html)-decorated `@task`, which is a custom Python function packaged up as a Task.

Internally, these are all actually subclasses of Airflow’s `BaseOperator`, and the concepts of Task and Operator are somewhat interchangeable, but it’s useful to think of them as separate concepts - essentially, Operators and Sensors are *templates*, and when you call one in a Dag file, you’re making a Task.