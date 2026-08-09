---
id: kubernetes-scheduling-framework-tas-plugins-configuration-5d19d5cb
type: concept
title: 'Scheduling framework: TAS plugins configuration'
description: 'The scheduler includes new and extended in-tree plugins that implement
  the TAS extension points:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/scheduling-eviction/topology-aware-scheduling/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

## Scheduling framework: TAS plugins configuration

The scheduler includes new and extended in-tree plugins that implement the TAS extension points:

- `TopologyPlacement`: Implements the `PlacementGeneratePlugin` interface. It generates candidate
  placements by grouping nodes based on the distinct values of the requested topology `key` (defined
  in the PodGroup).
- `NodeResourcesFit`: Extended to implement the `PlacementScorePlugin` interface. Following
  similar logic to standard pod bin-packing, it scores placements based on the allocation ratio
  across all nodes within the placement. It uses the `MostAllocated` strategy to maximize resource
  utilization within a placement, and it inherits resource weights from the standard pod-by-pod
  plugin settings.
- `PodGroupPodsCount`: Implements the `PlacementScorePlugin` interface. It scores candidate
  placements based on the total number of pods in the PodGroup that you can successfully schedule.