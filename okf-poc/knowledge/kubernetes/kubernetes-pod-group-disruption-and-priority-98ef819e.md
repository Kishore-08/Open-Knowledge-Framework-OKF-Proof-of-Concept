---
id: kubernetes-pod-group-disruption-and-priority-98ef819e
type: concept
title: Pod Group Disruption and Priority
description: 'FEATURE STATE:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/workload-api/disruption-and-priority/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

# Pod Group Disruption and Priority

FEATURE STATE:
`Kubernetes v1.37 [beta]`(disabled by default)

PodGroup can declare a disruption mode. This mode dictates how
the scheduler can disrupt a running PodGroup, for example to accommodate
a higher priority PodGroup. A PodGroup also has a priority,
which overrides the priority of the individual pods from the group
for [workload-aware preemption](https://kubernetes.io/docs/concepts/scheduling-eviction/workload-aware-preemption/) events.