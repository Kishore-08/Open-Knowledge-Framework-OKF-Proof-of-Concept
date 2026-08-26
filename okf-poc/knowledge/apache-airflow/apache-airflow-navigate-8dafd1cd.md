---
id: apache-airflow-navigate-8dafd1cd
type: concept
title: '`↑↓` Navigate'
description: '`↑↓` Navigate'
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/best-practices.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

`↑↓` Navigate
`⏎` Select
`Esc` Close



# Best Practices

Creating a new Dag is a three-step process:

- writing Python code to create a Dag object,
- testing if the code meets your expectations,
- configuring environment dependencies to run your Dag

This tutorial will introduce you to the best practices for these three steps.

## Writing a Dag

Creating a new Dag in Airflow is quite simple. However, there are many things that you need to take care of
to ensure the Dag run or failure does not produce unexpected results.

### Creating a Custom Operator/Hook

Please follow our guide on [custom Operators](https://airflow.apache.org/docs/apache-airflow/stable/howto/custom-operator.html#custom-operator).