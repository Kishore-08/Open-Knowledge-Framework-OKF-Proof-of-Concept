---
id: apache-airflow-prune-data-before-upgrading-8dafd1cd
type: concept
title: Prune data before upgrading
description: Some database migrations can be time-consuming. If your metadata database
  is very large, consider pruning some of the old data with the [db clean](https://airflow.apache.org/docs/apache-airflow/stable
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/best-practices.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Prune data before upgrading

Some database migrations can be time-consuming. If your metadata database is very large, consider pruning some of the old data with the [db clean](https://airflow.apache.org/docs/apache-airflow/stable/howto/usage-cli.html#cli-db-clean) command prior to performing the upgrade. *Use with caution.*