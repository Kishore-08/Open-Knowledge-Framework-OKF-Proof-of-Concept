---
id: apache-airflow-dags-9acbc545
type: concept
title: Dags
description: 'A Dag is a model that encapsulates everything needed to execute a workflow.
  Some Dag attributes include the following:'
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/index.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Dags

A Dag is a model that encapsulates everything needed to execute a workflow. Some Dag attributes include the following:

- **Schedule**: When the workflow should run.
- **Tasks**: [tasks](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/tasks.html) are discrete units of work that are run on workers.
- **Task Dependencies**: The order and conditions under which [tasks](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/tasks.html) execute.
- **Callbacks**: Actions to take when the entire workflow completes.
- **Additional Parameters**: And many other operational details.

Let’s look at a code snippet that defines a simple Dag:

```
from datetime import datetime

from airflow.sdk import DAG, task
from airflow.providers.standard.operators.bash import BashOperator

# A Dag represents a workflow, a collection of tasks
with DAG(dag_id="demo", start_date=datetime(2022, 1, 1), schedule="0 0 * * *") as dag:
    # Tasks are represented as operators
    hello = BashOperator(task_id="hello", bash_command="echo hello")

    @task()
    def airflow():
        print("airflow")

    # Set dependencies between tasks
    hello >> airflow()
```

Here you see:

- A Dag named `"demo"`, scheduled to run daily starting on January 1st, 2022. A Dag is how Airflow represents a workflow.
- Two tasks: One using a `BashOperator` to run a shell script, and another using the `@task` decorator to define a Python function.
- The `>>` operator defines a dependency between the two tasks and controls execution order.

Airflow parses the script, schedules the tasks, and executes them in the defined order. The status of the `"demo"` Dag
is displayed in the web interface:

![Demo Dag in the Graph View, showing the status of one Dag run along with Dag code.](https://airflow.apache.org/docs/apache-airflow/stable/_images/demo_graph_and_code_view.png)

This example uses a simple Bash command and Python function, but Airflow tasks can run virtually any code. You might use
tasks to run a Spark job, move files between storage buckets, or send a notification email. Here’s what that same Dag looks
like over time, with multiple runs:

![Demo Dag in the Grid View, showing the status of all Dag runs, as well as logs for a task instance](https://airflow.apache.org/docs/apache-airflow/stable/_images/demo_grid_view_with_task_logs.png)

Each column in the grid represents a single Dag run. While the graph and grid views are most commonly used, Airflow provides
several other views to help you monitor and troubleshoot workflows — such as the `Dag Overview` view:

![Overview of a complex Dag in the Grid View, showing the status of all Dag runs, as well as quick links to recently failed task logs](https://airflow.apache.org/docs/apache-airflow/stable/_images/demo_complex_dag_overview_with_failed_tasks.png)

Note

The term “DAG” comes from the mathematical concept “directed acyclic graph”, but the meaning in Airflow has evolved well beyond just the literal data structure associated with the mathematical DAG concept. Therefore it was decided to use the term Dag in Airflow.

# Why Airflow®?

Airflow is a platform for orchestrating batch workflows. It offers a flexible framework with a wide range of built-in operators
and makes it easy to integrate with new technologies.

If your workflows have a clear start and end and run on a schedule, they’re a great fit for Airflow Dags.

If you prefer coding over clicking, Airflow is built for you. Defining workflows as Python code provides several key benefits:

- **Version control**: Track changes, roll back to previous versions, and collaborate with your team.
- **Team collaboration**: Multiple developers can work on the same workflow codebase.
- **Testing**: Validate pipeline logic through unit and integration tests.
- **Extensibility**: Customize workflows using a large ecosystem of existing components — or build your own.

Airflow’s rich scheduling and execution semantics make it easy to define comple