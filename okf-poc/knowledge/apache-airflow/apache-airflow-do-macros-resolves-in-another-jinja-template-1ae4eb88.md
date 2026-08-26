---
id: apache-airflow-do-macros-resolves-in-another-jinja-template-1ae4eb88
type: concept
title: Do Macros resolves in another Jinja template?
description: It is not possible to render [Macros](https://jinja.palletsprojects.com/en/3.1.x/templates/#macros
  "(in Jinja v3.1.x)") or any Jinja template within another Jinja template. This is
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/faq.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Do Macros resolves in another Jinja template?

It is not possible to render [Macros](https://jinja.palletsprojects.com/en/3.1.x/templates/#macros "(in Jinja v3.1.x)") or any Jinja template within another Jinja template. This is
commonly attempted in `user_defined_macros`.

```
dag = DAG(
    # ...
    user_defined_macros={"my_custom_macro": "day={{ ds }}"}
)

bo = BashOperator(task_id="my_task", bash_command="echo {{ my_custom_macro }}", dag=dag)
```

This will echo “day={{ ds }}” instead of “day=2020-01-01” for a Dag run with a
`data_interval_start` of 2020-01-01 00:00:00.

```
bo = BashOperator(task_id="my_task", bash_command="echo day={{ ds }}", dag=dag)
```

By using the ds macros directly in the template\_field, the rendered value results in “day=2020-01-01”.