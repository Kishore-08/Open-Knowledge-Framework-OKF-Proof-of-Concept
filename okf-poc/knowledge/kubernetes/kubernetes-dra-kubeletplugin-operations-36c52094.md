---
id: kubernetes-dra-kubeletplugin-operations-36c52094
type: concept
title: DRA kubeletplugin operations
description: DRA drivers implement the [`kubeletplugin` package
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/cluster-administration/dra/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

### DRA kubeletplugin operations

DRA drivers implement the [`kubeletplugin` package
interface](https://pkg.go.dev/k8s.io/dynamic-resource-allocation/kubeletplugin)
which surfaces its own metric for the underlying gRPC operation
`NodePrepareResources` and `NodeUnprepareResources`. You can observe this
behavior from the point of view of the internal kubeletplugin with the following
metrics.

- DRA kubeletplugin gRPC NodePrepareResources operation: Observe `histogram_quantile(0.99,
  sum(rate(dra_grpc_operations_duration_seconds_bucket{method_name=~".*NodePrepareResources"}[5m]))
  by (le))`.
- DRA kubeletplugin gRPC NodeUnprepareResources operation: Observe `histogram_quantile(0.99,
  sum(rate(dra_grpc_operations_duration_seconds_bucket{method_name=~".*NodeUnprepareResources"}[5m]))
  by (le))`.