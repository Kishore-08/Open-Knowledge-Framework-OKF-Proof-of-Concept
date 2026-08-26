---
id: apache-airflow-config-interface-changes-51425edb
type: concept
title: Config & Interface Changes
description: Airflow 3.0 introduces several configuration and interface updates that
  improve consistency, clarify ownership of core
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/release_notes.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Config & Interface Changes

Airflow 3.0 introduces several configuration and interface updates that improve consistency, clarify ownership of core
utilities, and remove legacy behaviors that were no longer aligned with modern usage patterns.

#### Default Value Handling

Airflow no longer silently updates configuration options that retain deprecated default values. Users are now required
to explicitly set any config values that differ from the current defaults. This change improves transparency and
prevents unintentional behavior changes during upgrades.

#### Refactored Config Defaults

Several configuration defaults have changed in Airflow 3.0 to better reflect modern usage patterns:

- The default value of `catchup_by_default` is now `False`. DAGs will not backfill missed intervals unless explicitly configured to do so.
- The default value of `create_cron_data_intervals` is now `False`. Cron expressions are now interpreted using the `CronTriggerTimetable` instead of the legacy `CronDataIntervalTimetable`. This change simplifies interval logic and aligns with the future direction of Airflow’s scheduling system. Set this flag explicitly **before** upgrading from Airflow 2 if you rely on data interval semantics; flipping it later (after Airflow 3 DAG runs exist) will skip one scheduled run per affected DAG.

#### Refactored Internal Utilities

Several core components have been moved to more intuitive or stable locations:

- The `SecretsMasker` class has been relocated to `airflow.sdk.execution_time.secrets_masker`.
- The `ObjectStoragePath` utility previously located under `airflow.io` is now available via `airflow.sdk`.

These changes simplify imports and reflect broader efforts to stabilize utility interfaces across the Airflow codebase.

#### Improved `inlet_events`, `outlet_events`, and `triggering_asset_events`

Asset event mappings in the task context are improved to better support asset use cases, including new features introduced in AIP-74.

Events of an asset or asset alias are now accessed directly by a concrete object to avoid ambiguity. Using a `str` to access events is
no longer supported. Use an `Asset` or `AssetAlias` object, or `Asset.ref` to refer to an entity explicitly instead, such as:

```
outlet_events[Asset.ref(name="myasset")]  # Get events for asset named "myasset".
outlet_events[AssetAlias(name="myalias")]  # Get events for asset alias named "myalias".
```

Alternatively, two helpers `for_asset` and `for_asset_alias` are added as shortcuts:

```
outlet_events.for_asset(name="myasset")  # Get events for asset named "myasset".
outlet_events.for_asset_alias(name="myalias")  # Get events for asset alias named "myalias".
```

The internal representation of asset event triggers now also includes an explicit `uri` field, simplifying traceability and
aligning with the broader asset-aware execution model introduced in Airflow 3.0. DAG authors interacting directly with
`inlet_events` may need to update logic that assumes the previous structure.

#### Behaviour change in `xcom_pull`

In Airflow 2, the `xcom_pull()` method allowed pulling XComs by key without specifying task\_ids, despite the fact that the underlying
DB model defines task\_id as part of the XCom primary key. This created ambiguity: if two tasks pushed XComs with the same key,
`xcom_pull()` would pull whichever one happened to be first, leading to unpredictable behavior.

Airflow 3 resolves this inconsistency by requiring `task_ids` when pulling by key. This change aligns with the task-scoped nature of
XComs as defined by the schema, ensuring predictable and consistent behavior.

DAG Authors should update their dags to use `task_ids` if their dags used `xcom_pull` without `task_ids` such as:

```
kwargs["ti"].xcom_pull(key="key")
```

Should be updated to:

```
kwargs["ti"].xcom_pull(task_ids="task1", key="key")
```

#### Removed Configuration Keys

As part of the deprecation cleanup, several legacy configuration options have been removed. The