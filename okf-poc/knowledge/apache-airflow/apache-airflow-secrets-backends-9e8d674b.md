---
id: apache-airflow-secrets-backends-9e8d674b
type: concept
title: Secrets Backends
description: Airflow can be configured to rely on secrets backends to retrieve
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/public-airflow-interface.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Secrets Backends

Airflow can be configured to rely on secrets backends to retrieve
[`Connection`](https://airflow.apache.org/docs/task-sdk/stable/api.html#airflow.sdk.Connection "(in Apache Airflow Task SDK v1.4.0)") and [`Variable`](https://airflow.apache.org/docs/task-sdk/stable/api.html#airflow.sdk.Variable "(in Apache Airflow Task SDK v1.4.0)").
All secrets backends derive from [`BaseSecretsBackend`](https://airflow.apache.org/docs/apache-airflow/stable/_api/airflow/secrets/base_secrets/index.html#airflow.secrets.base_secrets.BaseSecretsBackend "airflow.secrets.base_secrets.BaseSecretsBackend").

All Secrets Backend implementations are public. You can extend their functionality:

- [airflow.secrets](https://airflow.apache.org/docs/apache-airflow/stable/_api/airflow/secrets/index.html)

You can read more about Secret Backends in [Secrets Backend](https://airflow.apache.org/docs/apache-airflow/stable/security/secrets/secrets-backend/index.html).
You can also find all the available Secrets Backends implemented in community providers
in [Secret backends](https://airflow.apache.org/docs/apache-airflow-providers/core-extensions/secrets-backends.html "(in apache-airflow-providers vstable)").