---
id: kubernetes-unutilized-swap-space-9edb5061
type: concept
title: Unutilized swap space
description: Under the `LimitedSwap` behavior, the amount of swap available to a Pod
  is determined automatically,
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/cluster-administration/swap-memory-management/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Unutilized swap space

Under the `LimitedSwap` behavior, the amount of swap available to a Pod is determined automatically,
based on the proportion of the memory requested relative to the node's total memory
(For more details, see the [section below](https://kubernetes.io/docs/concepts/cluster-administration/swap-memory-management/#how-is-the-swap-limit-being-determined-with-limitedswap)).

This design means that usually there would be some portion of swap that will remain
restricted for Kubernetes workloads.
For example, since Kubernetes 1.36 does not permit swap use for
Pods in the Guaranteed [QoS class](https://kubernetes.io/docs/concepts/workloads/pods/pod-qos/ "QoS Class (Quality of Service Class) provides a way for Kubernetes to classify pods within the cluster into several classes and make decisions about scheduling and eviction."),
the amount of swap that's proportional to the memory request for Guaranteed pods would
remain unused by Kubernetes workloads.

This behavior carries some risk in a situation where many pods are not eligible for swapping.
On the other hand, it effectively keeps some system-reserved amount of swap memory that can be used by processes
outside of Kubernetes' scope, such as system daemons and even kubelet itself.

## Good practice for using swap in a Kubernetes cluster