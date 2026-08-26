---
id: apache-airflow-relationship-terminology-dda6bf43
type: concept
title: Relationship Terminology
description: For any given Task Instance, there are two types of relationships it
  has with other instances.
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/tasks.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Relationship Terminology

For any given Task Instance, there are two types of relationships it has with other instances.

Firstly, it can have *upstream* and *downstream* tasks:

```
task1 >> task2 >> task3
```

When a Dag runs, it will create instances for each of these tasks that are upstream/downstream of each other, but which all have the same data interval.

There may also be instances of the *same task*, but for different data intervals - from other runs of the same Dag. We call these *previous* and *next* - it is a different relationship to *upstream* and *downstream*!

Note

Some older Airflow documentation may still use “previous” to mean “upstream”. If you find an occurrence of this, please help us fix it!