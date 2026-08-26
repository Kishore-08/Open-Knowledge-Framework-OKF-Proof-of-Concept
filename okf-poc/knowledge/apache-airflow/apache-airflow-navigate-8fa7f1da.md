---
id: apache-airflow-navigate-8fa7f1da
type: concept
title: '`↑↓` Navigate'
description: '`↑↓` Navigate'
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/authoring-and-scheduling/index.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

`↑↓` Navigate
`⏎` Select
`Esc` Close



# Authoring and Scheduling

Here you can find detailed documentation about advanced authoring and scheduling Airflow Dags.
It’s recommended that you first review the pages in [core concepts](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/index.html)

**Authoring**

- [Deferrable Operators & Triggers](https://airflow.apache.org/docs/apache-airflow/stable/authoring-and-scheduling/deferring.html)
  - [Using Deferrable Operators](https://airflow.apache.org/docs/apache-airflow/stable/authoring-and-scheduling/deferring.html#using-deferrable-operators)
  - [Writing Deferrable Operators](https://airflow.apache.org/docs/apache-airflow/stable/authoring-and-scheduling/deferring.html#writing-deferrable-operators)
  - [High Availability](https://airflow.apache.org/docs/apache-airflow/stable/authoring-and-scheduling/deferring.html#high-availability)
  - [Difference between Mode=’reschedule’ and Deferrable=True in Sensors](https://airflow.apache.org/docs/apache-airflow/stable/authoring-and-scheduling/deferring.html#difference-between-mode-reschedule-and-deferrable-true-in-sensors)
- [Serialization](https://airflow.apache.org/docs/apache-airflow/stable/authoring-and-scheduling/serializers.html)
  - [Serialization resolution order](https://airflow.apache.org/docs/apache-airflow/stable/authoring-and-scheduling/serializers.html#serialization-resolution-order)
  - [Airflow Object](https://airflow.apache.org/docs/apache-airflow/stable/authoring-and-scheduling/serializers.html#airflow-object)
- [Connections & Hooks](https://airflow.apache.org/docs/apache-airflow/stable/authoring-and-scheduling/connections.html)
  - [Hooks](https://airflow.apache.org/docs/apache-airflow/stable/authoring-and-scheduling/connections.html#hooks)
  - [Custom connections](https://airflow.apache.org/docs/apache-airflow/stable/authoring-and-scheduling/connections.html#custom-connections)
- [Dynamic Task Mapping](https://airflow.apache.org/docs/apache-airflow/stable/authoring-and-scheduling/dynamic-task-mapping.html)
  - [Simple mapping](https://airflow.apache.org/docs/apache-airflow/stable/authoring-and-scheduling/dynamic-task-mapping.html#simple-mapping)
  - [Mapping with non-TaskFlow operators](https://airflow.apache.org/docs/apache-airflow/stable/authoring-and-scheduling/dynamic-task-mapping.html#mapping-with-non-taskflow-operators)
  - [Assigning multiple parameters to a non-TaskFlow operator](https://airflow.apache.org/docs/apache-airflow/stable/authoring-and-scheduling/dynamic-task-mapping.html#assigning-multiple-parameters-to-a-non-taskflow-operator)
  - [Mapping over a task group](https://airflow.apache.org/docs/apache-airflow/stable/authoring-and-scheduling/dynamic-task-mapping.html#mapping-over-a-task-group)
  - [Filtering items from a mapped task](https://airflow.apache.org/docs/apache-airflow/stable/authoring-and-scheduling/dynamic-task-mapping.html#filtering-items-from-a-mapped-task)
  - [Transforming expanding data](https://airflow.apache.org/docs/apache-airflow/stable/authoring-and-scheduling/dynamic-task-mapping.html#transforming-expanding-data)
  - [Combining upstream data (aka “zipping”)](https://airflow.apache.org/docs/apache-airflow/stable/authoring-and-scheduling/dynamic-task-mapping.html#combining-upstream-data-aka-zipping)
  - [Concatenating multiple upstreams](https://airflow.apache.org/docs/apache-airflow/stable/authoring-and-scheduling/dynamic-task-mapping.html#concatenating-multiple-upstreams)
  - [What data types can be expanded?](https://airflow.apache.org/docs/apache-airflow/stable/authoring-and-scheduling/dynamic-task-mapping.html#what-data-types-can-be-expanded)
  - [How do templated fields and mapped arguments interact?](https://airflow.apache.org/docs/apache-airflow/stable/authoring-and-scheduling/dynamic-task-mapping.html#how-do-templated-fields-and-mapped-arguments-interact)
  - [Placing limits on mapped tasks](https://airflow.apache.org/docs/apache-airflow/stable/authoring-and-