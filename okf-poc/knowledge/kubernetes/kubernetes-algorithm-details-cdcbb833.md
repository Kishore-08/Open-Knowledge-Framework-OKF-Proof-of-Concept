---
id: kubernetes-algorithm-details-cdcbb833
type: concept
title: Algorithm details
description: From the most basic perspective, the HorizontalPodAutoscaler controller
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/autoscaling/horizontal-pod-autoscale/
updated_at: '2026-08-13'
created_at: '2026-08-13'
---

### Algorithm details

From the most basic perspective, the HorizontalPodAutoscaler controller
operates on the ratio between desired metric value and current metric
value:

$$\begin{equation\*}
desiredReplicas = ceil\left\lceil currentReplicas \times \frac{currentMetricValue}{desiredMetricValue} \right\rceil
\end{equation\*}$$

For example, if the current metric value is `200m`, and the desired value
is `100m`, the number of replicas will be doubled, since
\( { 200.0 \div 100.0 } = 2.0 \).  
If the current value is instead `50m`, you'll halve the number of
replicas, since \( { 50.0 \div 100.0 } = 0.5 \). The control plane skips any scaling
action if the ratio is sufficiently close to 1.0 (within a
[configurable tolerance](https://kubernetes.io/docs/concepts/workloads/autoscaling/horizontal-pod-autoscale/#tolerance), 0.1 by default).

When a `targetAverageValue` or `targetAverageUtilization` is specified,
the `currentMetricValue` is computed by taking the average of the given
metric across all Pods in the HorizontalPodAutoscaler's scale target.

Before checking the tolerance and deciding on the final values, the control
plane also considers whether any metrics are missing, and how many Pods
are [`Ready`](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#pod-conditions).
For per-pod resource metrics, all Pods with a deletion timestamp set
(objects with a deletion timestamp are in the process of being shut
down / removed) are ignored, and all failed Pods are discarded.
For external and object metrics, the replica count is based on the
number of Running and Ready Pods; terminating Pods that are still Ready
continue to count toward that total.

If a particular Pod is missing metrics, it is set aside for later; Pods
with missing metrics will be used to adjust the final scaling amount.

When scaling on CPU, if any pod has yet to become ready (it's still
initializing, or possibly is unhealthy) *or* the most recent metric point for
the pod was before it became ready, that pod is set aside as well.

Due to technical constraints, the HorizontalPodAutoscaler controller
cannot exactly determine the first time a pod becomes ready when
determining whether to set aside certain CPU metrics. Instead, it
considers a Pod "not yet ready" if it's unready and transitioned to
ready within a short, configurable window of time since it started.
This value is configured with the `--horizontal-pod-autoscaler-initial-readiness-delay`
command line option, and its default is 30 seconds.
Once a pod has become ready, it considers any transition to
ready to be the first if it occurred within a longer, configurable time
since it started. This value is configured with the
`--horizontal-pod-autoscaler-cpu-initialization-period` command line option,
and its default is 5 minutes.

The \( currentMetricValue \over desiredMetricValue \) base scale ratio is then
calculated, using the remaining pods not set aside or discarded from above.

If there were any missing metrics, the control plane recomputes the average more
conservatively, assuming those pods were consuming 100% of the desired
value in case of a scale down, and 0% in case of a scale up. This dampens
the magnitude of any potential scale.

Furthermore, if any not-yet-ready pods were present, and the workload would have
scaled up without factoring in missing metrics or not-yet-ready pods,
the controller conservatively assumes that the not-yet-ready pods are consuming 0%
of the desired metric, further dampening the magnitude of a scale up.

After factoring in the not-yet-ready pods and missing metrics, the
controller recalculates the usage ratio. If the new ratio reverses the scale
direction, or is within the tolerance, the controller doesn't take any scaling
action. In other cases, the new ratio is used to decide any change to the
number of Pods.

Note that the *original* value for the average utilization is reported
back via the HorizontalPodAutoscaler status, without factoring in the
not-yet-re