---
id: apache-airflow-using-dockeroperator-or-kubernetes-pod-operator-8dafd1cd
type: concept
title: Using DockerOperator or Kubernetes Pod Operator
description: Another strategy is to use the [`airflow.providers.docker.operators.docker.DockerOperator`](https://airflow.apache.org/docs/apache-airflow-providers-docker/stable/_api/airflow/providers/docker/operato
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/best-practices.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Using DockerOperator or Kubernetes Pod Operator

Another strategy is to use the [`airflow.providers.docker.operators.docker.DockerOperator`](https://airflow.apache.org/docs/apache-airflow-providers-docker/stable/_api/airflow/providers/docker/operators/docker/index.html#airflow.providers.docker.operators.docker.DockerOperator "(in apache-airflow-providers-docker v4.5.9)")
[`airflow.providers.cncf.kubernetes.operators.pod.KubernetesPodOperator`](https://airflow.apache.org/docs/apache-airflow-providers-cncf-kubernetes/stable/_api/airflow/providers/cncf/kubernetes/operators/pod/index.html#airflow.providers.cncf.kubernetes.operators.pod.KubernetesPodOperator "(in apache-airflow-providers-cncf-kubernetes v10.21.0)")
Those require that Airflow has access to a Docker engine or Kubernetes cluster.

Similarly as in case of Python operators, the taskflow decorators are handy for you if you would like to
use those operators to execute your callable Python code.

However, it is far more involved - you need to understand how Docker/Kubernetes Pods work if you want to use
this approach, but the tasks are fully isolated from each other and you are not even limited to running
Python code. You can write your tasks in any Programming language you want. Also your dependencies are
fully independent from Airflow ones (including the system level dependencies) so if your task require
a very different environment, this is the way to go.

Added in version 2.2.

As of version 2.2 of Airflow you can use `@task.docker` decorator to run your functions with `DockerOperator`.

Added in version 2.4.

As of version 2.2 of Airflow you can use `@task.kubernetes` decorator to run your functions with `KubernetesPodOperator`.

The benefits of using those operators are:

- You can run tasks with different sets of both Python and system level dependencies, or even tasks
  written in completely different language or even different processor architecture (x86 vs. arm).
- The environment used to run the tasks enjoys the optimizations and immutability of containers, where a
  similar set of dependencies can effectively reuse a number of cached layers of the image, so the
  environment is optimized for the case where you have multiple similar, but different environments.
- The dependencies can be pre-vetted by the admins and your security team, no unexpected, new code will
  be added dynamically. This is good for both, security and stability.
- Strong process-level isolation between tasks. Tasks run in separate containers/pods and cannot
  influence one another at the process or filesystem level. They can still interact through standard
  Airflow mechanisms (XComs, connections, variables) via the Execution API. See
  [Airflow Security Model](https://airflow.apache.org/docs/apache-airflow/stable/security/security_model.html) for the full isolation model.

The drawbacks:

- There is an overhead to start the tasks. Usually not as big as when creating virtual environments dynamically,
  but still significant (especially for the `KubernetesPodOperator`).
- In case of TaskFlow decorators, the whole method to call needs to be serialized and sent over to the
  Docker Container or Kubernetes Pod, and there are system-level limitations on how big the method can be.
  Serializing, sending, and finally deserializing the method on remote end also adds an overhead.
- There is a resources overhead coming from multiple processes needed. Running tasks in case of those
  two operators requires at least two processes - one process (running in Docker Container or Kubernetes Pod)
  executing the task, and a supervising process in the Airflow worker that submits the job to
  Docker/Kubernetes and monitors the execution.
- Your environment needs to have the container images ready upfront. This usually means that you
  cannot change them on the fly. Adding system dependencies, modifying or changing Python requirements
  requires an image rebuilding and publishing (usually in your private reg