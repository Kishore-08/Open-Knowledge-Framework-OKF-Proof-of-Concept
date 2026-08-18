---
id: kubernetes-default-behavior-cdcbb833
type: concept
title: Default behavior
description: To use the custom scaling not all fields have to be specified. Only values
  which need to be
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/autoscaling/horizontal-pod-autoscale/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

### Default behavior

To use the custom scaling not all fields have to be specified. Only values which need to be
customized can be specified. These custom values are merged with default values. The default values
match the existing behavior in the HPA algorithm.

```
behavior:
  scaleDown:
    stabilizationWindowSeconds: 300
    policies:
    - type: Percent
      value: 100
      periodSeconds: 15
  scaleUp:
    stabilizationWindowSeconds: 0
    policies:
    - type: Percent
      value: 100
      periodSeconds: 15
    - type: Pods
      value: 4
      periodSeconds: 15
    selectPolicy: Max
```

For scaling down the stabilization window is *300* seconds (or the value of the
`--horizontal-pod-autoscaler-downscale-stabilization` command line option, if provided). There is only a single policy
for scaling down which allows a 100% of the currently running replicas to be removed which
means the scaling target can be scaled down to the minimum allowed replicas.
For scaling up there is no stabilization window. When the metrics indicate that the target should be
scaled up the target is scaled up immediately. There are 2 policies where 4 pods or a 100% of the currently
running replicas may at most be added every 15 seconds till the HPA reaches its steady state.