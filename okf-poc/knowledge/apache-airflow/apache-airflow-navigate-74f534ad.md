---
id: apache-airflow-navigate-74f534ad
type: concept
title: '`↑↓` Navigate'
description: '`↑↓` Navigate'
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/database-erd-ref.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

`↑↓` Navigate
`⏎` Select
`Esc` Close



# ERD Schema of the Database

Here is the current Database schema diagram.

Warning

The ER diagram shows the snapshot of the database structure valid for Airflow version 3.3.1 and it
should be treated as an internal detail. It might be changed at any time and you should not directly
access the database to retrieve information from it or modify the data - you should use
[Airflow public REST API reference](https://airflow.apache.org/docs/apache-airflow/stable/stable-rest-api-ref.html) to do that instead.
The main purpose of this diagram is to help with troubleshooting and understanding of the
internal Airflow DB architecture in case you have any problems with the database - for example
when dealing with problems with migrations. See also [Reference for Database Migrations](https://airflow.apache.org/docs/apache-airflow/stable/migrations-ref.html) for
list of detailed database migrations that are applied when running migration script and
[db command](https://airflow.apache.org/docs/apache-airflow/stable/cli-and-env-variables-ref.html#db) for the commands that you can use to manage
the migrations.

![_images/airflow_erd.svg](https://airflow.apache.org/docs/apache-airflow/stable/_images/airflow_erd.svg)

Was this entry helpful?