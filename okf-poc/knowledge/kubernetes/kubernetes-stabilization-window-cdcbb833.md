---
id: kubernetes-stabilization-window-cdcbb833
type: concept
title: Stabilization window
description: The stabilization window is used to restrict the [flapping](https://kubernetes.io/docs/concepts/workloads/autoscaling/horizontal-pod-autoscale/#flapping)
  of
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/autoscaling/horizontal-pod-autoscale/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

### Stabilization window

The stabilization window is used to restrict the [flapping](https://kubernetes.io/docs/concepts/workloads/autoscaling/horizontal-pod-autoscale/#flapping) of
replica count when the metrics used for scaling keep fluctuating. The autoscaling algorithm
uses this window to infer a previous desired state and avoid unwanted changes to workload
scale.

For example, in the following example snippet, a stabilization window is specified for `scaleDown`.

```
behavior:
  scaleDown:
    stabilizationWindowSeconds: 300
```

When the metrics indicate that the target should be scaled down the algorithm looks
into previously computed desired states, and uses the highest value from the specified
interval. In the above example, all desired states from the past 5 minutes will be considered.

This approximates a rolling maximum, and avoids having the scaling algorithm frequently
remove Pods only to trigger recreating an equivalent Pod just moments later.