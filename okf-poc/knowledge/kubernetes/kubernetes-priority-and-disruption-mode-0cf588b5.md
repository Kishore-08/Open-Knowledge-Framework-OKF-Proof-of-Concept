---
id: kubernetes-priority-and-disruption-mode-0cf588b5
type: concept
title: Priority and Disruption mode
description: Each PodGroup can also define its own `spec.priority`, `spec.preemptionPolicy`
  and
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/podgroup-api/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

### Priority and Disruption mode

Each PodGroup can also define its own `spec.priority`, `spec.preemptionPolicy` and
`spec.disruptionMode`. Priority and preemption policy are set using a
`spec.priorityClassName` field, which points to a `PriorityClass` resource.
See
[Pod Group Disruption and Priority](https://kubernetes.io/docs/concepts/workloads/workload-api/disruption-and-priority/)
for detailed description of these fields.

When a workload controller creates the PodGroup, these fields are copied from
the Workload's PodGroupTemplate at creation time. For standalone PodGroups,
you set the fields directly.

```
spec:
  disruptionMode:
    all: {}
  priorityClassName: high-priority
```