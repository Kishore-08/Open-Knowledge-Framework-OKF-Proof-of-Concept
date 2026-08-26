---
id: apache-airflow-navigate-a60aa04f
type: concept
title: '`↑↓` Navigate'
description: '`↑↓` Navigate'
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/migrations-ref.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

`↑↓` Navigate
`⏎` Select
`Esc` Close



# Reference for Database Migrations

Here’s the list of all the Database Migrations that are executed via when you run `airflow db migrate`.

Warning

> Those migration details are mostly used here to make the users aware when and what kind of migrations
> will be executed during migrations between specific Airflow versions. The intention here is that the
> “DB conscious” users might perform an analysis on the migrations and draw conclusions about the impact
> of the migrations on their Airflow database. Those users might also want to take a look at the
> [ERD Schema of the Database](https://airflow.apache.org/docs/apache-airflow/stable/database-erd-ref.html) document to understand how the internal DB of Airflow structure looks like.
> However, you should be aware that the structure is internal and you should not access the DB directly
> to retrieve or modify any data - you should use the [REST API](https://airflow.apache.org/docs/apache-airflow/stable/stable-rest-api-ref.html) to do that instead.

| Revision ID | Revises ID | Airflow Version | Description |
| --- | --- | --- | --- |
| `d2f4e1b3c5a7` (head) | `9ff64e1c35d3` | `3.3.0` | Add partition\_date to asset\_partition\_dag\_run. |
| `9ff64e1c35d3` | `dd5f3a8e2b91` | `3.3.0` | Add indexes on dag\_run.created\_dag\_version\_id and task\_instance.dag\_version\_id. |
| `dd5f3a8e2b91` | `c20871fbf23a` | `3.3.0` | Add rollup\_fingerprint to AssetPartitionDagRun and index partitioned\_asset\_key\_log.asset\_partition\_dag\_run\_id. |
| `c20871fbf23a` | `c9d4e5f6a7b8` | `3.3.0` | Add partition\_mapper\_info to DagModel. |
| `c9d4e5f6a7b8` | `a7e6d4c3b2f1` | `3.3.0` | Add allow\_consumer\_teams columns to task\_outlet\_asset\_reference table. |
| `a7e6d4c3b2f1` | `8812eb67b63c` | `3.3.0` | Add connection\_test\_request table for the deferred connection-test workflow. |
| `8812eb67b63c` | `acc215baed80` | `3.3.0` | Change Deadline interval to JSON. |
| `acc215baed80` | `a1b2c3d4e5f6` | `3.3.0` | Add team\_name to trigger table. |
| `a1b2c3d4e5f6` | `a7f3b2c1d4e5` | `3.3.0` | Add version\_data to dag\_version. |
| `a7f3b2c1d4e5` | `b8f3e4a1d2c9` | `3.3.0` | Add access control columns to dag\_schedule\_asset\_reference table. |
| `b8f3e4a1d2c9` | `fde9ed84d07b` | `3.3.0` | Add retry\_delay\_override and retry\_reason to task\_instance. |
| `fde9ed84d07b` | `9fabad868fdb` | `3.3.0` | Add task\_state\_store and asset\_state\_store tables. |
| `9fabad868fdb` | `a4c2d171ae18` | `3.3.0` | Add timetable\_periodic to DagModel. |
| `a4c2d171ae18` | `1d6611b6ab7c` | `3.3.0` | Add dag\_result to XComModel. |
| `1d6611b6ab7c` | `888b59e02a5b` | `3.2.0` | Add bundle\_name to callback table. |
| `888b59e02a5b` | `6222ce48e289` | `3.2.0` | Fix migration file ORM inconsistencies. |
| `6222ce48e289` | `134de42d3cb0` | `3.2.0` | Add partition fields to DagModel. |
| `134de42d3cb0` | `e42d9fcd10d9` | `3.2.0` | Add partition\_key to backfill\_dag\_run. |
| `e42d9fcd10d9` | `f8c9d7e6b5a4` | `3.2.0` | Add allowed\_run\_types to dag. |
| `f8c9d7e6b5a4` | `53ff648b8a26` | `3.2.0` | Standardize UUID column format for non-PostgreSQL databases. |
| `53ff648b8a26` | `a5a3e5eb9b8d` | `3.2.0` | Add revoked\_token table. |
| `a5a3e5eb9b8d` | `55297ae24532` | `3.2.0` | Make external\_executor\_id TEXT to allow for longer external\_executor\_ids. |
| `55297ae24532` | `e79fc784f145` | `3.2.0` | Add required fields to enable UI integrations for the Deadline Alerts feature. |
| `e79fc784f145` | `0b112f49112d` | `3.2.0` | Add timetable\_type to dag table for filtering. |
| `0b112f49112d` | `c47f2e1ab9d4` | `3.2.0` | Add exceeds max runs flag to dag model. |
| `c47f2e1ab9d4` | `edc4f85a4619` | `3.2.0` | Add `queue` column to `trigger` table. |
| `edc4f85a4619` | `b12d4f98a91e` | `3.2.0` | Enforce the new `NOT NULL` expectations for `log.event` and `dag.is_stale`. |
| `b12d4f98a91e` | `665854ef0536` | `3.2.0` | Drop `id` column from `team` table and make `name` the primary key. |