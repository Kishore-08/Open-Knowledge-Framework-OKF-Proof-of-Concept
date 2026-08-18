---
id: kubernetes-support-for-resource-metrics-cdcbb833
type: concept
title: Support for resource metrics
description: Any HPA target can be scaled based on the resource usage of the pods
  in the scaling target.
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/autoscaling/horizontal-pod-autoscale/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

## Support for resource metrics

Any HPA target can be scaled based on the resource usage of the pods in the scaling target.
When defining the pod specification the resource requests like `cpu` and `memory` should
be specified. This is used to determine the resource utilization and used by the HPA controller
to scale the target up or down. To use resource utilization based scaling specify a metric source
like this:

```
type: Resource
resource:
  name: cpu
  target:
    type: Utilization
    averageUtilization: 60
```

With this metric the HPA controller will keep the average utilization of the pods in the scaling
target at 60%. Utilization is the ratio between the current usage of resource to the requested
resources of the pod. See [Algorithm](https://kubernetes.io/docs/concepts/workloads/autoscaling/horizontal-pod-autoscale/#algorithm-details) for more details about how the utilization
is calculated and averaged.

#### Note:

Since the resource usages of all the containers are summed up the total pod utilization may not
accurately represent the individual container resource usage. This could lead to situations where
a single container might be running with high usage and the HPA will not scale out because the overall
pod usage is still within acceptable limits.