---
id: apache-airflow-navigate-7705fccf
type: concept
title: '`↑↓` Navigate'
description: '`↑↓` Navigate'
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/operators-and-hooks-ref.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

`↑↓` Navigate
`⏎` Select
`Esc` Close



# Operators and Hooks Reference

Here’s the list of the operators and hooks which are available in this release.

Note that commonly used operators and sensors (such as `BashOperator`, `PythonOperator`, `ExternalTaskSensor`, etc.) are provided by the `apache-airflow-providers-standard` package.

Airflow has many more integrations available for separate installation as
[Providers](https://airflow.apache.org/docs/apache-airflow-providers/index.html "(in apache-airflow-providers vstable)").

For details see: [Operators and Hooks Reference](https://airflow.apache.org/docs/apache-airflow-providers/operators-and-hooks-ref/index.html "(in apache-airflow-providers vstable)").

**Base:**

| Module | Guides |
| --- | --- |
| [`airflow.hooks.base`](https://airflow.apache.org/docs/apache-airflow/stable/_api/airflow/hooks/base/index.html#module-airflow.hooks.base "airflow.hooks.base") |  |
| `airflow.models.baseoperator` |  |
| `airflow.sensors.base` |  |

**Operators:**

| Operators | Guides |
| --- | --- |
| [`airflow.providers.standard.operators.bash`](https://airflow.apache.org/docs/apache-airflow-providers-standard/stable/_api/airflow/providers/standard/operators/bash/index.html#module-airflow.providers.standard.operators.bash "(in apache-airflow-providers-standard v1.17.0)") | [How to use](https://airflow.apache.org/docs/apache-airflow-providers-standard/stable/operators/bash.html "(in apache-airflow-providers-standard v1.17.0)") |
| [`airflow.providers.standard.operators.python`](https://airflow.apache.org/docs/apache-airflow-providers-standard/stable/_api/airflow/providers/standard/operators/python/index.html#module-airflow.providers.standard.operators.python "(in apache-airflow-providers-standard v1.17.0)") | [How to use](https://airflow.apache.org/docs/apache-airflow-providers-standard/stable/operators/python.html "(in apache-airflow-providers-standard v1.17.0)") |
| [`airflow.providers.standard.operators.datetime`](https://airflow.apache.org/docs/apache-airflow-providers-standard/stable/_api/airflow/providers/standard/operators/datetime/index.html#module-airflow.providers.standard.operators.datetime "(in apache-airflow-providers-standard v1.17.0)") | [How to use](https://airflow.apache.org/docs/apache-airflow-providers-standard/stable/operators/datetime.html "(in apache-airflow-providers-standard v1.17.0)") |
| [`airflow.providers.standard.operators.empty`](https://airflow.apache.org/docs/apache-airflow-providers-standard/stable/_api/airflow/providers/standard/operators/empty/index.html#module-airflow.providers.standard.operators.empty "(in apache-airflow-providers-standard v1.17.0)") |  |
| [`airflow.providers.common.sql.operators.generic_transfer.GenericTransfer`](https://airflow.apache.org/docs/apache-airflow-providers-common-sql/stable/_api/airflow/providers/common/sql/operators/generic_transfer/index.html#airflow.providers.common.sql.operators.generic_transfer.GenericTransfer "(in apache-airflow-providers-common-sql v2.1.0)") | [How to use](https://airflow.apache.org/docs/apache-airflow-providers-common-sql/stable/operators.html "(in apache-airflow-providers-common-sql v2.1.0)") |
| [`airflow.providers.standard.operators.latest_only`](https://airflow.apache.org/docs/apache-airflow-providers-standard/stable/_api/airflow/providers/standard/operators/latest_only/index.html#module-airflow.providers.standard.operators.latest_only "(in apache-airflow-providers-standard v1.17.0)") | [How to use](https://airflow.apache.org/docs/apache-airflow-providers-standard/stable/operators/latest_only.html "(in apache-airflow-providers-standard v1.17.0)") |
| [`airflow.providers.standard.operators.trigger_dagrun`](https://airflow.apache.org/docs/apache-airflow-providers-standard/stable/_api/airflow/providers/standard/operators/trigger_dagrun/index.html#module-airflow.providers.standard.operators.trigger_dagrun "(in apache-airflow-providers-standard v1.17.0)") | [How to use](https://airflow.apache.org/doc