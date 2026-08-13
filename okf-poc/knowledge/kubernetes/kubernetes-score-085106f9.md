---
id: kubernetes-score-085106f9
type: concept
title: Score
description: These plugins are used to rank nodes that have passed the filtering phase.
  The
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/scheduling-eviction/scheduling-framework/
updated_at: '2026-08-13'
created_at: '2026-08-13'
---

### Score

These plugins are used to rank nodes that have passed the filtering phase. The
scheduler will call each scoring plugin for each node. There will be a well
defined range of integers representing the minimum and maximum scores. After the
[NormalizeScore](https://kubernetes.io/docs/concepts/scheduling-eviction/scheduling-framework/#normalize-scoring) phase, the scheduler will combine node
scores from all plugins according to the configured plugin weights.

#### Capacity scoring

FEATURE STATE:
`Kubernetes v1.33 [alpha]`(disabled by default)

The feature gate `VolumeCapacityPriority` was used in v1.32 to support storage that are
statically provisioned. Starting from v1.33, the new feature gate `StorageCapacityScoring`
replaces the old `VolumeCapacityPriority` gate with added support to dynamically provisioned storage.
When `StorageCapacityScoring` is enabled, the VolumeBinding plugin in the kube-scheduler is extended
to score Nodes based on the storage capacity on each of them.
This feature is applicable to CSI volumes that supported [Storage Capacity](https://kubernetes.io/docs/concepts/storage/storage-capacity/),
including local storage backed by a CSI driver.