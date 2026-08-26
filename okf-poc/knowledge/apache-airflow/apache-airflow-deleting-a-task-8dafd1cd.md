---
id: apache-airflow-deleting-a-task-8dafd1cd
type: concept
title: Deleting a task
description: Be careful when deleting a task from a Dag. You would not be able to
  see the Task in Graph View, Grid View, etc making
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/best-practices.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Deleting a task

Be careful when deleting a task from a Dag. You would not be able to see the Task in Graph View, Grid View, etc making
it difficult to check the logs of that Task from the Webserver. If that is not desired, please create a new Dag.