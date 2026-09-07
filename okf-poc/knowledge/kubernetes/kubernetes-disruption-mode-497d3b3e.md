---
id: kubernetes-disruption-mode-497d3b3e
type: concept
title: Disruption mode
description: The disruption mode block selects whether the group's Pods may be disrupted
  individually
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/workload-api/workloadbuilder/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

### Disruption mode

The disruption mode block selects whether the group's Pods may be disrupted individually
(`single`) or only as a unit (`all`), corresponding to the `Pod` and `PodGroup` disruption
modes documented in
[Pod group disruption and priority](https://kubernetes.io/docs/concepts/workloads/workload-api/disruption-and-priority/).

The library rejects combinations that are not meaningful. For example, prevent `all` disruption mode
for PodGroups with BasicSchedulingPolicy, because the preemption unit must not be larger than the
scheduling unit - a group scheduled pod-by-pod has no group-level unit to preempt or disrupt.