---
id: kubernetes-workloads-3e9846ed
type: concept
title: Workloads
description: Understand Pods, the smallest deployable compute object in Kubernetes,
  and the higher-level abstractions that help you to run them.
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

# Workloads

Understand Pods, the smallest deployable compute object in Kubernetes, and the higher-level abstractions that help you to run them.

A workload is an application running on Kubernetes.
Whether your workload is a single component or several that work together, on Kubernetes you run
it inside a set of [*pods*](https://kubernetes.io/docs/concepts/workloads/pods/).
In Kubernetes, a Pod represents a set of one or more running
[containers](https://kubernetes.io/docs/concepts/containers/ "A lightweight and portable executable image that contains software and all of its dependencies.") on your cluster.

Kubernetes pods have a [defined lifecycle](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/).
For example, once a pod is running in your cluster then a critical fault on the
[node](https://kubernetes.io/docs/concepts/architecture/nodes/ "A node is a worker machine in Kubernetes.") where that pod is running means that
all the pods on that node fail. Kubernetes treats that level of failure as final: you
would need to create a new Pod to recover, even if the node later becomes healthy.

However, to make life considerably easier, you don't need to manage each Pod directly.
Instead, you can use *workload resources* that manage a set of pods on your behalf.
These resources configure [controllers](https://kubernetes.io/docs/concepts/architecture/controller/ "A control loop that watches the shared state of the cluster through the apiserver and makes changes attempting to move the current state towards the desired state.")
that make sure the right number of the right kind of pod are running, to match the state
you specified.

Kubernetes provides several built-in workload resources:

- [Deployment](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/) and [ReplicaSet](https://kubernetes.io/docs/concepts/workloads/controllers/replicaset/)
  (replacing the legacy resource
  [ReplicationController](https://kubernetes.io/docs/reference/glossary/?all=true#term-replication-controller "A (deprecated) API object that manages a replicated application.")).
  Deployment is a good fit for managing a stateless application workload on your cluster,
  where any Pod in the Deployment is interchangeable and can be replaced if needed.
- [StatefulSet](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/) lets you
  run one or more related Pods that do track state somehow. For example, if your workload
  records data persistently, you can run a StatefulSet that matches each Pod with a
  [PersistentVolume](https://kubernetes.io/docs/concepts/storage/persistent-volumes/). Your code, running in the
  Pods for that StatefulSet, can replicate data to other Pods in the same StatefulSet
  to improve overall resilience.
- [DaemonSet](https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/) defines Pods that provide
  facilities that are local to nodes.
  Every time you add a node to your cluster that matches the specification in a DaemonSet,
  the control plane schedules a Pod for that DaemonSet onto the new node.
  Each pod in a DaemonSet performs a job similar to a system daemon on a classic Unix / POSIX
  server. A DaemonSet might be fundamental to the operation of your cluster, such as
  a plugin to run [cluster networking](https://kubernetes.io/docs/concepts/cluster-administration/networking/#how-to-implement-the-kubernetes-network-model),
  it might help you to manage the node,
  or it could provide optional behavior that enhances the container platform you are running.
- [Job](https://kubernetes.io/docs/concepts/workloads/controllers/job/) and
  [CronJob](https://kubernetes.io/docs/concepts/workloads/controllers/cron-jobs/) provide different ways to
  define tasks that run to completion and then stop.
  You can use a [Job](https://kubernetes.io/docs/concepts/workloads/controllers/job/) to
  define a task that runs to completion, just once. You can use a
  [CronJob](https://kubernetes.io/do