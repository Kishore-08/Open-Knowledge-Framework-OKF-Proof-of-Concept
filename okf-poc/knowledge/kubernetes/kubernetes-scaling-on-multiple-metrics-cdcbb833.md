---
id: kubernetes-scaling-on-multiple-metrics-cdcbb833
type: concept
title: Scaling on multiple metrics
description: 'FEATURE STATE:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/autoscaling/horizontal-pod-autoscale/
updated_at: '2026-08-13'
created_at: '2026-08-13'
---

## Scaling on multiple metrics

FEATURE STATE:
`Kubernetes v1.23 [stable]`

(the `autoscaling/v2beta2` API version previously provided this ability as a beta feature)

Provided that you use the `autoscaling/v2` API version, you can specify multiple metrics for a
HorizontalPodAutoscaler to scale on. Then, the HorizontalPodAutoscaler controller evaluates each metric,
and proposes a new scale based on that metric. The HorizontalPodAutoscaler takes the maximum scale
recommended for each metric and sets the workload to that size (provided that this isn't larger than the
overall maximum that you configured).