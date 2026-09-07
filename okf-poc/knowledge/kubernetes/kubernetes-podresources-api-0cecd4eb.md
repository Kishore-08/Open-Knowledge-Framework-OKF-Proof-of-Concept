---
id: kubernetes-podresources-api-0cecd4eb
type: concept
title: PodResources API
description: In Kubernetes 1.37, the `kubelet`'s node-local `PodResources` gRPC API
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/resource-management/pod-level-resource-managers/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

### PodResources API

In Kubernetes 1.37, the `kubelet`'s node-local `PodResources` gRPC API
includes pod-level resource allocations when `PodLevelResourceManagers` is
enabled. Node-local monitoring agents and device plugins can query
top-level Pod assignments (`cpu_ids` and `memory`) while avoiding
double-counting container-level allocations.

For complete API schemas, field masks, and scope-by-scope reporting tables, see
the
[Pod-level resource managers reference](https://kubernetes.io/docs/reference/node/pod-level-resource-managers/#podresources-api).