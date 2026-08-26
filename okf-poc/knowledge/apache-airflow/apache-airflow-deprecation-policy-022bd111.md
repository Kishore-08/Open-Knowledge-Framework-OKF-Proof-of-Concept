---
id: apache-airflow-deprecation-policy-022bd111
type: concept
title: Deprecation policy
description: From time-to-time existing features will be deprecated, or modules will
  be renamed.
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/release-process.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Deprecation policy

From time-to-time existing features will be deprecated, or modules will be renamed.

When this happens, the existing code will continue to work but will issue a DeprecationWarning (or a subclass) when the code is executed.
This code will continue to work for the rest of the current major version – if it works on 2.0.0, it will work for every 2.Y.Z release.

So, for example, if we decided to start the deprecation of a function in Airflow 2.2.4:

- Airflow 2.2 will contain a backwards-compatible replica of the function which will raise a DeprecationWarning
- Airflow 2.3 will continue to work and issue a warning
- Airflow 3.0 (the major version that follows 2.2) will remove the feature outright

The exception to this deprecation policy is any feature which is marked as “experimental”, which *may* suffer breaking changes or complete removal in a Feature release.