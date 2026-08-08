---
id: kubernetes-node-and-container-level-metric-statistics-9edb5061
type: concept
title: Node and container level metric statistics
description: Kubelet now collects node and container level metric statistics,
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/cluster-administration/swap-memory-management/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Node and container level metric statistics

Kubelet now collects node and container level metric statistics,
which can be accessed at the `/metrics/resource` (which is used mainly by monitoring
tools like Prometheus) and `/stats/summary` (which is used mainly by Autoscalers) kubelet HTTP endpoints.
This allows clients who can directly request the kubelet to
monitor swap usage and remaining swap memory when using `LimitedSwap`.
Additionally, a `machine_swap_bytes` metric has been added to cadvisor to show
the total physical swap capacity of the machine.
See [this page](https://kubernetes.io/docs/reference/instrumentation/node-metrics/) for more info.

For example, these `/metrics/resource` are supported:

- `node_swap_usage_bytes`: Current swap usage of the node in bytes.
- `container_swap_usage_bytes`: Current amount of the container swap usage in bytes.
- `container_swap_limit_bytes`: Current amount of the container swap limit in bytes.