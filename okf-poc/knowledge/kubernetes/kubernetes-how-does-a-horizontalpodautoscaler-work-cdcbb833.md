---
id: kubernetes-how-does-a-horizontalpodautoscaler-work-cdcbb833
type: concept
title: How does a HorizontalPodAutoscaler work?
description: '```'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/autoscaling/horizontal-pod-autoscale/
updated_at: '2026-08-13'
created_at: '2026-08-13'
---

## How does a HorizontalPodAutoscaler work?

```
graph BT

hpa[HorizontalPodAutoscaler] --> scale[Scale]

subgraph rc[Deployment]
    scale
end

scale -.-> pod1[Pod 1]
scale -.-> pod2[Pod 2]
scale -.-> pod3[Pod N]

classDef hpa fill:#D5A6BD,stroke:#1E1E1D,stroke-width:1px,color:#1E1E1D;
classDef rc fill:#F9CB9C,stroke:#1E1E1D,stroke-width:1px,color:#1E1E1D;
classDef scale fill:#B6D7A8,stroke:#1E1E1D,stroke-width:1px,color:#1E1E1D;
classDef pod fill:#9FC5E8,stroke:#1E1E1D,stroke-width:1px,color:#1E1E1D;
class hpa hpa;
class rc rc;
class scale scale;
class pod1,pod2,pod3 pod
```

Figure 1. HorizontalPodAutoscaler controls the scale of a Deployment and its ReplicaSet

Kubernetes implements horizontal pod autoscaling as a control loop that runs intermittently
(it is not a continuous process). The interval is set by the
`--horizontal-pod-autoscaler-sync-period` parameter to the
[`kube-controller-manager`](https://kubernetes.io/docs/reference/command-line-tools-reference/kube-controller-manager/)
(and the default interval is 15 seconds).

Once during each period, the controller manager queries the resource utilization against the
metrics specified in each HorizontalPodAutoscaler definition. The controller manager
finds the target resource defined by the `scaleTargetRef`,
then selects the pods based on the target resource's `.spec.selector` labels,
and obtains the metrics from either the resource metrics API (for per-pod resource metrics),
or the custom metrics API (for all other metrics).

- For per-pod resource metrics (like CPU), the controller fetches the metrics
  from the resource metrics API for each Pod targeted by the HorizontalPodAutoscaler.
  Then, if a target utilization value is set, the controller calculates the utilization
  value as a percentage of the equivalent
  [resource request](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/#requests-and-limits)
  on the containers in each Pod. If a target raw value is set, the raw metric values are used directly.
  The controller then takes the mean of the utilization or the raw value (depending on the type
  of target specified) across all targeted Pods, and produces a ratio used to scale
  the number of desired replicas.

  Please note that if some of the Pod's containers do not have the relevant resource request set,
  CPU utilization for the Pod will not be defined and the autoscaler will
  not take any action for that metric. See the [algorithm details](https://kubernetes.io/docs/concepts/workloads/autoscaling/horizontal-pod-autoscale/#algorithm-details) section below
  for more information about how the autoscaling algorithm works.
- For per-pod custom metrics, the controller functions similarly to per-pod resource metrics,
  except that it works with raw values, not utilization values.
- For object metrics and external metrics, a single metric is fetched, which describes
  the object in question. This metric is compared to the target
  value, to produce a ratio as above. In the `autoscaling/v2` API
  version, this value can optionally be divided by the number of Pods before the
  comparison is made.

The common use for HorizontalPodAutoscaler is to configure it to fetch metrics from
[aggregated APIs](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/apiserver-aggregation/ "The aggregation layer lets you install additional Kubernetes-style APIs in your cluster.")
(`metrics.k8s.io`, `custom.metrics.k8s.io`, or `external.metrics.k8s.io`). The `metrics.k8s.io` API is
usually provided by an add-on named Metrics Server, which needs to be launched separately.
For more information about resource metrics, see
[Metrics Server](https://kubernetes.io/docs/tasks/debug/debug-cluster/resource-metrics-pipeline/#metrics-server).

[Support for metrics APIs](https://kubernetes.io/docs/concepts/workloads/autoscaling/horizontal-pod-autoscale/#support-for-metrics-apis) explains the stability guarantees and support status for these
different API