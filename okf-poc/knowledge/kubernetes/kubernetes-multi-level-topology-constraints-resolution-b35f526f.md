---
id: kubernetes-multi-level-topology-constraints-resolution-b35f526f
type: concept
title: Multi-level topology constraints resolution
description: Every group inside a `CompositePodGroup` hierarchy can specify a topology
  constraint which
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/workload-api/topology-aware-scheduling/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

### Multi-level topology constraints resolution

Every group inside a `CompositePodGroup` hierarchy can specify a topology constraint which
guarantees that all descendant Pods of that group will be scheduled in the same topology domain,
matching that group's constraint.

During [hierarchical scheduling](https://kubernetes.io/docs/concepts/scheduling-eviction/podgroup-scheduling/), the
scheduler resolves these constraints in a **top-down** manner. Specifically, topology domains that
are considered during scheduling of a child group are confined within a topology domain that
corresponds to the placement assumed by the parent group.

Kubernetes does not impose any strict requirements on the physical hierarchy of topology labels - topology
keys are arbitrary node labels. However, the order in which you specify topology constraints from
parent to child determines the order in which the scheduler subdivides topology domains.

#### Note:

As of Kubernetes v1.37, you can specify only a single topology constraint in each
`CompositePodGroup`.