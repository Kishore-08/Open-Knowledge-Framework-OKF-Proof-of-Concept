---
id: kubernetes-kube-controller-manager-metrics-36c52094
type: concept
title: '`kube-controller-manager` metrics'
description: The following metrics look closely at the internal ResourceClaim controller
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/cluster-administration/dra/
updated_at: '2026-08-13'
created_at: '2026-08-13'
---

### `kube-controller-manager` metrics

The following metrics look closely at the internal ResourceClaim controller
managed by the `kube-controller-manager` component.

- Workqueue Add Rate: Monitor `sum(rate(workqueue_adds_total{name="resource_claim"}[5m]))` to gauge how quickly items are added to the ResourceClaim controller.
- Workqueue Depth: Track
  `sum(workqueue_depth{endpoint="kube-controller-manager",
  name="resource_claim"})` to identify any backlogs in the ResourceClaim
  controller.
- Workqueue Work Duration: Observe `histogram_quantile(0.99,
  sum(rate(workqueue_work_duration_seconds_bucket{name="resource_claim"}[5m]))
  by (le))` to understand the speed at which the ResourceClaim controller
  processes work.

If you are experiencing low Workqueue Add Rate, high Workqueue Depth, and/or
high Workqueue Work Duration, this suggests the controller isn't performing
optimally. Consider tuning parameters like QPS, burst, and CPU/memory
configurations.

If you are experiencing high Workequeue Add Rate, high Workqueue Depth, but
reasonable Workqueue Work Duration, this indicates the controller is processing
work, but concurrency might be insufficient. Concurrency is hardcoded in the
controller, so as a cluster administrator, you can tune for this by reducing the
pod creation QPS, so the add rate to the resource claim workqueue is more
manageable.