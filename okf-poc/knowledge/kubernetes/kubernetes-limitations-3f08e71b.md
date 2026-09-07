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
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

## Limitations

- All Pods in a `PodGroup` must use the same `.spec.schedulerName`.
  If a mismatch is detected, the scheduler rejects all Pods in the group as unschedulable.
- All Pods in a `PodGroup` must use the same `.spec.priority`.
  If a mismatch is detected, the scheduler rejects all Pods in the group as unschedulable.
- All Pods in a `PodGroup` must use the same `.spec.preemptionPolicy`.
  If a mismatch is detected, the scheduler rejects all Pods in the group as unschedulable.
- The `spec.schedulingGroup` field on a Pod is immutable.
  Once set, a Pod cannot move to a different PodGroup.
- The maximum number of `PodGroupTemplates` in a single `Workload` is 8.
- The scheduler does not update status information regarding the ongoing operational state of a PodGroup
  or subsequent scheduling attempts after initial placement. Consequently, the PodGroup status is not updated
  when existing Pods fail, are evicted, or terminate, or when newly observed Pods fail to schedule.