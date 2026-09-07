---
id: kubernetes-parent-group-0cf588b5
type: concept
title: Parent group
description: 'FEATURE STATE:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/podgroup-api/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

## Parent group

FEATURE STATE:
`Kubernetes v1.37 [alpha]`(disabled by default)

When the [`CompositePodGroup`](https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/#CompositePodGroup)
feature gate is enabled, a `PodGroup` can act as a leaf node in a multi-level group hierarchy that
consists of `PodGroups` and `CompositePodGroups`. A `PodGroup` can specify its parent group using the
`spec.parentCompositePodGroupName` field. Organizing a workload into a hierarchy of groups can be
used to express multi-level gang scheduling requirements, multi-level topology constraints and
disruption fate-sharing across parts of the workload.

For more details on hierarchical group structures and multi-level gang scheduling, see the
[CompositePodGroup API](https://kubernetes.io/docs/concepts/workloads/compositepodgroup-api/) overview.

#### Note:

A `PodGroup` that specifies `spec.parentCompositePodGroupName` must also specify `spec.workloadRef`,
linking the `PodGroup` back to its template in the `Workload`. Standalone `PodGroup` objects
(created without a `spec.workloadRef`) are not allowed to specify a parent `CompositePodGroup`.