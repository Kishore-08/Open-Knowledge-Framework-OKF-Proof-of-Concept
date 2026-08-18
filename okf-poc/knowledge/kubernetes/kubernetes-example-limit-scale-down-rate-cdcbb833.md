---
id: kubernetes-example-limit-scale-down-rate-cdcbb833
type: concept
title: 'Example: limit scale down rate'
description: To limit the rate at which pods are removed by the HPA to 10% per minute,
  the
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/autoscaling/horizontal-pod-autoscale/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

### Example: limit scale down rate

To limit the rate at which pods are removed by the HPA to 10% per minute, the
following behavior would be added to the HPA:

```
behavior:
  scaleDown:
    policies:
    - type: Percent
      value: 10
      periodSeconds: 60
```

To ensure that no more than 5 Pods are removed per minute, you can add a second scale-down
policy with a fixed size of 5, and set `selectPolicy` to minimum. Setting `selectPolicy` to `Min` means
that the autoscaler chooses the policy that affects the smallest number of Pods:

```
behavior:
  scaleDown:
    policies:
    - type: Percent
      value: 10
      periodSeconds: 60
    - type: Pods
      value: 5
      periodSeconds: 60
    selectPolicy: Min
```