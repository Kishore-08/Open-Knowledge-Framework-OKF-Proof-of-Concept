---
id: apache-airflow-providers-extras-f586a1ea
type: concept
title: Providers extras
description: These providers extras are simply convenience extras to install providers
  so that you can install the providers with simple command - including
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/extra-packages-ref.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Providers extras

These providers extras are simply convenience extras to install providers so that you can install the providers with simple command - including
provider package and necessary dependencies in single command, which allows PIP to resolve any conflicting dependencies. This is extremely useful
for first time installation where you want to repeatably install version of dependencies which are ‘valid’ for both Airflow and providers installed.

For example the below command will install:

> - apache-airflow
> - apache-airflow-core
> - apache-airflow-task-sdk
> - apache-airflow-providers-amazon
> - apache-airflow-providers-google
> - apache-airflow-providers-apache-spark

with a consistent set of dependencies based on constraint files provided by Airflow Community at the time 3.3.1 version was released.

```
pip install apache-airflow[google,amazon,apache-spark]==3.3.1 \
  --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-3.3.1/constraints-3.10.txt"
```

Note, that this will install providers in the versions that were released at the time of Airflow 3.3.1 release. You can later
upgrade those providers manually if you want to use latest versions of the providers.

Also, those extras are ONLY available in the `apache-airflow` distribution package as they are a convenient way to install
all the `airflow` packages together - similarly to what happened in Airflow 2. When you are installing `airflow-core` or
`airflow-task-sdk` separately, if you want to install providers, you need to install them separately as
`apache-airflow-providers-*` distribution packages.