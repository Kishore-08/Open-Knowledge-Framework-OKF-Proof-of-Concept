---
id: apache-airflow-navigate-b3467d3c
type: concept
title: '`↑↓` Navigate'
description: '`↑↓` Navigate'
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

`↑↓` Navigate
`⏎` Select
`Esc` Close



# Configuration Reference

This page contains the list of all the available Airflow configurations that you
can set in `airflow.cfg` file or using environment variables.

Different Airflow components may require different configuration parameters, and for
improved security, you should restrict sensitive configuration to only the components that
need it. Some configuration values must be shared across specific components to work
correctly — for example, the JWT signing key (`[api_auth] jwt_secret` or
`[api_auth] jwt_private_key_path`) must be consistent across all components that generate
or validate JWT tokens (Scheduler, API Server). However, other sensitive parameters such as
database connection strings or Fernet keys should only be provided to components that need them.

For security-sensitive deployments, pass configuration values via environment variables
scoped to individual components rather than sharing a single configuration file across all
components. See [Airflow Security Model](https://airflow.apache.org/docs/apache-airflow/stable/security/security_model.html) for details on which configuration
parameters should be restricted to which components.

Make sure that time on ALL the machines that you run Airflow components on is synchronized
(for example using ntpd) otherwise you might get “forbidden” errors when the logs are
accessed or API calls are made.

Note

For more information see [Setting Configuration Options](https://airflow.apache.org/docs/apache-airflow/stable/howto/set-config.html).