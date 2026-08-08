---
id: kubernetes-swap-memory-management-9edb5061
type: concept
title: Swap memory management
description: Kubernetes can be configured to use swap memory on a [node](https://kubernetes.io/docs/concepts/architecture/nodes/
  "A node is a worker machine in Kubernetes."),
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/cluster-administration/swap-memory-management/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

# Swap memory management

Kubernetes can be configured to use swap memory on a [node](https://kubernetes.io/docs/concepts/architecture/nodes/ "A node is a worker machine in Kubernetes."),
allowing the kernel to free up physical memory by swapping out pages to backing storage.
This is useful for multiple use-cases.
For example, nodes running workloads that can benefit from using swap,
such as those that have large memory footprints but only access a portion of that memory at any given time.
It also helps prevent Pods from being terminated during memory pressure spikes,
shields nodes from system-level memory spikes that might compromise its stability,
allows for more flexible memory management on the node, and much more.

To learn about configuring swap in your cluster, read
[Configuring swap memory on Kubernetes nodes](https://kubernetes.io/docs/tutorials/cluster-management/provision-swap-memory/).