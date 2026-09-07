---
id: kubernetes-multi-level-topology-placements-5d19d5cb
type: concept
title: Multi-level topology placements
description: 'FEATURE STATE:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/scheduling-eviction/topology-aware-scheduling/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

## Multi-level topology placements

FEATURE STATE:
`Kubernetes v1.37 [alpha]`(disabled by default)

When the [`CompositePodGroup`](https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/#CompositePodGroup)
feature gate and the `scheduling.k8s.io/v1alpha3` [API group](https://kubernetes.io/docs/concepts/overview/kubernetes-api/#api-groups-and-versioning "A set of related paths in the Kubernetes API.")
are enabled, the Topology-Aware Scheduling plugins extend their support to multi-level
`CompositePodGroup` hierarchies. These plugins are called for `CompositePodGroups` during
[hierarchical scheduling](https://kubernetes.io/docs/concepts/scheduling-eviction/podgroup-scheduling/).