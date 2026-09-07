---
id: kubernetes-creation-ordering-3f983ea5
type: concept
title: Creation ordering
description: To ensure proper hierarchy resolution and scheduling, workload controllers
  create resources in a
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/compositepodgroup-api/lifecycle/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

## Creation ordering

To ensure proper hierarchy resolution and scheduling, workload controllers create resources in a
top-down order:

1. **`Workload`**: Defines static templates (`CompositePodGroupTemplates` and `PodGroupTemplates`).
2. **Root `CompositePodGroup`**: Created with `spec.workloadRef` pointing to the root template in
   the `Workload`.
3. **Descendant `CompositePodGroups` and `PodGroups`**: Created top-down. Each child group specifies
   its parent by using `spec.parentCompositePodGroupName` and its template using `spec.workloadRef`.
4. **`Pods`**: Created with `spec.schedulingGroup.podGroupName` pointing to their leaf `PodGroup`.

If a group references a parent `CompositePodGroup` that does not exist, or if a Pod references
a `PodGroup` that has not yet been created, the scheduler holds off scheduling until all parent
resources in the hierarchy exist.