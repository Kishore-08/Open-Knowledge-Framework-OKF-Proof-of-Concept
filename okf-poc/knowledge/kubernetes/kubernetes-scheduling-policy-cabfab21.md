---
id: kubernetes-scheduling-policy-cabfab21
type: concept
title: Scheduling policy
description: Each `CompositePodGroup` carries a [scheduling policy](https://kubernetes.io/docs/concepts/workloads/workload-api/policies/)
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/compositepodgroup-api/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

### Scheduling policy

Each `CompositePodGroup` carries a [scheduling policy](https://kubernetes.io/docs/concepts/workloads/workload-api/policies/)
(`basic` or `gang`) in `spec.schedulingPolicy`. When a workload controller creates a
`CompositePodGroup`, this policy is copied from the `Workload`'s `CompositePodGroupTemplate`
at creation time.

For a `gang` policy on a `CompositePodGroup`, the `minGroupCount` field specifies the
minimum number of child groups that must be schedulable simultaneously:

```
spec:
  schedulingPolicy:
    gang:
      minGroupCount: 2
```