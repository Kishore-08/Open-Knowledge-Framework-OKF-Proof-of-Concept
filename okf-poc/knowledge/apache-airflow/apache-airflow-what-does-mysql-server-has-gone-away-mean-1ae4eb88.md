---
id: apache-airflow-what-does-mysql-server-has-gone-away-mean-1ae4eb88
type: concept
title: What does “MySQL Server has gone away” mean?
description: You may occasionally experience `OperationalError` with the message “MySQL
  Server has gone away”. This is due to the
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/faq.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### What does “MySQL Server has gone away” mean?

You may occasionally experience `OperationalError` with the message “MySQL Server has gone away”. This is due to the
connection pool keeping connections open too long and you are given an old connection that has expired. To ensure a
valid connection, you can set [sql\_alchemy\_pool\_recycle](https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html#config-database-sql-alchemy-pool-recycle) to ensure connections are invalidated after
that many seconds and new ones are created.