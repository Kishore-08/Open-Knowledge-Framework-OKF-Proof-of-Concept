---
id: kubernetes-metrics-c2bd57dc
type: concept
title: Metrics
description: 'Kubernetes components emit metrics in [Prometheus format](https://prometheus.io/docs/instrumenting/exposition_formats/)
  from their `/metrics` endpoints, including:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/cluster-administration/observability/
updated_at: '2026-08-13'
created_at: '2026-08-13'
---

## Metrics

Kubernetes components emit metrics in [Prometheus format](https://prometheus.io/docs/instrumenting/exposition_formats/) from their `/metrics` endpoints, including:

- kube-controller-manager
- kube-proxy
- kube-apiserver
- kube-scheduler
- kubelet

The kubelet also exposes metrics at `/metrics/cadvisor`, `/metrics/resource`, and `/metrics/probes`, and add-ons such as [kube-state-metrics](https://kubernetes.io/docs/concepts/cluster-administration/kube-state-metrics/) enrich those control plane signals with Kubernetes object status.

A typical Kubernetes metrics pipeline periodically scrapes these endpoints and stores the samples in a time series database (for example with Prometheus).

See the [system metrics guide](https://kubernetes.io/docs/concepts/cluster-administration/system-metrics/) for details and configuration options.

Figure 2 outlines a common Kubernetes metrics pipeline.

```
flowchart LR
    C[Cluster components] --> P[Prometheus scraper]
    P --> TS[(Time series storage)]
    TS --> D[Dashboards and alerts]
    TS --> A[Automated actions]
```

*Figure 2. Components of a typical Kubernetes metrics pipeline.*

For multi-cluster or multi-cloud visibility, distributed time series databases (for example Thanos or Cortex) can complement Prometheus.

See [Common observability tools - metrics tools](https://kubernetes.io/docs/concepts/cluster-administration/observability/#metrics-tools) for metrics scrapers and time series databases.

#### See Also

- [System metrics for Kubernetes components](https://kubernetes.io/docs/concepts/cluster-administration/system-metrics/)
- [Resource usage monitoring with metrics-server](https://kubernetes.io/docs/tasks/debug/debug-cluster/resource-usage-monitoring/)
- [kube-state-metrics concept](https://kubernetes.io/docs/concepts/cluster-administration/kube-state-metrics/)
- [Resource metrics pipeline overview](https://kubernetes.io/docs/tasks/debug/debug-cluster/resource-metrics-pipeline/)