---
id: kubernetes-basic-policy-217a0ad5
type: concept
title: Basic policy
description: The `basic` policy instructs the scheduler to evaluate all Pods on a
  best-effort basis.
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/workload-api/policies/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Basic policy

The `basic` policy instructs the scheduler to evaluate all Pods on a best-effort basis.
Unlike the `gang` policy, a PodGroup using the `basic` policy is considered feasible
regardless of how many of its Pods are currently schedulable.

The primary reason to use the `basic` policy is to organize Pods into a group for better
observability and management, while still evaluating them together within a single, atomic
[PodGroup scheduling cycle](https://kubernetes.io/docs/concepts/scheduling-eviction/podgroup-scheduling/#podgroup-scheduling-cycle).

This policy is suited for groups that do not require simultaneous startup but logically
belong together, or to open the way for group-level constraints that do not imply
"all-or-nothing" placement.

```
schedulingPolicy:
  basic: {}
```