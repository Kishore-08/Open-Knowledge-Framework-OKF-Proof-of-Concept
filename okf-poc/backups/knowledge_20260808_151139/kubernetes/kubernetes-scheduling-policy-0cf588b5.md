---
id: kubernetes-scheduling-policy-0cf588b5
type: concept
title: Scheduling policy
description: Each PodGroup carries a [scheduling policy](https://kubernetes.io/docs/concepts/workloads/workload-api/policies/)
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/podgroup-api/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Scheduling policy

Each PodGroup carries a [scheduling policy](https://kubernetes.io/docs/concepts/workloads/workload-api/policies/)
(`basic` or `gang`) in `spec.schedulingPolicy`. When a workload controller creates
the PodGroup, this policy is copied from the Workload's PodGroupTemplate at creation time.
For standalone PodGroups, you set the policy directly.

```
spec:
  schedulingPolicy:
    gang:
      minCount: 4
```