---
id: kubernetes-taints-and-tolerations-b7b8ba42
type: concept
title: Taints and tolerations
description: 'The DaemonSet controller automatically adds a set of [tolerations](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/
  "A core object consisting of three required properties:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/
updated_at: '2026-08-13'
created_at: '2026-08-13'
---

### Taints and tolerations

The DaemonSet controller automatically adds a set of [tolerations](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/ "A core object consisting of three required properties: key, value, and effect. Tolerations enable the scheduling of pods on nodes or node groups that have a matching taint.") to DaemonSet Pods:

Tolerations for DaemonSet pods

| Toleration key | Effect | Details |
| --- | --- | --- |
| [`node.kubernetes.io/not-ready`](https://kubernetes.io/docs/reference/labels-annotations-taints/#node-kubernetes-io-not-ready) | `NoExecute` | DaemonSet Pods can be scheduled onto nodes that are not healthy or ready to accept Pods. Any DaemonSet Pods running on such nodes will not be evicted. |
| [`node.kubernetes.io/unreachable`](https://kubernetes.io/docs/reference/labels-annotations-taints/#node-kubernetes-io-unreachable) | `NoExecute` | DaemonSet Pods can be scheduled onto nodes that are unreachable from the node controller. Any DaemonSet Pods running on such nodes will not be evicted. |
| [`node.kubernetes.io/disk-pressure`](https://kubernetes.io/docs/reference/labels-annotations-taints/#node-kubernetes-io-disk-pressure) | `NoSchedule` | DaemonSet Pods can be scheduled onto nodes with disk pressure issues. |
| [`node.kubernetes.io/memory-pressure`](https://kubernetes.io/docs/reference/labels-annotations-taints/#node-kubernetes-io-memory-pressure) | `NoSchedule` | DaemonSet Pods can be scheduled onto nodes with memory pressure issues. |
| [`node.kubernetes.io/pid-pressure`](https://kubernetes.io/docs/reference/labels-annotations-taints/#node-kubernetes-io-pid-pressure) | `NoSchedule` | DaemonSet Pods can be scheduled onto nodes with process pressure issues. |
| [`node.kubernetes.io/unschedulable`](https://kubernetes.io/docs/reference/labels-annotations-taints/#node-kubernetes-io-unschedulable) | `NoSchedule` | DaemonSet Pods can be scheduled onto nodes that are unschedulable. |
| [`node.kubernetes.io/network-unavailable`](https://kubernetes.io/docs/reference/labels-annotations-taints/#node-kubernetes-io-network-unavailable) | `NoSchedule` | **Only added for DaemonSet Pods that request host networking**, i.e., Pods having `spec.hostNetwork: true`. Such DaemonSet Pods can be scheduled onto nodes with unavailable network. |

You can add your own tolerations to the Pods of a DaemonSet as well, by
defining these in the Pod template of the DaemonSet.

Because the DaemonSet controller sets the
`node.kubernetes.io/unschedulable:NoSchedule` toleration automatically,
Kubernetes can run DaemonSet Pods on nodes that are marked as *unschedulable*.

If you use a DaemonSet to provide an important node-level function, such as
[cluster networking](https://kubernetes.io/docs/concepts/cluster-administration/networking/), it is
helpful that Kubernetes places DaemonSet Pods on nodes before they are ready.
For example, without that special toleration, you could end up in a deadlock
situation where the node is not marked as ready because the network plugin is
not running there, and at the same time the network plugin is not running on
that node because the node is not yet ready.