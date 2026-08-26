---
id: apache-airflow-provider-refactor-standardization-51425edb
type: concept
title: Provider Refactor & Standardization
description: Airflow 3.0 completes the migration of several core operators, sensors,
  hooks, and triggers into the new
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/release_notes.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Provider Refactor & Standardization

Airflow 3.0 completes the migration of several core operators, sensors, hooks, and triggers into the new
`apache-airflow-providers-standard` package. This package now includes commonly used components such as:

- `PythonOperator`, `BashOperator`
- `ExternalTaskSensor`, `FileSensor`
- `ShortCircuitOperator`, `LatestOnlyOperator`
- `SubprocessHook`, `FilesystemHook`
- `DateTimeTrigger`, `TimeDeltaTrigger`, `FileTrigger`

These operators, sensors, hooks, and triggers were previously bundled inside `airflow-core` but are now treated as provider-managed components to
improve modularity, testability, and lifecycle independence.

This change enables more consistent versioning across providers and prepares Airflow for a future where all integrations
— including “standard” ones — follow the same interface model.

To maintain compatibility with existing DAGs, the `apache-airflow-providers-standard` package is installable on both
Airflow 2.x and 3.x. Users upgrading from Airflow 2.x are encouraged to begin updating import paths and testing provider
installation in advance of the upgrade.

Legacy imports such as `airflow.operators.python.PythonOperator` are deprecated and will be removed soon. They should be
replaced with:

```
from airflow.providers.standard.operators.python import PythonOperator
```

The SimpleHttpOperator has been migrated to apache-airflow-providers-http and renamed to HttpOperator