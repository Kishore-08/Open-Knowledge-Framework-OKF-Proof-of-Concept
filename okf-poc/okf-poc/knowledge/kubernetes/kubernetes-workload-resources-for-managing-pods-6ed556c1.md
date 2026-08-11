---
id: kubernetes-workload-resources-for-managing-pods-6ed556c1
type: concept
title: Workload resources for managing pods
description: Usually you don't need to create Pods directly, even singleton Pods.
  Instead, create them using workload resources such as [Deployment](https://kubernetes.io/docs/concepts/workloads/controllers/deploy
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/pods/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Workload resources for managing pods

Usually you don't need to create Pods directly, even singleton Pods. Instead, create them using workload resources such as [Deployment](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/ "Manages a replicated application on your cluster.") or [Job](https://kubernetes.io/docs/concepts/workloads/controllers/job/ "A finite or batch task that runs to completion.").
If your Pods need to track state, consider the
[StatefulSet](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/ "A StatefulSet manages deployment and scaling of a set of Pods, with durable storage and persistent identifiers for each Pod.") resource.

Each Pod is meant to run a single instance of a given application. If you want to
scale your application horizontally (to provide more overall resources by running
more instances), you should use multiple Pods, one for each instance. In
Kubernetes, this is typically referred to as *replication*.
Replicated Pods are usually created and managed as a group by a workload resource
and its [controller](https://kubernetes.io/docs/concepts/architecture/controller/ "A control loop that watches the shared state of the cluster through the apiserver and makes changes attempting to move the current state towards the desired state.").

See [Pods and controllers](https://kubernetes.io/docs/concepts/workloads/pods/#pods-and-controllers) for more information on how
Kubernetes uses workload resources, and their controllers, to implement application
scaling and auto-healing.

Pods natively provide two kinds of shared resources for their constituent containers:
[networking](https://kubernetes.io/docs/concepts/workloads/pods/#pod-networking) and [storage](https://kubernetes.io/docs/concepts/workloads/pods/#pod-storage).