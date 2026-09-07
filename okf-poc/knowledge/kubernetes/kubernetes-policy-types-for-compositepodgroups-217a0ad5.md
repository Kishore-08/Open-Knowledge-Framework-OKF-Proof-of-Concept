---
id: kubernetes-policy-types-for-compositepodgroups-217a0ad5
type: concept
title: Policy types for CompositePodGroups
description: Similar to `PodGroups`, the `spec.schedulingPolicy` field of a `CompositePodGroup`
  supports two
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/workload-api/policies/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

### Policy types for CompositePodGroups

Similar to `PodGroups`, the `spec.schedulingPolicy` field of a `CompositePodGroup` supports two
types:

- **`basic`**: Child groups within the `CompositePodGroup` are evaluated and admitted independently.
- **`gang`**: Enforces multi-level all-or-nothing scheduling across child groups. The
  `CompositePodGroup` is schedulable only if at least `minGroupCount` child groups can be scheduled
  simultaneously.

```
schedulingPolicy:
  gang:
    # The minimum number of child groups that must be schedulable
    # simultaneously for this composite group to be admitted.
    minGroupCount: 2
```