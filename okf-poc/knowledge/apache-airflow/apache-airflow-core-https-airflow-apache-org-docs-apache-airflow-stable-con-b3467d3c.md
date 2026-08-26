---
id: apache-airflow-core-https-airflow-apache-org-docs-apache-airflow-stable-con-b3467d3c
type: concept
title: '[[core]](https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html#id16)'
description: '> Added in version 3.3.0.'
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### [[core]](https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html#id16)

#### allow\_double\_dot\_in\_ids

> Added in version 3.3.0.

Allow `..` (consecutive dots) in DAG IDs and run IDs. By default, `..` is blocked to prevent
path traversal attacks. Set to `True` only if you have existing DAGs or runs whose IDs contain
`..` and cannot be renamed.

Type:
:   boolean

Default:
:   `False`

Environment Variable:
:   `AIRFLOW__CORE__ALLOW_DOUBLE_DOT_IN_IDS`

#### allowed\_deserialization\_classes

> Added in version 2.5.0.

Space-separated list of classes that may be imported during deserialization. Items can be glob
expressions. Python built-in classes (like dict) are always allowed.

Type:
:   string

Default:
:   `airflow.*`

Environment Variable:
:   `AIRFLOW__CORE__ALLOWED_DESERIALIZATION_CLASSES`

Example:
:   `airflow.* my_mod.my_other_mod.TheseClasses*`

#### allowed\_deserialization\_classes\_regexp

> Added in version 2.8.2.

Space-separated list of classes that may be imported during deserialization. Items are processed
as regex expressions and matched against the full classname (`re.fullmatch` semantics), so a
pattern such as `airflow\.models\.Variable` does not also admit `airflow.models.VariableXYZ`.
Use `.*` (e.g. `airflow\.models\..*`) to allow a prefix and any suffix. Python built-in
classes (like dict) are always allowed.
This is a secondary option to `[core] allowed_deserialization_classes`.

Type:
:   string

Default:
:   `''`

Environment Variable:
:   `AIRFLOW__CORE__ALLOWED_DESERIALIZATION_CLASSES_REGEXP`

#### asset\_manager\_class

> Added in version 3.0.0.

Class to use as asset manager.

Type:
:   string

Default:
:   `None`

Environment Variable:
:   `AIRFLOW__CORE__ASSET_MANAGER_CLASS`

Example:
:   `airflow.assets.manager.AssetManager`

#### asset\_manager\_kwargs

> Added in version 3.0.0.

Kwargs to supply to asset manager.

Type:
:   string

Default:
:   `None`

Environment Variables:
:   `AIRFLOW__CORE__ASSET_MANAGER_KWARGS`

    `AIRFLOW__CORE__ASSET_MANAGER_KWARGS_CMD`

    `AIRFLOW__CORE__ASSET_MANAGER_KWARGS_SECRET`

Example:
:   `{"some_param": "some_value"}`

#### auth\_manager

> Added in version 2.7.0.

The auth manager class that airflow should use. Full import path to the auth manager class.

Type:
:   string

Default:
:   `airflow.api_fastapi.auth.managers.simple.simple_auth_manager.SimpleAuthManager`

Environment Variable:
:   `AIRFLOW__CORE__AUTH_MANAGER`

#### compress\_serialized\_dags

> Added in version 2.3.0.

If `True`, serialized DAGs are compressed before writing to DB.

Note

This will disable the DAG dependencies view

Type:
:   boolean

Default:
:   `False`

Environment Variable:
:   `AIRFLOW__CORE__COMPRESS_SERIALIZED_DAGS`

#### daemon\_umask

> Added in version 2.3.4.

The default umask to use for process when run in daemon mode (scheduler, worker, etc.)

This controls the file-creation mode mask which determines the initial value of file permission bits
for newly created files.

This value is treated as an octal-integer.

Type:
:   string

Default:
:   `0o077`

Environment Variable:
:   `AIRFLOW__CORE__DAEMON_UMASK`

#### dag\_discovery\_safe\_mode

> Added in version 1.10.3.

If enabled, Airflow will only scan files containing both `DAG` and `airflow` (case-insensitive).

Type:
:   string

Default:
:   `True`

Environment Variable:
:   `AIRFLOW__CORE__DAG_DISCOVERY_SAFE_MODE`

#### dag\_ignore\_file\_syntax

> Added in version 2.3.0.

The pattern syntax used in the
[.airflowignore](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/dags.html#airflowignore)
files in the DAG directories. Valid values are `regexp` or `glob`.

Type:
:   string

Default:
:   `glob`

Environment Variable:
:   `AIRFLOW__CORE__DAG_IGNORE_FILE_SYNTAX`

#### dag\_run\_conf\_overrides\_params

Whether to override params with dag\_run.conf. If you pass some key-value pairs
through `airflow dags backfill -c` or
`airflow dags trigger -c`, the key-value pair