---
id: kubernetes-disruption-mode-types-98ef819e
type: concept
title: Disruption mode types
description: In v1.36, the `priority` or `disruptionMode` fields of the PodGroup are
  only respected
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/workload-api/disruption-and-priority/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

## Disruption mode types

#### Note:

In v1.36, the `priority` or `disruptionMode` fields of the PodGroup are only respected
by [workload-aware preemption](https://kubernetes.io/docs/concepts/scheduling-eviction/workload-aware-preemption/).
During the pod scheduling phase, the scheduler does not take into account
the `priority` or `disruptionMode` fields of the PodGroup. This limitation no longer
applies in v1.37.

The API supports two disruption modes: `Single` and `All`.
The default one is `Single`.

### Single

The `Single` mode instructs the scheduler to treat all Pods in the group as separate entities,
allowing independent disruption of a single pod from a PodGroup.

### All

The `All` mode emphasizes "all-or-nothing" semantics for disruption.
It instructs the scheduler that all pods from the PodGroup have to be disrupted together.