---
id: kubernetes-garbage-collection-of-pods-3e34f258
type: concept
title: Garbage collection of Pods
description: For failed Pods, the API objects remain in the cluster's API until a
  human or
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Garbage collection of Pods

For failed Pods, the API objects remain in the cluster's API until a human or
[controller](https://kubernetes.io/docs/concepts/architecture/controller/ "A control loop that watches the shared state of the cluster through the apiserver and makes changes attempting to move the current state towards the desired state.") process
explicitly removes them.

The Pod garbage collector (PodGC), which is a controller in the control plane, cleans up
terminated Pods (with a phase of `Succeeded` or `Failed`), when the number of Pods exceeds the
configured threshold (determined by `terminated-pod-gc-threshold` in the kube-controller-manager).
This avoids a resource leak as Pods are created and terminated over time.

Additionally, PodGC cleans up any Pods which satisfy any of the following conditions:

1. are orphan Pods - bound to a node which no longer exists,
2. are unscheduled terminating Pods,
3. are terminating Pods, bound to a non-ready node tainted with
   [`node.kubernetes.io/out-of-service`](https://kubernetes.io/docs/reference/labels-annotations-taints/#node-kubernetes-io-out-of-service).

Along with cleaning up the Pods, PodGC will also mark them as failed if they are in a non-terminal
phase. Also, PodGC adds a Pod disruption condition when cleaning up an orphan Pod.
See [Pod disruption conditions](https://kubernetes.io/docs/concepts/workloads/pods/disruptions/#pod-disruption-conditions)
for more details.