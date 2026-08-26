---
id: apache-airflow-executors-9e8d674b
type: concept
title: Executors
description: Executors are the mechanism by which task instances get run. All executors
  are
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/public-airflow-interface.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Executors

Executors are the mechanism by which task instances get run. All executors are
derived from `BaseExecutor`. There are several
executor implementations built-in Airflow, each with their own unique characteristics and capabilities.

The executor interface itself (the BaseExecutor class) is public, but the built-in executors are not (i.e. KubernetesExecutor, LocalExecutor, etc). This means that, to use KubernetesExecutor as an example, we may make changes to KubernetesExecutor in minor or patch Airflow releases which could break an executor that subclasses KubernetesExecutor. This is necessary to allow Airflow developers sufficient freedom to continue to improve the executors we offer. Accordingly, if you want to modify or extend a built-in executor, you should incorporate the full executor code into your project so that such changes will not break your derivative executor.

You can read more about executors and how to write your own in [Executor](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/executor/index.html).

Added in version 2.6: The executor interface has been present in Airflow for quite some time but prior to 2.6, there was executor-specific
code elsewhere in the codebase. As of version 2.6 executors are fully decoupled, in the sense that Airflow core no
longer needs to know about the behavior of specific executors.
You could have succeeded with implementing a custom executor before Airflow 2.6, and a number
of people did, but there were some hard-coded behaviours that preferred in-built
executors, and custom executors could not provide full functionality that built-in executors had.