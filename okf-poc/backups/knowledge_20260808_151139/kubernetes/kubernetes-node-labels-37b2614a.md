---
id: kubernetes-node-labels-37b2614a
type: concept
title: Node labels
description: Like many other Kubernetes objects, nodes have
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

## Node labels

Like many other Kubernetes objects, nodes have
[labels](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/). You can
[attach labels manually](https://kubernetes.io/docs/tasks/configure-pod-container/assign-pods-nodes/#add-a-label-to-a-node).
Kubernetes also populates a [standard set of labels](https://kubernetes.io/docs/reference/node/node-labels/)
on all nodes in a cluster.

#### Note:

The value of these labels is cloud provider specific and is not guaranteed to be reliable.
For example, the value of `kubernetes.io/hostname` may be the same as the node name in some environments
and a different value in other environments.