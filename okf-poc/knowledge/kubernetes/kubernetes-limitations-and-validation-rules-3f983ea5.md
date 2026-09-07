---
id: kubernetes-limitations-and-validation-rules-3f983ea5
type: concept
title: Limitations and validation rules
description: '- **Consistent scheduler name**: All Pods across an entire `CompositePodGroup`
  hierarchy must use'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/compositepodgroup-api/lifecycle/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

## Limitations and validation rules

- **Consistent scheduler name**: All Pods across an entire `CompositePodGroup` hierarchy must use
  the same `spec.schedulerName`. If a mismatch is detected, the scheduler rejects the hierarchy as
  unschedulable.
- **Consistent priority**: All Pods across an entire `CompositePodGroup` hierarchy must specify the
  same value of `spec.priority` which must be equal to the priority specified by the root group. If
  a mismatch is detected, the scheduler rejects the hierarchy as unschedulable.
- **Consistent preemption policy**: All Pods across an entire `CompositePodGroup` hierarchy must use
  the same `spec.preemptionPolicy`. In addition, when the
  [PodGroupPreemptionPolicy](https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/podgroup-preemption-policy/)
  feature gate is enabled, the root group's preemption policy must be equal to the one specified by
  the Pods. If a mismatch is detected, the scheduler rejects the hierarchy as unschedulable.
- **Maximum nesting depth**: The group-template hierarchy supports a maximum depth of 4 levels.
- **List item limit**: The maximum number of child `CompositePodGroupTemplates` and
  `PodGroupTemplates` at any level of a `Workload` is 8.
- **Immutable gang group count**: The `spec.schedulingPolicy.gang.minGroupCount` field on a
  `CompositePodGroup` is immutable after creation.
- **Immutable hierarchy references**: `spec.parentCompositePodGroupName` on groups and
  `spec.schedulingGroup` on Pods are immutable once set.