---
id: kubernetes-memory-manager-2f1e5981
type: concept
title: Memory manager
description: 'FEATURE STATE:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/resource-managers/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

## Memory manager

FEATURE STATE:
`Kubernetes v1.32 [stable]`(enabled by default)

*Memory Manager* is a kubelet component that provides exclusive resource
allocation for memory resources. It consults with the Topology Manager to make
resource assignment decisions. To learn more, read
[Control Memory Management Policies on a Node](https://kubernetes.io/docs/tasks/administer-cluster/memory-manager/).