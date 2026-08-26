---
id: apache-airflow-code-a85da58d
type: concept
title: Code
description: Displays the Dag source code as it was at the time this run was parsed.
  This view is helpful for debugging version drift
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/ui.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Code

Displays the Dag source code as it was at the time this run was parsed. This view is helpful for debugging version drift
or comparing behavior across Dag Runs that used different code.

Dag Run code for `hello >> airflow()`:

![Dag Run Code Snapshot - airflow() (dark mode)](https://airflow.apache.org/docs/apache-airflow/stable/_images/dag_run_code_hello_airflow.png)
![Dag Run Code Snapshot - airflow() (light mode)](https://airflow.apache.org/docs/apache-airflow/stable/_images/dag_run_code_hello_airflow1.png)

Dag Run code for `hello >> world()`:

![Dag Run Code Snapshot - world() (dark mode)](https://airflow.apache.org/docs/apache-airflow/stable/_images/dag_run_code_hello_world.png)
![Dag Run Code Snapshot - world() (light mode)](https://airflow.apache.org/docs/apache-airflow/stable/_images/dag_run_code_hello_world1.png)