---
id: apache-airflow-how-to-check-if-my-code-is-top-level-code-8dafd1cd
type: concept
title: How to check if my code is “top-level” code
description: In order to understand whether your code is “top-level” or not you need
  to understand a lot of
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/best-practices.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### How to check if my code is “top-level” code

In order to understand whether your code is “top-level” or not you need to understand a lot of
intricacies of how parsing Python works. In general, when Python parses the python file it executes
the code it sees, except (in general) internal code of the methods that it does not execute.

It has a number of special cases that are not obvious - for example top-level code also means
any code that is used to determine default values of methods.

However, there is an easy way to check whether your code is “top-level” or not. You simply need to
parse your code and see if the piece of code gets executed.

Imagine this code:

```
from airflow.sdk import DAG
from airflow.providers.standard.operators.python import PythonOperator
import pendulum


def get_task_id():
    return "print_array_task"  # <- is that code going to be executed?


def get_array():
    return [1, 2, 3]  # <- is that code going to be executed?


with DAG(
    dag_id="example_python_operator",
    schedule=None,
    start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
    catchup=False,
    tags=["example"],
) as dag:
    operator = PythonOperator(
        task_id=get_task_id(),
        python_callable=get_array,
        dag=dag,
    )
```

What you can do to check it is add some print statements to the code you want to check and then run
`python <my_dag_file>.py`.

```
from airflow.sdk import DAG
from airflow.providers.standard.operators.python import PythonOperator
import pendulum


def get_task_id():
    print("Executing 1")
    return "print_array_task"  # <- is that code going to be executed? YES


def get_array():
    print("Executing 2")
    return [1, 2, 3]  # <- is that code going to be executed? NO


with DAG(
    dag_id="example_python_operator",
    schedule=None,
    start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
    catchup=False,
    tags=["example"],
) as dag:
    operator = PythonOperator(
        task_id=get_task_id(),
        python_callable=get_array,
        dag=dag,
    )
```

When you execute that code you will see:

```
[Breeze:3.10.19] root@cf85ab34571e:/opt/airflow# python /files/test_python.py
Executing 1
```

This means that the `get_array` is not executed as top-level code, but `get_task_id` is.