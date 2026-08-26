---
id: apache-airflow-dag-authoring-enhancements-51425edb
type: concept
title: DAG Authoring Enhancements
description: Airflow 3.0 includes several changes that improve consistency, clarity,
  and long-term stability for DAG authors.
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/release_notes.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### DAG Authoring Enhancements

Airflow 3.0 includes several changes that improve consistency, clarity, and long-term stability for DAG authors.

#### New Stable DAG Authoring Interface: `airflow.sdk`

Airflow 3.0 introduces a new, stable public API for DAG authoring under the `airflow.sdk` namespace,
available via the `apache-airflow-task-sdk` package.

The goal of this change is to **decouple DAG authoring from Airflow internals** (Scheduler, API Server, etc.),
providing a **forward-compatible, stable interface** for writing and maintaining DAGs across Airflow versions.

DAG authors should now import core constructs from `airflow.sdk` rather than internal modules.

**Key Imports from** `airflow.sdk`:

- Classes:

  - `Asset`
  - `BaseNotifier`
  - `BaseOperator`
  - `BaseOperatorLink`
  - `BaseSensorOperator`
  - `Connection`
  - `Context`
  - `DAG`
  - `EdgeModifier`
  - `Label`
  - `ObjectStoragePath`
  - `Param`
  - `TaskGroup`
  - `Variable`
- Decorators and Functions:

  - `@asset`
  - `@dag`
  - `@setup`
  - `@task`
  - `@task_group`
  - `@teardown`
  - `chain`
  - `chain_linear`
  - `cross_downstream`
  - `get_current_context`
  - `get_parsing_context`

For an exhaustive list of available classes, decorators, and functions, check `airflow.sdk.__all__`.

All DAGs should update imports to use `airflow.sdk` instead of referencing internal Airflow modules directly.
Legacy import paths (e.g., `airflow.models.dag.DAG`, `airflow.decorator.task`) are **deprecated** and
will be **removed** in a future Airflow version. Some additional utilities and helper functions
that DAGs sometimes use from `airflow.utils.*` and others will be progressively migrated to the Task SDK in future
minor releases.

These future changes aim to **complete the decoupling** of DAG authoring constructs
from internal Airflow services. DAG authors should expect continued improvements
to `airflow.sdk` with no backwards-incompatible changes to existing constructs.

For example, update:

```
# Old (Airflow 2.x)
from airflow.models import DAG
from airflow.decorators import task

# New (Airflow 3.x)
from airflow.sdk import DAG, task
```

#### Renamed Parameter: `fail_stop` → `fail_fast`

The DAG argument `fail_stop` has been renamed to `fail_fast` for improved clarity. This parameter controls whether a
DAG run should immediately stop execution when a task fails. DAG authors should update any code referencing
`fail_stop` to use the new name.

#### Context Cleanup and Parameter Removal

Several legacy context variables have been removed or may no longer be available in certain types of DAG runs,
including:

- `conf`
- `execution_date`
- `dag_run.external_trigger`

In asset-triggered and manually triggered DAG runs with `logical_date=None`, data interval fields such as
`data_interval_start` and `data_interval_end` may not be present in the task context. DAG authors should use
explicit references such as `dag_run.logical_date` and conditionally check for the presence of interval-related fields
where applicable.

#### Task Context Utilities Moved

Internal task context functions such as `get_parsing_context` have been moved to a more appropriate location (e.g.,
`airflow.models.taskcontext`). DAG authors using these utilities directly should update import paths accordingly.

#### Trigger Rule Restrictions

The `TriggerRule.ALWAYS` rule can no longer be used with teardown tasks or tasks that are expected to honor upstream
dependency semantics. DAG authors should ensure that teardown logic is defined with the appropriate trigger rules for
consistent task resolution behavior.

#### Asset Aliases for Reusability

A new utility function, `create_asset_aliases()`, allows DAG authors to define reusable aliases for frequently
referenced Assets. This improves modularity and reuse across DAG files and is particularly helpful for teams adopting
asset-centric DAGs.

#### Operator Links interface changed

The Operator Extra links, which can be defined either via plugins or custo