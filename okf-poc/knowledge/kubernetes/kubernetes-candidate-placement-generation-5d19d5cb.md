---
id: kubernetes-candidate-placement-generation-5d19d5cb
type: concept
title: Candidate placement generation
description: For workloads defined with a `CompositePodGroup` hierarchy, the `TopologyPlacement`
  plugin generates
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/scheduling-eviction/topology-aware-scheduling/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

### Candidate placement generation

For workloads defined with a `CompositePodGroup` hierarchy, the `TopologyPlacement` plugin generates
candidate placements top-down across the group hierarchy by successive subdivision:

- For a root `CompositePodGroup`, `TopologyPlacement` generates candidate placements across all
  available cluster nodes by grouping nodes based on the distinct values of the requested topology
  `key`.
- For a child `CompositePodGroup` or leaf `PodGroup`, `TopologyPlacement` generates candidate
  placements confined in the placement assumed by the parent group. It subdivides the set of nodes
  from the parent group's placement by grouping those nodes based on the child group's requested
  topology `key`.

#### Note:

If a topology constraint is not specified, the `TopologyPlacement` plugin generates a single
candidate placement equivalent to the parent placement.

Similarly, if the root group does not specify any topology constraint, the plugin generates a single
candidate placement corresponding to all available nodes in the cluster. This is also true for
single-level workloads using the `PodGroup` API where no topology constraint is specified.