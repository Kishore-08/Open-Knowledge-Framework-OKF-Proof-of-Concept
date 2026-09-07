---
id: kubernetes-workload-reference-cabfab21
type: concept
title: Workload reference
description: The `spec.workloadRef` field links the `CompositePodGroup` back to the
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/compositepodgroup-api/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

### Workload reference

The `spec.workloadRef` field links the `CompositePodGroup` back to the
`CompositePodGroupTemplate` in the `Workload` object it was derived from.

```
spec:
  workloadRef:
    workloadName: hierarchical-workload
    templateName: replica-group
```