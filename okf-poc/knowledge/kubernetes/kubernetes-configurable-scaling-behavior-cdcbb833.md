---
id: kubernetes-configurable-scaling-behavior-cdcbb833
type: concept
title: Configurable scaling behavior
description: 'FEATURE STATE:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/autoscaling/horizontal-pod-autoscale/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

## Configurable scaling behavior

FEATURE STATE:
`Kubernetes v1.23 [stable]`

(the `autoscaling/v2beta2` API version previously provided this ability as a beta feature)

If you use the `v2` HorizontalPodAutoscaler API, you can use the `behavior` field
(see the [API reference](https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/horizontal-pod-autoscaler-v2/#HorizontalPodAutoscalerSpec))
to configure separate scale-up and scale-down behaviors.
You specify these behaviors by setting `scaleUp` and / or `scaleDown`
under the `behavior` field.

Scaling policies let you control the rate of change of replicas while scaling.
Also two settings can be used to prevent [flapping](https://kubernetes.io/docs/concepts/workloads/autoscaling/horizontal-pod-autoscale/#flapping): you can specify a
*stabilization window* for smoothing replica counts, and a tolerance to ignore
minor metric fluctuations below a specified threshold.