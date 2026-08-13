---
id: kubernetes-scaling-on-custom-metrics-cdcbb833
type: concept
title: Scaling on custom metrics
description: 'FEATURE STATE:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/autoscaling/horizontal-pod-autoscale/
updated_at: '2026-08-13'
created_at: '2026-08-13'
---

## Scaling on custom metrics

FEATURE STATE:
`Kubernetes v1.23 [stable]`

(the `autoscaling/v2beta2` API version previously provided this ability as a beta feature)

Provided that you use the `autoscaling/v2` API version, you can configure a HorizontalPodAutoscaler
to scale based on a custom metric (that is not built in to Kubernetes or any Kubernetes component).
The HorizontalPodAutoscaler controller then queries for these custom metrics from the Kubernetes
API.

See [Support for metrics APIs](https://kubernetes.io/docs/concepts/workloads/autoscaling/horizontal-pod-autoscale/#support-for-metrics-apis) for the requirements.