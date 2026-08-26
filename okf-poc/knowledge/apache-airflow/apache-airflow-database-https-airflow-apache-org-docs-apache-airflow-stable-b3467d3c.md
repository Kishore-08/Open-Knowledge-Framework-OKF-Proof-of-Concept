---
id: apache-airflow-database-https-airflow-apache-org-docs-apache-airflow-stable-b3467d3c
type: concept
title: '[[database]](https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html#id18)'
description: '> Added in version 2.7.0.'
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### [[database]](https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html#id18)

#### alembic\_ini\_file\_path

> Added in version 2.7.0.

Path to the `alembic.ini` file. You can either provide the file path relative
to the Airflow home directory or the absolute path if it is located elsewhere.

Type:
:   string

Default:
:   `alembic.ini`

Environment Variable:
:   `AIRFLOW__DATABASE__ALEMBIC_INI_FILE_PATH`

#### check\_migrations

> Added in version 2.6.0.

Whether to run alembic migrations during Airflow start up. Sometimes this operation can be expensive,
and the users can assert the correct version through other means (e.g. through a Helm chart).
Accepts `True` or `False`.

Type:
:   string

Default:
:   `True`

Environment Variable:
:   `AIRFLOW__DATABASE__CHECK_MIGRATIONS`

#### external\_db\_managers

> Added in version 3.0.0.

Additional DB managers to include when migrating external tables in the Airflow
database, beyond those automatically discovered from installed providers.
The managers must inherit from BaseDBManager.

Type:
:   string

Default:
:   `None`

Environment Variable:
:   `AIRFLOW__DATABASE__EXTERNAL_DB_MANAGERS`

Example:
:   `airflow.providers.fab.auth_manager.models.db.FABDBManager`

#### max\_db\_retries

> Added in version 2.3.0.

Number of times the code should be retried in case of DB Operational Errors.
Not all transactions will be retried as it can cause undesired state.
Currently it is only used in `DagFileProcessor.process_file` to retry `dagbag.sync_to_db`.

Type:
:   integer

Default:
:   `3`

Environment Variable:
:   `AIRFLOW__DATABASE__MAX_DB_RETRIES`

#### migration\_batch\_size

> Added in version 3.0.0.

The number of rows to process in each batch when performing a migration.
This is useful for large tables to avoid locking and failure due to query timeouts.

Type:
:   integer

Default:
:   `10000`

Environment Variable:
:   `AIRFLOW__DATABASE__MIGRATION_BATCH_SIZE`

#### sql\_alchemy\_conn

> Added in version 2.3.0.

The SQLAlchemy connection string to the metadata database.
SQLAlchemy supports many different database engines.
See: [Set up a Database Backend: Database URI](https://airflow.apache.org/docs/apache-airflow/stable/howto/set-up-database.html#database-uri)
for more details.

Type:
:   string

Default:
:   `sqlite:///{AIRFLOW_HOME}/airflow.db`

Environment Variables:
:   `AIRFLOW__DATABASE__SQL_ALCHEMY_CONN`

    `AIRFLOW__DATABASE__SQL_ALCHEMY_CONN_CMD`

    `AIRFLOW__DATABASE__SQL_ALCHEMY_CONN_SECRET`

#### sql\_alchemy\_conn\_async

> Added in version 3.1.0.

The SQLAlchemy connection string to the metadata database used for async connections.
If this is not set, Airflow automatically derives a string by converting `sql_alchemy_conn`.
Unfortunately, this conversion logic does not always work due to various incompatibilities
between sync and async db driver implementations. This sets the connection string directly
without any conversion instead.

Type:
:   string

Default:
:   `None`

Environment Variables:
:   `AIRFLOW__DATABASE__SQL_ALCHEMY_CONN_ASYNC`

    `AIRFLOW__DATABASE__SQL_ALCHEMY_CONN_ASYNC_CMD`

    `AIRFLOW__DATABASE__SQL_ALCHEMY_CONN_ASYNC_SECRET`

Example:
:   `postgresql+asyncpg://postgres:airflow@postgres/airflow`

#### sql\_alchemy\_connect\_args

> Added in version 2.3.0.

Import path for connect args in SQLAlchemy. Defaults to an empty dict.
This is useful when you want to configure db engine args that SQLAlchemy won’t parse
in connection string. This can be set by passing a dictionary containing the create engine parameters.
For more details about passing create engine parameters (keepalives variables, timeout etc)
in Postgres DB Backend see [Setting up a PostgreSQL Database](https://airflow.apache.org/docs/apache-airflow/stable/howto/set-up-database.html#setting-up-a-postgresql-database)
e.g `connect_args={"timeout":30}` can be defined in `airflow_local_settings.py` and
can be imported as shown below

*Changed in 3.1.0*: This con