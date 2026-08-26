---
id: apache-airflow-cli-api-changes-51425edb
type: concept
title: CLI & API Changes
description: Airflow 3.0 introduces changes to both the CLI and REST API interfaces
  to better align with service-oriented deployments
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/release_notes.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### CLI & API Changes

Airflow 3.0 introduces changes to both the CLI and REST API interfaces to better align with service-oriented deployments
and event-driven workflows.

#### Split CLI Architecture (AIP-81)

The Airflow CLI has been split into two distinct interfaces:

- The core `airflow` CLI now handles only local functionality (e.g., `airflow tasks test`, `airflow dags list`).
- Remote functionality, including triggering DAGs or managing connections in service-mode environments, is now handled by a separate CLI called `airflowctl`, distributed via the `apache-airflow-client` package.

This change improves security and modularity for deployments that use Airflow in a distributed or API-first context.

#### REST API v2 replaces v1

The legacy REST API v1, previously built with Connexion and Marshmallow, has been replaced by a modern FastAPI-based REST API v2.

This new implementation improves performance, aligns more closely with web standards, and provides a consistent developer experience across the API and UI.

Key changes include stricter validation (422 errors instead of 400), the removal of the `execution_date` parameter in favor of `logical_date`, and more consistent query parameter handling.

The v2 API is now the stable, fully supported interface for programmatic access to Airflow, and also powers the new UI - achieving full feature parity between the UI and API.

For details, see the [Airflow REST API v2](https://airflow.apache.org/docs/apache-airflow/stable/stable-rest-api-ref.html) documentation.

#### REST API: DAG Trigger Behavior Updated

The behavior of the `POST /dags/{dag_id}/dagRuns` endpoint has changed. If a `logical_date` is not explicitly
provided when triggering a DAG via the REST API, it now defaults to `None`.

This aligns with event-driven DAGs and manual runs in Airflow 3.0, but may break backward compatibility with scripts or
tools that previously relied on Airflow auto-generating a timestamped `logical_date`.

#### Removed CLI Flags and Commands

Several deprecated CLI arguments and commands that were marked for removal in earlier versions have now been cleaned up
in Airflow 3.0. Run `airflow --help` to review the current set of available commands and arguments.

- Deprecated `--ignore-depends-on-past` cli option is replaced by `--depends-on-past ignore`.
- `--tree` flag for `airflow tasks list` command is removed. The format of the output with that flag can be
  expensive to generate and extremely large, depending on the DAG. `airflow dag show` is a better way to
  visualize the relationship of tasks in a DAG.
- Changing `dag_id` from flag (`-d`, `--dag-id`) to a positional argument in the `dags list-runs` CLI command.
- The `airflow db init` and `airflow db upgrade` commands have been removed. Use `airflow db migrate` instead
  to initialize or migrate the metadata database. If you would like to create default connections use
  `airflow connections create-default-connections`.
- `airflow api-server` has replaced `airflow webserver` cli command.