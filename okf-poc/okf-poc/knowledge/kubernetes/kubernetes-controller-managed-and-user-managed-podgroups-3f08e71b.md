---
id: kubernetes-controller-managed-and-user-managed-podgroups-3f08e71b
type: concept
title: Controller-managed and user-managed PodGroups
description: In most cases, workload controllers (for example, Job) create `PodGroups`
  automatically
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/podgroup-api/lifecycle/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

## Controller-managed and user-managed PodGroups

In most cases, workload controllers (for example, Job) create `PodGroups` automatically
(controller-managed). The controller determines the `podGroupName` for each Pod
at creation time, similar to how a `DaemonSet` sets node affinity per Pod.

If you need more control over naming and lifecycle, you can create `PodGroup` objects directly and set
`spec.schedulingGroup.podGroupName` in your Pod templates yourself
(user-managed). This gives you full control over `PodGroup` creation and naming.