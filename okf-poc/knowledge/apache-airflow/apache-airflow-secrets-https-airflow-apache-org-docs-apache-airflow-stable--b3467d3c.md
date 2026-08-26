---
id: apache-airflow-secrets-https-airflow-apache-org-docs-apache-airflow-stable--b3467d3c
type: concept
title: '[[secrets]](https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html#id29)'
description: '> Added in version 1.10.10.'
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### [[secrets]](https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html#id29)

#### backend

> Added in version 1.10.10.

Full class name of secrets backend to enable (will precede env vars and metastore in search path)

Type:
:   string

Default:
:   `''`

Environment Variable:
:   `AIRFLOW__SECRETS__BACKEND`

Example:
:   `airflow.providers.amazon.aws.secrets.systems_manager.SystemsManagerParameterStoreBackend`

#### backend\_kwargs

> Added in version 1.10.10.

The backend\_kwargs param is loaded into a dictionary and passed to `__init__`
of secrets backend class. See documentation for the secrets backend you are using.
JSON is expected.

Example for AWS Systems Manager ParameterStore:
`{"connections_prefix": "/airflow/connections", "profile_name": "default"}`

You can also set individual kwargs via `AIRFLOW__SECRETS__BACKEND_KWARG__<KEY>=value`
environment variables. Per-key variables override the same key in this JSON setting.
Values are raw strings (not JSON-parsed).

Type:
:   string

Default:
:   `''`

Environment Variables:
:   `AIRFLOW__SECRETS__BACKEND_KWARGS`

    `AIRFLOW__SECRETS__BACKEND_KWARGS_CMD`

    `AIRFLOW__SECRETS__BACKEND_KWARGS_SECRET`

#### cache\_ttl\_seconds

> Added in version 2.7.0.

Note

This is an [experimental feature](https://airflow.apache.org/docs/apache-airflow/stable/release-process.html#experimental).

When the cache is enabled, this is the duration for which we consider an entry in the cache to be
valid. Entries are refreshed if they are older than this many seconds.
It means that when the cache is enabled, this is the maximum amount of time you need to wait to see a
Variable change take effect.

Type:
:   integer

Default:
:   `900`

Environment Variable:
:   `AIRFLOW__SECRETS__CACHE_TTL_SECONDS`

#### use\_cache

> Added in version 2.7.0.

Note

This is an [experimental feature](https://airflow.apache.org/docs/apache-airflow/stable/release-process.html#experimental).

Enables local caching of Variables, when parsing DAGs only.
Using this option can make dag parsing faster if Variables are used in top level code, at the expense
of longer propagation time for changes.
Please note that this cache concerns only the DAG parsing step. There is no caching in place when DAG
tasks are run.

Type:
:   boolean

Default:
:   `False`

Environment Variable:
:   `AIRFLOW__SECRETS__USE_CACHE`