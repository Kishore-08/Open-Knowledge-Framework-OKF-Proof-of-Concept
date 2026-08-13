---
id: kubernetes-tolerance-cdcbb833
type: concept
title: Tolerance
description: 'FEATURE STATE:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/autoscaling/horizontal-pod-autoscale/
updated_at: '2026-08-13'
created_at: '2026-08-13'
---

### Tolerance

FEATURE STATE:
`Kubernetes v1.35 [beta]`(enabled by default)

The `tolerance` field configures a threshold for metric variations, preventing the
autoscaler from scaling for changes below that value.

This tolerance is defined as the amount of variation around the desired metric value under
which no scaling will occur. For example, consider a HorizontalPodAutoscaler configured
with a target memory consumption of 100MiB and a scale-up tolerance of 5%:

```
behavior:
  scaleUp:
    tolerance: 0.05 # 5% tolerance for scale up
```

With this configuration, the HPA algorithm will only consider scaling up if the memory
consumption is higher than 105MiB (that is: 5% above the target).

If you don't set this field, the HPA applies the default cluster-wide tolerance of 10%. This
default can be updated for both scale-up and scale-down using the
[kube-controller-manager](https://kubernetes.io/docs/reference/command-line-tools-reference/kube-controller-manager/)
`--horizontal-pod-autoscaler-tolerance` command line argument. (You can't use the Kubernetes API
to configure this default value.)