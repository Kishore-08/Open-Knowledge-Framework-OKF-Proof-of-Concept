---
id: kubernetes-limitations-3f08e71b
type: concept
title: Limitations
description: '- All Pods in a `PodGroup` must use the same `.spec.schedulerName`.'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/podgroup-api/lifecycle/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

## Limitations

- All Pods in a `PodGroup` must use the same `.spec.schedulerName`.
  If a mismatch is detected, the scheduler rejects all Pods in the group as unschedulable.
- The `spec.schedulingPolicy.gang.minCount` field on a PodGroup is immutable.
  Once created, you cannot change the minimum number of Pods that must be schedulable for the group to be admitted.
- The `spec.schedulingGroup` field on a Pod is immutable.
  Once set, a Pod cannot move to a different PodGroup.
- The maximum number of `PodGroupTemplates` in a single `Workload` is 8.
- The `PodGroupScheduled` condition reflects the outcome of the initial scheduling
  attempt only. Once the condition is set to `True`, the scheduler does not update it
  if Pods later fail, are evicted, or stop running.