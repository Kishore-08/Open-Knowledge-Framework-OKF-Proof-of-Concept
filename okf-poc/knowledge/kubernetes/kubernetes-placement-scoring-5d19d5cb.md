---
id: kubernetes-placement-scoring-5d19d5cb
type: concept
title: Placement scoring
description: When scoring a candidate placement for a `CompositePodGroup`, the scoring
  plugins apply similar
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/scheduling-eviction/topology-aware-scheduling/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

### Placement scoring

When scoring a candidate placement for a `CompositePodGroup`, the scoring plugins apply similar
logic to the single-level `PodGroup` case:

- `PodGroupPodsCount`: Scores candidate placements based on the total number of Pods (both
  already scheduled and newly assumed) across all descendant leaf `PodGroups` of that
  `CompositePodGroup`. Candidate placements capable of accommodating a higher total number of Pods
  across the subhierarchy receive higher scores.
- `NodeResourcesFit`: Aggregates the resource requests of all proposed Pods across all descendant
  `PodGroups` of that `CompositePodGroup` and evaluates resource utilization across all nodes within
  the candidate placement's domain.