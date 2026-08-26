---
id: apache-airflow-relationships-dda6bf43
type: concept
title: Relationships
description: The key part of using Tasks is defining how they relate to each other
  - their *dependencies*, or as we say in Airflow, their *upstream* and *downstream*
  tasks. You declare your Tasks first, and then y
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/tasks.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Relationships

The key part of using Tasks is defining how they relate to each other - their *dependencies*, or as we say in Airflow, their *upstream* and *downstream* tasks. You declare your Tasks first, and then you declare their dependencies second.

Note

We call the *upstream* task the one that is directly preceding the other task. We used to call it a parent task before.
Be aware that this concept does not describe the tasks that are higher in the tasks hierarchy (i.e. they are not a direct parents of the task).
Same definition applies to *downstream* task, which needs to be a direct child of the other task.

There are two ways of declaring dependencies - using the `>>` and `<<` (bitshift) operators:

```
first_task >> second_task >> [third_task, fourth_task]
```

Or the more explicit `set_upstream` and `set_downstream` methods:

```
first_task.set_downstream(second_task)
third_task.set_upstream(second_task)
```

These both do exactly the same thing, but in general we recommend you use the bitshift operators, as they are easier to read in most cases.

By default, a Task will run when all of its upstream (parent) tasks have succeeded, but there are many ways of modifying this behaviour to add branching, to only wait for some upstream tasks, or to change behaviour based on where the current run is in history. For more, see [Control Flow](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/dags.html#concepts-control-flow).

Tasks don’t pass information to each other by default, and run entirely independently. If you want to pass information from one Task to another, you should use [XComs](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/xcoms.html).