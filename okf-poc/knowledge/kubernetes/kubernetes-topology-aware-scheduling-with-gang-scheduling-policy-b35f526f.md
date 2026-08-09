---
id: kubernetes-topology-aware-scheduling-with-gang-scheduling-policy-b35f526f
type: concept
title: Topology-aware scheduling with gang scheduling policy
description: When applied to PodGroups with `gang` scheduling policy, TAS simulates
  the potential assignment
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/workload-api/topology-aware-scheduling/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

## Topology-aware scheduling with gang scheduling policy

When applied to PodGroups with `gang` scheduling policy, TAS simulates the potential assignment
(*placement*) of the full group of pods at once. It guarantees that at least the specified
`minCount` pods can fit together into the same topology domain before committing resources.
If no feasible placement is found, the entire PodGroup becomes unschedulable.

This is the recommended approach for workloads like distributed AI and ML training that strictly
require proximity to minimize inter-pod communication latency.

If new pods are added to the PodGroup where some pods are already scheduled (for example, if pods
are recreated), the scheduler will force all new incoming pods to land on the exact same topology
domain where the existing pods currently reside. If that specific domain lacks sufficient capacity
for the new pods, the pods will remain pending - even if it means that less than `minCount` pods
are scheduled at this point.

#### Note:

As of v1.36 Topology-Aware Scheduling does not trigger workload or pod preemption. If no
feasible placement can be found without triggering preemption, the PodGroup becomes unschedulable.