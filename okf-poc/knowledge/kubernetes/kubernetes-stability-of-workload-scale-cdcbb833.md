---
id: kubernetes-stability-of-workload-scale-cdcbb833
type: concept
title: Stability of workload scale
description: When managing the scale of a group of replicas using the HorizontalPodAutoscaler,
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/autoscaling/horizontal-pod-autoscale/
updated_at: '2026-08-13'
created_at: '2026-08-13'
---

## Stability of workload scale

When managing the scale of a group of replicas using the HorizontalPodAutoscaler,
it is possible that the number of replicas keeps fluctuating frequently due to the
dynamic nature of the metrics evaluated. This is sometimes referred to as *thrashing*,
or *flapping*. It's similar to the concept of *hysteresis* in cybernetics.