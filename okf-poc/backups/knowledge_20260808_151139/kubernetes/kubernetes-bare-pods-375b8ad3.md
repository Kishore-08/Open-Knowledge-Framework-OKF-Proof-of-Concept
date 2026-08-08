---
id: kubernetes-bare-pods-375b8ad3
type: concept
title: Bare Pods
description: Unlike the case where a user directly created Pods, a ReplicaSet replaces
  Pods that are deleted or
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/controllers/replicaset/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Bare Pods

Unlike the case where a user directly created Pods, a ReplicaSet replaces Pods that are deleted or
terminated for any reason, such as in the case of node failure or disruptive node maintenance,
such as a kernel upgrade. For this reason, we recommend that you use a ReplicaSet even if your
application requires only a single Pod. Think of it similarly to a process supervisor, only it
supervises multiple Pods across multiple nodes instead of individual processes on a single node. A
ReplicaSet delegates local container restarts to some agent on the node such as Kubelet.

### Job

Use a [`Job`](https://kubernetes.io/docs/concepts/workloads/controllers/job/) instead of a ReplicaSet for Pods that are
expected to terminate on their own (that is, batch jobs).