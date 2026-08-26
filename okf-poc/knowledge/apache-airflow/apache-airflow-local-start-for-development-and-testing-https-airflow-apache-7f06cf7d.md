---
id: apache-airflow-local-start-for-development-and-testing-https-airflow-apache-7f06cf7d
type: concept
title: '[Local start for development and testing](https://airflow.apache.org/docs/apache-airflow/stable/installation/index.html#id1)'
description: You just want to try Apache Airflow without all production complexity?
  If you have `pipx` installed,
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/installation/index.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## [Local start for development and testing](https://airflow.apache.org/docs/apache-airflow/stable/installation/index.html#id1)

You just want to try Apache Airflow without all production complexity? If you have `pipx` installed,
you can install Airflow directly from PyPI with the command below:

```
pipx run apache-airflow standalone
```

Alternatively similar with Astral `uv`:

```
uvx apache-airflow standalone
```

Which starts a minimal system with an auto-generated admin password and SQLite database, so you can
start using Airflow right away. This is a great way to get familiar with Airflow and try it out
without the need to set up a complex environment.

Note that the standalone mode is not for production purposes. But it is a simple start for a local development.