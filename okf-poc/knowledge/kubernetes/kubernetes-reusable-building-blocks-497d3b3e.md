---
id: kubernetes-reusable-building-blocks-497d3b3e
type: concept
title: Reusable building blocks
description: The building blocks are strongly-typed Go structs in the `scheduling.k8s.io/v1alpha3`
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/workload-api/workloadbuilder/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

## Reusable building blocks

The building blocks are strongly-typed Go structs in the `scheduling.k8s.io/v1alpha3`
API group. They are meant for *controller authors*: a controller embeds these structs into
its own API type as fields, and the `workloadbuilder` library compiles them. The type names
follow two conventions: leaf-level types are prefixed `WorkloadPodGroup...` (for example,
`WorkloadPodGroupSchedulingPolicy`) and the multi-level variants - `WorkloadCompositePodGroup...`.

Each controller chooses the field names and structure that are idiomatic for its own API, so
these blocks impose no fixed top-level shape. Although not strictly enforced, reusing the
standard field names and structure is recommended, so that a user who has configured gang
scheduling on one controller's resource recognizes the same options on another's.

To adopt the building blocks, a controller adds the ones it wants to support as fields on
its own types. For example, the [Job](https://kubernetes.io/docs/concepts/workloads/controllers/job/) API groups
all four of them into a single type reachable at `spec.scheduling`:

```
type JobSchedulingConfiguration struct {
    SchedulingPolicy      *schedulingv1alpha3.WorkloadPodGroupSchedulingPolicy
    SchedulingConstraints *schedulingv1alpha3.WorkloadPodGroupSchedulingConstraints
    DisruptionMode        *schedulingv1alpha3.WorkloadPodGroupDisruptionMode
    ResourceClaims        []schedulingv1alpha3.WorkloadPodGroupResourceClaim
}
```

A different controller might nest the same blocks per component of a multi-part workload,
or support only a subset of them.