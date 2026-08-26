---
id: apache-airflow-top-level-python-code-8dafd1cd
type: concept
title: Top level Python Code
description: You should avoid writing the top level code which is not necessary to
  create Operators
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/best-practices.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Top level Python Code

You should avoid writing the top level code which is not necessary to create Operators
and build Dag relations between them. This is because of the design decision for the scheduler of Airflow
and the impact the top-level code parsing speed on both performance and scalability of Airflow.

Airflow scheduler executes the code outside the Operator’s `execute` methods with the minimum interval of
[min\_file\_process\_interval](https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html#config-dag-processor-min-file-process-interval) seconds. This is done in order
to allow dynamic scheduling of the Dags - where scheduling and dependencies might change over time and
impact the next schedule of the Dag. Airflow scheduler tries to continuously make sure that what you have
in Dags is correctly reflected in scheduled tasks.

Specifically you should not run any database access, heavy computations and networking operations.

One of the important factors impacting Dag loading time, that might be overlooked by Python developers is
that top-level imports might take surprisingly a lot of time and they can generate a lot of overhead
and this can be easily avoided by converting them to local imports inside Python callables for example.

Consider the two examples below. In the first example, Dag will take an additional 1000 seconds to parse
than the functionally equivalent Dag in the second example where the `expensive_api_call` is executed from the context of its task.

Not avoiding top-level Dag code:

```
import pendulum

from airflow.sdk import DAG
from airflow.sdk import task


def expensive_api_call():
    print("Hello from Airflow!")
    sleep(1000)


my_expensive_response = expensive_api_call()

with DAG(
    dag_id="example_python_operator",
    schedule=None,
    start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
    catchup=False,
    tags=["example"],
) as dag:

    @task()
    def print_expensive_api_call():
        print(my_expensive_response)
```

Avoiding top-level Dag code:

```
import pendulum

from airflow.sdk import DAG
from airflow.sdk import task


def expensive_api_call():
    sleep(1000)
    return "Hello from Airflow!"


with DAG(
    dag_id="example_python_operator",
    schedule=None,
    start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
    catchup=False,
    tags=["example"],
) as dag:

    @task()
    def print_expensive_api_call():
        my_expensive_response = expensive_api_call()
        print(my_expensive_response)
```

In the first example, `expensive_api_call` is executed each time the Dag file is parsed, which will result in suboptimal performance in the Dag file processing. In the second example, `expensive_api_call` is only called when the task is running and thus is able to be parsed without suffering any performance hits. To test it out yourself, implement the first Dag and see “Hello from Airflow!” printed in the scheduler logs!

Note that import statements also count as top-level code. So, if you have an import statement that takes a long time or the imported module itself executes code at the top-level, that can also impact the performance of the scheduler. The following example illustrates how to handle expensive imports.

```
# It's ok to import modules that are not expensive to load at top-level of a Dag file
import random
import pendulum

# Expensive imports should be avoided as top level imports, because Dag files are parsed frequently, resulting in top-level code being executed.
#
# import pandas
# import torch
# import tensorflow
#

...


@task()
def do_stuff_with_pandas_and_torch():
    import pandas
    import torch

    # do some operations using pandas and torch


@task()
def do_stuff_with_tensorflow():
    import tensorflow

    # do some operations using tensorflow
```