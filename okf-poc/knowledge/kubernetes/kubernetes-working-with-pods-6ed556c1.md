---
id: kubernetes-working-with-pods-6ed556c1
type: concept
title: Working with Pods
description: You'll rarely create individual Pods directly in Kubernetes—even singleton
  Pods. This
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/pods/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

## Working with Pods

You'll rarely create individual Pods directly in Kubernetes—even singleton Pods. This
is because Pods are designed as relatively ephemeral, disposable entities. When
a Pod gets created (directly by you, or indirectly by a
[controller](https://kubernetes.io/docs/concepts/architecture/controller/ "A control loop that watches the shared state of the cluster through the apiserver and makes changes attempting to move the current state towards the desired state.")), the new Pod is
scheduled to run on a [Node](https://kubernetes.io/docs/concepts/architecture/nodes/ "A node is a worker machine in Kubernetes.") in your cluster.
The Pod remains on that node until the Pod finishes execution, the Pod object is deleted,
the Pod is *evicted* for lack of resources, or the node fails.

#### Note:

Restarting a container in a Pod should not be confused with restarting a Pod. A Pod
is not a process, but an environment for running container(s). A Pod persists until
it is deleted.

The name of a Pod must be a valid
[DNS subdomain](https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#dns-subdomain-names)
value, but this can produce unexpected results for the Pod hostname. For best compatibility,
the name should follow the more restrictive rules for a
[DNS label](https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#dns-label-names).