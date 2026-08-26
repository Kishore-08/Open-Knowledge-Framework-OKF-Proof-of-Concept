---
id: apache-airflow-add-integration-test-dags-8dafd1cd
type: concept
title: Add “integration test” Dags
description: 'It can be helpful to add a couple “integration test” Dags that use all
  the common services in your ecosystem (e.g. S3, Snowflake, Vault) but with test
  resources or “dev” accounts. These test Dags can '
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/best-practices.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Add “integration test” Dags

It can be helpful to add a couple “integration test” Dags that use all the common services in your ecosystem (e.g. S3, Snowflake, Vault) but with test resources or “dev” accounts. These test Dags can be the ones you turn on *first* after an upgrade, because if they fail, it doesn’t matter and you can revert to your backup without negative consequences. However, if they succeed, they should prove that your cluster is able to run tasks with the libraries and services that you need to use.

For example, if you use an external secrets backend, make sure you have a task that retrieves a connection. If you use KubernetesPodOperator, add a task that runs `sleep 30; echo "hello"`. If you need to write to s3, do so in a test task. And if you need to access a database, add a task that does `select 1` from the server.