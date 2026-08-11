---
id: kubernetes-pod-lifecycle-3e34f258
type: concept
title: Pod Lifecycle
description: This page describes the lifecycle of a Pod. Pods follow a defined lifecycle,
  starting
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

# Pod Lifecycle

This page describes the lifecycle of a Pod. Pods follow a defined lifecycle, starting
in the `Pending` [phase](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#pod-phase), moving through `Running` if at least one
of its primary containers starts OK, and then through either the `Succeeded` or
`Failed` phases depending on whether any container in the Pod terminated in failure.

While a Pod runs, the kubelet manages containers and translates the Pod's spec
for the container runtime. The kubelet also manages executing
[probes](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#container-probes) that track the health of your application.

Like individual application containers, Pods are considered to be relatively
ephemeral (rather than durable) entities. Pods are created, assigned a unique
ID ([UID](https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#uids)), and scheduled
to run on nodes where they remain until termination (according to restart policy) or
deletion.
If a [Node](https://kubernetes.io/docs/concepts/architecture/nodes/ "A node is a worker machine in Kubernetes.") dies, the Pods running on (or scheduled
to run on) that node are [marked for deletion](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#pod-garbage-collection). The control
plane marks the Pods for removal after a timeout period.