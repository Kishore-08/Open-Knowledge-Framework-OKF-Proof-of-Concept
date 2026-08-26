---
id: apache-airflow-using-pythonvirtualenvoperator-8dafd1cd
type: concept
title: Using PythonVirtualenvOperator
description: This is simplest to use and most limited strategy. The PythonVirtualenvOperator
  allows you to dynamically
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/best-practices.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Using PythonVirtualenvOperator

This is simplest to use and most limited strategy. The PythonVirtualenvOperator allows you to dynamically
create a virtualenv that your Python callable function will execute in. In the modern
TaskFlow approach described in [Pythonic Dags with the TaskFlow API](https://airflow.apache.org/docs/apache-airflow/stable/tutorial/taskflow.html). this also can be done with decorating
your callable with `@task.virtualenv` decorator (recommended way of using the operator).
Each [`airflow.providers.standard.operators.python.PythonVirtualenvOperator`](https://airflow.apache.org/docs/apache-airflow-providers-standard/stable/_api/airflow/providers/standard/operators/python/index.html#airflow.providers.standard.operators.python.PythonVirtualenvOperator "(in apache-airflow-providers-standard v1.17.0)") task can
have its own independent Python virtualenv (dynamically created every time the task is run) and can
specify fine-grained set of requirements that need to be installed for that task to execute.

The operator takes care of:

- creating the virtualenv based on your environment
- serializing your Python callable and passing it to execution by the virtualenv Python interpreter
- executing it and retrieving the result of the callable and pushing it via xcom if specified

The benefits of the operator are:

- There is no need to prepare the venv upfront. It will be dynamically created before task is run, and
  removed after it is finished, so there is nothing special (except having virtualenv package in your
  Airflow dependencies) to make use of multiple virtual environments
- You can run tasks with different sets of dependencies on the same workers - thus Memory resources are
  reused (though see below about the CPU overhead involved in creating the venvs).
- In bigger installations, Dag authors do not need to ask anyone to create the venvs for you.
  As a Dag author, you only have to have virtualenv dependency installed and you can specify and modify the
  environments as you see fit.
- No changes in deployment requirements - whether you use Local virtualenv, or Docker, or Kubernetes,
  the tasks will work without adding anything to your deployment.
- No need to learn more about containers, Kubernetes as a Dag author. Only knowledge of Python requirements
  is required to author Dags this way.

There are certain limitations and overhead introduced by this operator:

- Your python callable has to be serializable. There are a number of python objects that are not serializable
  using standard `pickle` library. You can mitigate some of those limitations by using `dill` library
  but even that library does not solve all the serialization limitations.
- All dependencies that are not available in the Airflow environment must be locally imported in the callable you
  use and the top-level Python code of your Dag should not import/use those libraries.
- The virtual environments are run in the same operating system, so they cannot have conflicting system-level
  dependencies (`apt` or `yum` installable packages). Only Python dependencies can be independently
  installed in those environments.
- The operator adds a CPU, networking and elapsed time overhead for running each task - Airflow has
  to re-create the virtualenv from scratch for each task
- The workers need to have access to PyPI or private repositories to install dependencies
- The dynamic creation of virtualenv is prone to transient failures (for example when your repo is not available
  or when there is a networking issue with reaching the repository)
- It’s easy to fall into a “too” dynamic environment - since the dependencies you install might get upgraded
  and their transitive dependencies might get independent upgrades you might end up with the situation where
  your task will stop working because someone released a new version of a dependency or you might fall
  a victim of “supply chain” attack where new version of a dependency might become malici