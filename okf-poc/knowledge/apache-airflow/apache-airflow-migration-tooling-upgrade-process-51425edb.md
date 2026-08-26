---
id: apache-airflow-migration-tooling-upgrade-process-51425edb
type: concept
title: Migration Tooling & Upgrade Process
description: Airflow 3 was designed with migration in mind. Many Airflow 2 DAGs will
  work without changes, especially if deprecation
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/release_notes.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Migration Tooling & Upgrade Process

Airflow 3 was designed with migration in mind. Many Airflow 2 DAGs will work without changes, especially if deprecation
warnings were addressed in earlier releases. To support the upgrade, Airflow 3 includes validation tools such as `ruff`
and `airflow config update`, as well as a simplified startup model.

For a step-by-step upgrade process, see the [Upgrade Guide](https://airflow.apache.org/docs/apache-airflow/stable/installation/upgrading_to_airflow3.html).

#### Minimum Supported Versions

To upgrade to Airflow 3.0, you must be running **Airflow 2.7 or later**.

Airflow 3.0 supports the following Python versions:

- Python 3.9
- Python 3.10
- Python 3.11
- Python 3.12

Earlier versions of Airflow or Python are not supported due to architectural changes and updated dependency requirements.

#### DAG Compatibility Checks

Airflow now includes a Ruff-based linter with custom rules to detect DAG patterns and interfaces that are no longer
compatible with Airflow 3.0. These checks are packaged under the `AIR30x` rule series. Example usage:

```
ruff check dags/ --select AIR301  --preview
ruff check dags/ --select AIR301 --fix  --preview
```

These checks can automatically fix many common issues such as renamed arguments, removed imports, or legacy context
variable usage.

#### Configuration Migration

Airflow 3.0 introduces a new utility to validate and upgrade your Airflow configuration file:

```
airflow config update
airflow config update --fix
```

This utility detects removed or deprecated configuration options and, if desired, updates them in-place.

Additional validation is available via:

```
airflow config lint
```

This command surfaces obsolete configuration keys and helps align your environment with Airflow 3.0 requirements.

#### Metadata Database Upgrade

As with previous major releases, the Airflow 3.0 upgrade includes schema changes to the metadata database. Before
upgrading, it is strongly recommended that you back up your database and optionally run:

```
airflow db clean
```

to remove old task instance, log, or XCom data. To apply the new schema:

```
airflow db migrate
```

#### Startup Behavior Changes

Airflow components are now started explicitly. For example:

```
airflow api-server        # Replaces airflow webserver
airflow dag-processor     # Required in all environments
```

These changes reflect Airflow’s new service-oriented architecture.