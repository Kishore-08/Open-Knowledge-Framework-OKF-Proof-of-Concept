---
id: apache-airflow-environment-variables-5b0ecd17
type: concept
title: Environment Variables
description: AIRFLOW\_\_{SECTION}\_\_{KEY}
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/cli-and-env-variables-ref.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Environment Variables

AIRFLOW\_\_{SECTION}\_\_{KEY}
:   Sets options in the Airflow configuration. This takes priority over the value in the `airflow.cfg` file.

    Replace the `{SECTION}` placeholder with any section
    and the `{KEY}` placeholder with any key in that specified section.

    For example, if you want to set the `dags_folder` options in `[core]` section,
    then you should set the `AIRFLOW__CORE__DAGS_FOLDER` environment variable.

    For more information, see: [Setting Configuration Options](https://airflow.apache.org/docs/apache-airflow/stable/howto/set-config.html).

AIRFLOW\_\_{SECTION}\_\_{KEY}\_CMD
:   For any specific key in a section in Airflow, execute the command the key is pointing to.
    The result of the command is used as a value of the `AIRFLOW__{SECTION}__{KEY}` environment variable.

    This is only supported by the following config options:

- `sql_alchemy_conn` in `[database]` section
- `fernet_key` in `[core]` section
- `broker_url` in `[celery]` section
- `flower_basic_auth` in `[celery]` section
- `result_backend` in `[celery]` section
- `password` in `[atlas]` section
- `smtp_password` in `[smtp]` section
- `secret_key` in `[api]` section

AIRFLOW\_\_{SECTION}\_\_{KEY}\_SECRET
:   For any specific key in a section in Airflow, retrieve the secret from the configured secrets backend.
    The returned value will be used as the value of the `AIRFLOW__{SECTION}__{KEY}` environment variable.

    See [Secrets Backends](https://airflow.apache.org/docs/apache-airflow/stable/security/secrets/secrets-backend/index.html#secrets-backend-configuration) for more information on available secrets backends.

    This form of environment variable configuration is only supported for the same subset of config options as `AIRFLOW__{SECTION}__{KEY}_CMD`

AIRFLOW\_CONFIG
:   The path to the Airflow configuration file.

AIRFLOW\_CONN\_{CONN\_ID}
:   Defines a new connection with the name `{CONN_ID}` using the URI value.

    For example, if you want to create a connection named `PROXY_POSTGRES_TCP`, you can create
    a key `AIRFLOW_CONN_PROXY_POSTGRES_TCP` with the connection URI as the value.

    For more information, see: [Storing connections in environment variables](https://airflow.apache.org/docs/apache-airflow/stable/howto/connection.html#environment-variables-connections).

AIRFLOW\_HOME
:   The root directory for the Airflow content.
    This is the default parent directory for Airflow assets such as Dags and logs.

AIRFLOW\_VAR\_{KEY}
:   Defines an Airflow variable.
    Replace the `{KEY}` placeholder with the variable name.

    For more information, see: [Managing Variables](https://airflow.apache.org/docs/apache-airflow/stable/howto/variable.html#managing-variables).

Was this entry helpful?