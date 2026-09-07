---
id: kubernetes-composite-building-blocks-497d3b3e
type: concept
title: Composite building blocks
description: Multi-level controllers that orchestrate other controllers (for example,
  JobSet
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/workload-api/workloadbuilder/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

### Composite building blocks

Multi-level controllers that orchestrate other controllers (for example, JobSet
creating Jobs) coordinate a *group of groups*. For that layer, the API provides an
analogous set of primitives prefixed with `WorkloadCompositePodGroup...`
(for example `WorkloadCompositePodGroupSchedulingPolicy`). They follow the same shapes as
the leaf-level blocks, except the composite gang policy uses `minGroupCount` (the minimum
number of child groups that must be schedulable together) in place of the leaf's
`minCount`. Keeping leaf and composite types distinct lets each hierarchy level evolve
independently.