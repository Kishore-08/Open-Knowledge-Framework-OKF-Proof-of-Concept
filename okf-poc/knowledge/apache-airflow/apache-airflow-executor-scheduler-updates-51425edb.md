---
id: apache-airflow-executor-scheduler-updates-51425edb
type: concept
title: Executor & Scheduler Updates
description: Airflow 3.0 introduces several important improvements and behavior changes
  in how DAGs and tasks are scheduled,
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/release_notes.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Executor & Scheduler Updates

Airflow 3.0 introduces several important improvements and behavior changes in how DAGs and tasks are scheduled,
prioritized, and executed.

#### Standalone DAG Processor Required

Airflow 3.0 now requires the standalone DAG processor to parse DAGs. This dedicated process improves scheduler
performance, isolation, and observability. It also simplifies architecture by clearly separating DAG parsing from
scheduling logic. This change may affect custom deployments that previously used embedded DAG parsing.

#### Priority Weight Capped by Pool Slots

The `priority_weight` value on a task is now capped by the number of available pool slots. This ensures that resource
availability remains the primary constraint in task execution order, preventing high-priority tasks from starving others
when resource contention exists.

#### Teardown Task Handling During DAG Termination

Teardown tasks will now be executed even when a DAG run is terminated early. This ensures that cleanup logic is
respected, improving reliability for workflows that use teardown tasks to manage ephemeral infrastructure, temporary
files, or downstream notifications.

#### Improved Scheduler Fault Tolerance

Scheduler components now use `run_with_db_retries` to handle transient database issues more gracefully. This enhances
Airflow’s fault tolerance in high-volume environments and reduces the likelihood of scheduler restarts due to temporary
database connection problems.

#### Mapped Task Stats Accuracy

Airflow 3.0 fixes a bug that caused incorrect task statistics to be reported for dynamic task mapping. Stats now
accurately reflect the number of mapped task instances and their statuses, improving observability and debugging for
dynamic workflows.

#### `SequentialExecutor` has been removed

`SequentialExecutor` was primarily used for local testing but is now redundant, as `LocalExecutor`
supports SQLite with WAL mode and provides better performance with parallel execution.
Users should switch to `LocalExecutor` or `CeleryExecutor` as alternatives.