---
id: kubernetes-kubelet-metrics-36c52094
type: concept
title: '`kubelet` metrics'
description: When a Pod bound to a node must have a ResourceClaim satisfied, kubelet
  calls
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/cluster-administration/dra/
updated_at: '2026-08-13'
created_at: '2026-08-13'
---

### `kubelet` metrics

When a Pod bound to a node must have a ResourceClaim satisfied, kubelet calls
the `NodePrepareResources` and `NodeUnprepareResources` methods of the DRA
driver. You can observe this behavior from the kubelet's point of view with the
following metrics.

- Kubelet NodePrepareResources: Monitor `histogram_quantile(0.99,
  sum(rate(dra_operations_duration_seconds_bucket{operation_name="PrepareResources"}[5m]))
  by (le))`.
- Kubelet NodeUnprepareResources: Track `histogram_quantile(0.99,
  sum(rate(dra_operations_duration_seconds_bucket{operation_name="UnprepareResources"}[5m]))
  by (le))`.