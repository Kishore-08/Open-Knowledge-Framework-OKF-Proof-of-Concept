---
id: kubernetes-example-disable-scale-down-cdcbb833
type: concept
title: 'Example: disable scale down'
description: The `selectPolicy` value of `Disabled` turns off scaling the given direction.
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/autoscaling/horizontal-pod-autoscale/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

### Example: disable scale down

The `selectPolicy` value of `Disabled` turns off scaling the given direction.
So to prevent downscaling the following policy would be used:

```
behavior:
  scaleDown:
    selectPolicy: Disabled
```