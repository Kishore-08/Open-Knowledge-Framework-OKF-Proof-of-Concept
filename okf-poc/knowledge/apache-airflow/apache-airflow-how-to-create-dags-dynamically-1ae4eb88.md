---
id: apache-airflow-how-to-create-dags-dynamically-1ae4eb88
type: concept
title: How to create Dags dynamically?
description: Airflow looks in your `DAGS_FOLDER` for modules that contain `DAG` objects
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/faq.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### How to create Dags dynamically?

Airflow looks in your `DAGS_FOLDER` for modules that contain `DAG` objects
in their global namespace and adds the objects it finds in the
`DagBag`. Knowing this, all we need is a way to dynamically assign
variable in the global namespace. This is easily done in python using the
`globals()` function for the standard library, which behaves like a
simple dictionary.

```
def create_dag(dag_id):
    """
    A function returning a DAG object.
    """

    return DAG(dag_id)


for i in range(10):
    dag_id = f"foo_{i}"
    globals()[dag_id] = DAG(dag_id)

    # or better, call a function that returns a DAG object!
    other_dag_id = f"bar_{i}"
    globals()[other_dag_id] = create_dag(other_dag_id)
```

Even though Airflow supports multiple Dag definition per python file, dynamically generated or otherwise, it is not
recommended as Airflow would like better isolation between Dags from a fault and deployment perspective and multiple
Dags in the same file goes against that.