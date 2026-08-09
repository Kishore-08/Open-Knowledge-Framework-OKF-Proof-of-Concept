---
id: kubernetes-topology-aware-scheduling-with-basic-scheduling-policy-b35f526f
type: concept
title: Topology-aware scheduling with basic scheduling policy
description: Using TAS with `basic` scheduling policy may exhibit inconsistent behavior.
  The scheduler may only
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/workload-api/topology-aware-scheduling/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

## Topology-aware scheduling with basic scheduling policy

Using TAS with `basic` scheduling policy may exhibit inconsistent behavior. The scheduler may only
observe a subset of pods when entering the PodGroup scheduling cycle - therefore placement
feasibility is only evaluated for the observed pods, rather than the entire PodGroup. To partially
mitigate this limitation, you can use scheduling gates to hold off PodGroup scheduling until all
pods within the PodGroup are in the scheduling queue.

If no feasible placement is found for the entire PodGroup, only a subset of pods may be scheduled,
and they are guaranteed to meet the scheduling constraints.

If new pods are added to the PodGroup where some pods are already scheduled, the scheduler will act
the same as in case of `gang` policy - forcing the new pods into the same domain, unless there is
insufficient capacity (in which case the new pods will remain pending).