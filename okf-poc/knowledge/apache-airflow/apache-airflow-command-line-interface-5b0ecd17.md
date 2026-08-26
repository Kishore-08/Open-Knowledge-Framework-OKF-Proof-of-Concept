---
id: apache-airflow-command-line-interface-5b0ecd17
type: concept
title: Command Line Interface
description: Airflow has a very rich command line interface that allows for
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/cli-and-env-variables-ref.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Command Line Interface

Airflow has a very rich command line interface that allows for
many types of operation on a Dag, starting services, and supporting
development and testing.

Note

For more information on usage CLI, see [Using the Command Line Interface](https://airflow.apache.org/docs/apache-airflow/stable/howto/usage-cli.html)

Providers that implement executors might contribute additional commands to the CLI. Here are the commands
contributed by the community providers:

Important

Starting in Airflow `3.2.0`, provider-level CLI commands are available to manage core extensions such as auth managers and executors. Implementing provider-level CLI commands can reduce CLI startup time by avoiding heavy imports when they are not required.
See [provider-level CLI](https://airflow.apache.org/docs/apache-airflow-providers/core-extensions/cli-commands.html "(in apache-airflow-providers vstable)") for implementation guidance.

- Celery Executor and related CLI commands: [Celery Executor Commands](https://airflow.apache.org/docs/apache-airflow-providers-celery/stable/cli-ref.html "(in apache-airflow-providers-celery v3.23.1)")
- Kubernetes Executor and related CLI commands: [Kubernetes Executor Commands](https://airflow.apache.org/docs/apache-airflow-providers-cncf-kubernetes/stable/cli-ref.html "(in apache-airflow-providers-cncf-kubernetes v10.21.0)")
- Edge Executor and related CLI commands: [Edge Executor Commands](https://airflow.apache.org/docs/apache-airflow-providers-edge3/stable/cli-ref.html "(in apache-airflow-providers-edge3 v4.3.0)")
- AWS and related CLI commands: [Amazon CLI Commands](https://airflow.apache.org/docs/apache-airflow-providers-amazon/stable/cli-ref.html "(in apache-airflow-providers-amazon v9.34.0)")
- The `users` and `roles` CLI commands are described in FAB provider documentation [FAB CLI Commands](https://airflow.apache.org/docs/apache-airflow-providers-fab/stable/cli-ref.html "(in apache-airflow-providers-fab v3.8.0)")

```
Usage: airflow [-h] GROUP_OR_COMMAND ...
```