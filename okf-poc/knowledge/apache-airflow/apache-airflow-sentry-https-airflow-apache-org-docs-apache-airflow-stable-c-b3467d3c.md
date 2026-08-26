---
id: apache-airflow-sentry-https-airflow-apache-org-docs-apache-airflow-stable-c-b3467d3c
type: concept
title: '[[sentry]](https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html#id31)'
description: '[Sentry](https://docs.sentry.io) integration. Here you can supply'
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### [[sentry]](https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html#id31)

[Sentry](https://docs.sentry.io) integration. Here you can supply
additional configuration options based on the Python platform.
See [Python / Configuration / Basic Options](https://docs.sentry.io/platforms/python/configuration/options/) for more details.
Unsupported options: `integrations`, `in_app_include`, `in_app_exclude`,
`ignore_errors`, `before_breadcrumb`, `transport`.

#### before\_send

> Added in version 2.2.0.

Dotted path to a before\_send function that the sentry SDK should be configured to use.

Type:
:   string

Default:
:   `None`

Environment Variable:
:   `AIRFLOW__SENTRY__BEFORE_SEND`

#### sentry\_dsn

> Added in version 1.10.6.

Type:
:   string

Default:
:   `''`

Environment Variables:
:   `AIRFLOW__SENTRY__SENTRY_DSN`

    `AIRFLOW__SENTRY__SENTRY_DSN_CMD`

    `AIRFLOW__SENTRY__SENTRY_DSN_SECRET`

#### sentry\_on

> Added in version 2.0.0.

Enable error reporting to Sentry

Type:
:   boolean

Default:
:   `false`

Environment Variable:
:   `AIRFLOW__SENTRY__SENTRY_ON`