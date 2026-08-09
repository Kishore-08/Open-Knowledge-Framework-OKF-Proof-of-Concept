---
id: kubernetes-swap-aware-scheduling-9edb5061
type: concept
title: Swap-aware scheduling
description: Kubernetes 1.36 does not support allocating Pods to nodes in a way that
  accounts
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/cluster-administration/swap-memory-management/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Swap-aware scheduling

Kubernetes 1.36 does not support allocating Pods to nodes in a way that accounts
for swap memory usage. The scheduler typically uses *requests* for infrastructure resources
to guide Pod placement, and Pods do not request swap space; they just request `memory`.
This means that the scheduler does not consider swap memory when making scheduling decisions.
While this is something we are actively working on, it is not yet implemented.

In order for administrators to ensure that Pods are not scheduled on nodes
with swap memory unless they are specifically intended to use it,
Administrators can taint nodes with swap available to protect against this problem.
Taints will ensure that workloads which tolerate swap will not spill onto nodes without swap under load.