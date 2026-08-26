---
id: apache-airflow-why-does-my-dag-version-keep-increasing-1ae4eb88
type: concept
title: Why does my Dag version keep increasing?
description: Every time the Dag processor parses a Dag file, it serializes the Dag
  and compares the result with the
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/faq.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Why does my Dag version keep increasing?

Every time the Dag processor parses a Dag file, it serializes the Dag and compares the result with the
version stored in the metadata database. If anything has changed, Airflow creates a new Dag version.

**Dag version inflation** occurs when the version number increases indefinitely without the Dag author
making any intentional changes.

#### What goes wrong

When Dag versions increase without meaningful changes:

- The metadata database accumulates unnecessary Dag version records, increasing storage and query overhead.
- The UI shows a misleading history of Dag changes, making it harder to identify real modifications.
- The scheduler and API server may consume more memory as they load and cache a growing number of Dag versions.

#### Common causes

Version inflation is caused by using values that change at **parse time** — that is, every time the Dag
processor evaluates the Dag file — as arguments to Dag or Task constructors. The most common patterns are:

**1. Using ``datetime.now()`` or ``pendulum.now()`` as ``start\_date``:**

```
from datetime import datetime

from airflow.sdk import DAG

with DAG(
    dag_id="bad_example",
    # BAD: datetime.now() produces a different value on every parse
    start_date=datetime.now(),
    schedule="@daily",
):
    ...
```

Every parse produces a different `start_date`, so the serialized Dag is always different from the
stored version.

**2. Using random values in Dag or Task arguments:**

```
import random

from airflow.sdk import DAG
from airflow.providers.standard.operators.python import PythonOperator

with DAG(dag_id="bad_random", start_date="2024-01-01", schedule="@daily") as dag:
    PythonOperator(
        # BAD: random value changes every parse
        task_id=f"task_{random.randint(1, 1000)}",
        python_callable=lambda: None,
    )
```

**3. Assigning runtime-varying values to variables used in constructors:**

```
from datetime import datetime

from airflow.sdk import DAG
from airflow.providers.standard.operators.python import PythonOperator

# BAD: the variable captures a parse-time value, then is passed to the DAG
default_args = {"start_date": datetime.now()}

with DAG(dag_id="bad_defaults", default_args=default_args, schedule="@daily") as dag:
    PythonOperator(task_id="my_task", python_callable=lambda: None)
```

Even though `datetime.now()` is not called directly inside the Dag constructor, it flows in through
`default_args` and still causes a different serialized Dag on every parse.

**4. Using environment variables or file contents that change between parses:**

```
import os

from airflow.sdk import DAG
from airflow.providers.standard.operators.bash import BashOperator

with DAG(dag_id="bad_env", start_date="2024-01-01", schedule="@daily") as dag:
    BashOperator(
        task_id="echo_build",
        # BAD if BUILD_NUMBER changes on every deployment or parse
        bash_command=f"echo {os.environ.get('BUILD_NUMBER', 'unknown')}",
    )
```

#### How to avoid version inflation

- **Use fixed ``start\_date`` values.** Always set `start_date` to a static `datetime` literal:

  ```
  import datetime

  from airflow.sdk import DAG

  with DAG(
      dag_id="good_example",
      start_date=datetime.datetime(2024, 1, 1),
      schedule="@daily",
  ):
      ...
  ```
- **Keep all Dag and Task constructor arguments deterministic.** Arguments passed to Dag and Operator
  constructors must produce the same value on every parse. Move any dynamic computation into the
  `execute()` method or use Jinja templates, which are evaluated at task execution time rather than
  parse time.
- **Use Jinja templates for dynamic values:**

  ```
  from airflow.providers.standard.operators.bash import BashOperator

  BashOperator(
      task_id="echo_date",
      # GOOD: the template is resolved at execution time, not parse time
      bash_command="echo {{ ds }}",
  )
  ```
- **Use Airflow Variables with templates instead of top-level lookup