---
id: apache-airflow-core-airflow-extras-f586a1ea
type: concept
title: Core Airflow extras
description: These are core Airflow extras that extend capabilities of core Airflow.
  They do not install provider
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/extra-packages-ref.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Core Airflow extras

These are core Airflow extras that extend capabilities of core Airflow. They do not install provider
packages, they just install necessary
python dependencies for the provided package. The same extras are available as `airflow-core` package extras.

| extra | install command | enables |
| --- | --- | --- |
| async | `pip install 'apache-airflow[async]'` | Async worker classes for Gunicorn |
| graphviz | `pip install 'apache-airflow[graphviz]'` | Graphviz renderer for converting Dag to graphical output |
| kerberos | `pip install 'apache-airflow[kerberos]'` | Kerberos integration for Kerberized services (Hadoop, Presto, Trino) |
| memray | `pip install 'apache-airflow[memray]'` | Required for memory profiling with memray |
| otel | `pip install 'apache-airflow[otel]'` | Required for OpenTelemetry metrics |
| sentry | `pip install 'apache-airflow[sentry]'` | Sentry service for application logging and monitoring |
| standard | `pip install apache-airflow[standard]'` | Standard hooks and operators |
| statsd | `pip install 'apache-airflow[statsd]'` | Needed by StatsD metrics |