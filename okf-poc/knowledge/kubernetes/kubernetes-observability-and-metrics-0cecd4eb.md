---
id: kubernetes-observability-and-metrics-0cecd4eb
type: concept
title: Observability and metrics
description: You can monitor the behavior and health of the resource managers across
  both
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/resource-management/pod-level-resource-managers/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

## Observability and metrics

You can monitor the behavior and health of the resource managers across both
container-level and pod-level allocations using the following `kubelet`
metrics (enabled via the `PodLevelResourceManagers` feature gate):

- `resource_manager_allocations_total`: Counts the total number of exclusive
  resource allocations performed by a manager. The `source` label ("pod" or
  "node") distinguishes between allocations drawn from the node-level pool
  versus a pre-allocated pod-level pool.
- `resource_manager_allocation_errors_total`: Counts errors encountered during
  exclusive resource allocation, distinguished by the intended allocation
  `source` ("pod" or "node").
- `resource_manager_container_assignments`: Tracks the cumulative number of
  containers that will be granted a specific type of resource assignment. The
  `assignment_type` label ("node\_exclusive", "pod\_exclusive", "pod\_shared")
  provides visibility into how many containers are running with exclusive
  resources (from the node or pod pool) versus the pod-level shared pool.