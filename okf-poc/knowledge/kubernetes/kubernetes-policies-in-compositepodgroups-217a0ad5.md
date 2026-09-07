---
id: kubernetes-policies-in-compositepodgroups-217a0ad5
type: concept
title: Policies in CompositePodGroups
description: 'FEATURE STATE:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/workload-api/policies/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

## Policies in CompositePodGroups

FEATURE STATE:
`Kubernetes v1.37 [alpha]`(disabled by default)

When the [`CompositePodGroup`](https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/#CompositePodGroup)
feature gate and the `scheduling.k8s.io/v1alpha3` [API group](https://kubernetes.io/docs/concepts/overview/kubernetes-api/#api-groups-and-versioning "A set of related paths in the Kubernetes API.")
are enabled, `CompositePodGroupTemplates` in a Workload and the `CompositePodGroup` objects also
declare a scheduling policy.

While a scheduling policy in a `PodGroup` governs a collection of individual Pods, a
`CompositePodGroup` scheduling policy governs its direct **child groups** (which can be both
`CompositePodGroup` and `PodGroup` objects).