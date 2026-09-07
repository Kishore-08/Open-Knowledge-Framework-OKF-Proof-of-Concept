---
id: kubernetes-pod-level-resource-managers-6d51e885
type: concept
title: Pod-level resource managers
description: 'FEATURE STATE:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/resource-management/resource-managers/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

## Pod-level resource managers

FEATURE STATE:
`Kubernetes v1.37 [beta]`(disabled by default)

Pod-level resource support for `kubelet` resource managers (Topology, CPU,
and Memory) allows resource managers to use `.spec.resources` directly for
NUMA alignment and exclusive allocation decisions.

To learn more, see the dedicated
[Pod-level resource managers](https://kubernetes.io/docs/concepts/resource-management/pod-level-resource-managers/)
concept page, or read how to
[Assign Pod-level CPU and memory resources](https://kubernetes.io/docs/tasks/configure-pod-container/assign-pod-level-resources/).

## What's next

- [Node Resource Managers](https://kubernetes.io/docs/concepts/policy/node-resource-managers/)