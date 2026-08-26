---
id: apache-airflow-xcom-a85da58d
type: concept
title: XCom
description: Shows any values pushed via `XCom.push()` or returned from Python functions
  when using TaskFlow.
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/ui.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### XCom

Shows any values pushed via `XCom.push()` or returned from Python functions when using TaskFlow.

![Task Instance - XCom tab (dark mode)](https://airflow.apache.org/docs/apache-airflow/stable/_images/dag_run_task_instance_xcom.png)
![Task Instance - XCom tab (light mode)](https://airflow.apache.org/docs/apache-airflow/stable/_images/dag_run_task_instance_xcom1.png)

### Events

If present, displays relevant events related to this specific task instance execution.

### Code

Shows the Dag source code parsed at the time of execution. This helps verify what version of the Dag the task ran with.