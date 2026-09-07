---
id: kubernetes-compositepodgroup-priority-98ef819e
type: concept
title: CompositePodGroup priority
description: 'FEATURE STATE:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/workload-api/disruption-and-priority/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

### CompositePodGroup priority

FEATURE STATE:
`Kubernetes v1.37 [alpha]`(disabled by default)

`CompositePodGroup` API has `priorityClassName` and `priority` fields as well and their resolution
is performed in the same way as for the `PodGroups`, through the priority admission controller.

The priority of a root `CompositePodGroup` acts as the authoritative priority for all child groups
and Pods within its hierarchy during
[workload-aware preemption](https://kubernetes.io/docs/concepts/scheduling-eviction/workload-aware-preemption/) events.
All Pods within a single group hierarchy must share the exact same priority and must be equal to the
priority of the root `CompositePodGroup`.

The value of priority is also used for the ordering of root `CompositePodGroups` in the scheduling
active queue.

#### Note:

In v1.37, the scheduler doesn't validate if the non-root groups have priority value that is equal to
the priority of the root `CompositePodGroup`.