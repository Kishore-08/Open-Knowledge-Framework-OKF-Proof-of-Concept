---
id: kubernetes-traces-c2bd57dc
type: concept
title: Traces
description: Traces capture how requests moves across Kubernetes components and applications,
  linking latency, timing and relationships between operations.By collecting traces,
  you can visualize end-to-end request
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/cluster-administration/observability/
updated_at: '2026-08-13'
created_at: '2026-08-13'
---

## Traces

Traces capture how requests moves across Kubernetes components and applications, linking latency, timing and relationships between operations.By collecting traces, you can visualize end-to-end request flow, diagnose performance issues, and identify bottlenecks or unexpected interactions in the control plane, add-ons, or applications.

Kubernetes 1.36 can export spans over the [OpenTelemetry Protocol](https://kubernetes.io/docs/concepts/cluster-administration/system-traces/) (OTLP), either directly via built-in gRPC exporters or by forwarding them through an OpenTelemetry Collector.

The OpenTelemetry Collector receives spans from components and applications, processes them (for example by applying sampling or redaction), and forwards them to a tracing backend for storage and analysis.

Figure 4 outlines a typical distributed tracing pipeline.

```
flowchart LR
    subgraph Sources
        A[Control plane spans]
        B[Application spans]
    end
    A --> X[OTLP exporter]
    B --> X
    X --> COL[OpenTelemetry Collector]
    COL --> TS[(Tracing backend)]
    TS --> V[Visualization and analysis]
```

*Figure 4. Components of a typical Kubernetes traces pipeline.*

See [Common observability tools - tracing tools](https://kubernetes.io/docs/concepts/cluster-administration/observability/#tracing-tools) for tracing collectors and backends.

#### See Also

- [System traces for Kubernetes components](https://kubernetes.io/docs/concepts/cluster-administration/system-traces/)
- [OpenTelemetry Collector getting started guide](https://opentelemetry.io/docs/collector/getting-started/)
- [Monitoring and tracing tasks](https://kubernetes.io/docs/tasks/debug/monitoring/)