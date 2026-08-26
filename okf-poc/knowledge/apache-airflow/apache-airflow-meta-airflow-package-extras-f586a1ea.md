---
id: apache-airflow-meta-airflow-package-extras-f586a1ea
type: concept
title: Meta-airflow package extras
description: Airflow 3 is released in several packages. The `apache-airflow` package
  is a meta-package that installs
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/extra-packages-ref.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Meta-airflow package extras

Airflow 3 is released in several packages. The `apache-airflow` package is a meta-package that installs
all the other packages when you run Airflow as a standalone installation, and it also has several extras
that are not extending Airflow core functionality, but they are useful for the users who want to install
other packages that can be used by airflow or some of its providers.

| extra | install command | enables |
| --- | --- | --- |
| aiobotocore | `pip install 'apache-airflow[aiobotocore]'` | Support for asynchronous (deferrable) operators for Amazon integration |
| amazon-aws-auth | `pip install apache-airflow[amazon-aws-auth]` | Amazon-aws-auth AWS authentication |
| cloudpickle | `pip install apache-airflow[cloudpickle]` | Cloudpickle hooks and operators |
| github-enterprise | `pip install 'apache-airflow[github-enterprise]'` | GitHub Enterprise auth backend |
| google-auth | `pip install 'apache-airflow[google-auth]'` | Google auth backend |
| graphviz | `pip install 'apache-airflow[graphviz]'` | Graphviz renderer for converting Dag to graphical output |
| gunicorn | `pip install 'apache-airflow[gunicorn]'` | Gunicorn server with rolling worker restarts for the API server |
| ldap | `pip install 'apache-airflow[ldap]'` | LDAP authentication for users |
| leveldb | `pip install 'apache-airflow[leveldb]'` | Required for use leveldb extra in google provider |
| pandas | `pip install 'apache-airflow[pandas]'` | Install Pandas library compatible with Airflow |
| polars | `pip install 'apache-airflow[polars]'` | Polars hooks and operators |
| rabbitmq | `pip install 'apache-airflow[rabbitmq]'` | RabbitMQ support as a Celery backend |
| s3fs | `pip install 'apache-airflow[s3fs]'` | Support for S3 as Airflow FS |
| saml | `pip install 'apache-airflow[saml]'` | Support for SAML authentication in Amazon provider |
| uv | `pip install 'apache-airflow[uv]'` | Install uv - fast, Rust-based package installer (experimental) |