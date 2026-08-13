---
id: kubernetes-support-for-metrics-apis-cdcbb833
type: concept
title: Support for metrics APIs
description: By default, the HorizontalPodAutoscaler controller retrieves metrics
  from a series of APIs.
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/autoscaling/horizontal-pod-autoscale/
updated_at: '2026-08-13'
created_at: '2026-08-13'
---

## Support for metrics APIs

By default, the HorizontalPodAutoscaler controller retrieves metrics from a series of APIs.
In order for it to access these APIs, cluster administrators must ensure that:

- The [API aggregation layer](https://kubernetes.io/docs/tasks/extend-kubernetes/configure-aggregation-layer/) is enabled.
- The corresponding APIs are registered:

  - For resource metrics, this is the `metrics.k8s.io` [API](https://kubernetes.io/docs/reference/external-api/metrics.v1beta1/),
    generally provided by [metrics-server](https://github.com/kubernetes-sigs/metrics-server).
    It can be launched as a cluster add-on.
  - For custom metrics, this is the `custom.metrics.k8s.io` [API](https://kubernetes.io/docs/reference/external-api/custom-metrics.v1beta2/).
    It's provided by "adapter" API servers provided by metrics solution vendors.
    Check with your metrics pipeline to see if there is a Kubernetes metrics adapter available.
  - For external metrics, this is the `external.metrics.k8s.io` [API](https://kubernetes.io/docs/reference/external-api/external-metrics.v1beta1/).
    It may be provided by the custom metrics adapters provided above.

For more information on these different metrics paths and how they differ please see the relevant design proposals for
[the HPA V2](https://git.k8s.io/design-proposals-archive/autoscaling/hpa-v2.md),
[custom.metrics.k8s.io](https://git.k8s.io/design-proposals-archive/instrumentation/custom-metrics-api.md)
and [external.metrics.k8s.io](https://git.k8s.io/design-proposals-archive/instrumentation/external-metrics-api.md).

For examples of how to use them see
[the walkthrough for using custom metrics](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale-walkthrough/#autoscaling-on-multiple-metrics-and-custom-metrics)
and [the walkthrough for using external metrics](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale-walkthrough/#autoscaling-on-metrics-not-related-to-kubernetes-objects).