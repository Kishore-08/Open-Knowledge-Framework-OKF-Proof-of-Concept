---
id: apache-airflow-metadata-db-maintenance-8dafd1cd
type: concept
title: Metadata DB maintenance
description: Over time, the metadata database will increase its storage footprint
  as more Dag and task runs and event logs accumulate.
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/best-practices.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Metadata DB maintenance

Over time, the metadata database will increase its storage footprint as more Dag and task runs and event logs accumulate.

You can use the Airflow CLI to purge old data with the command `airflow db clean`.

See [db clean usage](https://airflow.apache.org/docs/apache-airflow/stable/howto/usage-cli.html#cli-db-clean) for more details.

## Upgrades and downgrades

### Backup your database

It’s always a wise idea to backup the metadata database before undertaking any operation modifying the database.