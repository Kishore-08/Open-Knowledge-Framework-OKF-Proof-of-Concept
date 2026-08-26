---
id: apache-airflow-using-airflow-public-interfaces-9e8d674b
type: concept
title: Using Airflow Public Interfaces
description: Note
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/public-airflow-interface.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Using Airflow Public Interfaces

Note

As of **Airflow 3.0**, users should use the `airflow.sdk` namespace as the official **Public Interface**, as defined in [AIP-72](https://cwiki.apache.org/confluence/display/AIRFLOW/AIP-72+Task+Execution+Interface+aka+Task+SDK).

Direct interaction with internal modules or the metadata database is not possible.
For stable, production-safe integration, it is recommended to use:

- The official **REST API**
- The **Python Client SDK** (airflow-client-python)
- The new **Task SDK** (`airflow.sdk`)

Related docs:
- [Release Notes 3.0](https://airflow.apache.org/docs/apache-airflow/stable/release_notes.html)
- [Task SDK Overview](https://airflow.apache.org/docs/apache-airflow/stable/concepts/taskflow.html)

The following are some examples of the public interface of Airflow:

- When you are writing your own operators or hooks. This is commonly done when no hook or operator exists for your use case, or when perhaps when one exists but you need to customize the behavior.
- When writing new [Plugins](https://airflow.apache.org/docs/apache-airflow/stable/administration-and-deployment/plugins.html) that extend Airflow’s functionality beyond
  Dag building blocks. Secrets, Timetables, Triggers, Listeners are all examples of such functionality. This
  is usually done by users who manage Airflow instances.
- Bundling custom Operators, Hooks, Plugins and releasing them together via
  [providers](https://airflow.apache.org/docs/apache-airflow-providers/index.html "(in apache-airflow-providers vstable)") - this is usually done by those who intend to
  provide a reusable set of functionality for external services or applications Airflow integrates with.
- Using the taskflow API to write tasks
- Relying on the consistent behavior of Airflow objects

One aspect of “public interface” is extending or using Airflow Python classes and functions. The classes
and functions mentioned below can be relied on to maintain backwards-compatible signatures and behaviours within
MAJOR version of Airflow. On the other hand, classes and methods starting with `_` (also known
as protected Python methods) and `__` (also known as private Python methods) are not part of the Public
Airflow Interface and might change at any time.

You can also use Airflow’s Public Interface via the [Stable REST API](https://airflow.apache.org/docs/apache-airflow/stable/stable-rest-api-ref.html) (based on the
OpenAPI specification). For specific needs you can also use the
[Airflow Command Line Interface (CLI)](https://airflow.apache.org/docs/apache-airflow/stable/cli-and-env-variables-ref.html) though its behaviour might change
in details (such as output format and available flags) so if you want to rely on those in programmatic
way, the Stable REST API is recommended.