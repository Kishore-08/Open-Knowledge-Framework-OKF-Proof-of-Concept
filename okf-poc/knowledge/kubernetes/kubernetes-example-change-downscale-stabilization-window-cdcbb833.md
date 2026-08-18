---
id: kubernetes-example-change-downscale-stabilization-window-cdcbb833
type: concept
title: 'Example: change downscale stabilization window'
description: To provide a custom downscale stabilization window of 1 minute, the following
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/autoscaling/horizontal-pod-autoscale/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

### Example: change downscale stabilization window

To provide a custom downscale stabilization window of 1 minute, the following
behavior would be added to the HPA:

```
behavior:
  scaleDown:
    stabilizationWindowSeconds: 60
```