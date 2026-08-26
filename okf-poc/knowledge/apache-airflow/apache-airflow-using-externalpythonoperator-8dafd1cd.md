---
id: apache-airflow-using-externalpythonoperator-8dafd1cd
type: concept
title: Using ExternalPythonOperator
description: Added in version 2.4.
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/best-practices.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Using ExternalPythonOperator

Added in version 2.4.

A bit more involved but with significantly less overhead, security, stability problems is to use the
`` airflow.providers.standard.operators.python.ExternalPythonOperator` ``. In the modern
TaskFlow approach described in [Pythonic Dags with the TaskFlow API](https://airflow.apache.org/docs/apache-airflow/stable/tutorial/taskflow.html). this also can be done with decorating
your callable with `@task.external_python` decorator (recommended way of using the operator).
It requires, however, that you have a pre-existing, immutable Python environment, that is prepared upfront.
Unlike in [`airflow.providers.standard.operators.python.PythonVirtualenvOperator`](https://airflow.apache.org/docs/apache-airflow-providers-standard/stable/_api/airflow/providers/standard/operators/python/index.html#airflow.providers.standard.operators.python.PythonVirtualenvOperator "(in apache-airflow-providers-standard v1.17.0)") you cannot add new dependencies
to such pre-existing environment. All dependencies you need should be added upfront in your environment
and available in all the workers in case your Airflow runs in a distributed environment.

This way you avoid the overhead and problems of re-creating the virtual environment but they have to be
prepared and deployed together with Airflow installation. Usually people who manage Airflow installation
need to be involved, and in bigger installations those are usually different people than Dag authors
(DevOps/System Admins).

Those virtual environments can be prepared in various ways - if you use LocalExecutor they just need to be installed
at the machine where scheduler is run, if you are using distributed Celery virtualenv installations, there
should be a pipeline that installs those virtual environments across multiple machines, finally if you are using
Docker Image (for example via Kubernetes), the virtualenv creation should be added to the pipeline of
your custom image building.

The benefits of the operator are:

- No setup overhead when running the task. The virtualenv is ready when you start running a task.
- You can run tasks with different sets of dependencies on the same workers - thus all resources are reused.
- There is no need to have access by workers to PyPI or private repositories. Less chance for transient
  errors resulting from networking.
- The dependencies can be pre-vetted by the admins and your security team, no unexpected, new code will
  be added dynamically. This is good for both, security and stability.
- Limited impact on your deployment - you do not need to switch to Docker containers or Kubernetes to
  make a good use of the operator.
- No need to learn more about containers, Kubernetes as a Dag author. Only knowledge of Python, requirements
  is required to author Dags this way.

The drawbacks:

- Your environment needs to have the virtual environments prepared upfront. This usually means that you
  cannot change it on the fly, adding new or changing requirements require at least an Airflow re-deployment
  and iteration time when you work on new versions might be longer.
- Your python callable has to be serializable. There are a number of python objects that are not serializable
  using standard `pickle` library. You can mitigate some of those limitations by using `dill` library
  but even that library does not solve all the serialization limitations.
- All dependencies that are not available in Airflow environment must be locally imported in the callable you
  use and the top-level Python code of your Dag should not import/use those libraries.
- The virtual environments are run in the same operating system, so they cannot have conflicting system-level
  dependencies (`apt` or `yum` installable packages). Only Python dependencies can be independently
  installed in those environments
- The tasks are only isolated from each other via running in different environments. This makes it possible
  that running tasks will