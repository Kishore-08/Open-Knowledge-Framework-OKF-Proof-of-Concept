---
id: kubernetes-container-resource-metrics-cdcbb833
type: concept
title: Container resource metrics
description: 'FEATURE STATE:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/autoscaling/horizontal-pod-autoscale/
updated_at: '2026-08-13'
created_at: '2026-08-13'
---

### Container resource metrics

FEATURE STATE:
`Kubernetes v1.30 [stable]`(enabled by default)

The HorizontalPodAutoscaler API also supports a container metric source where the HPA can track the
resource usage of individual containers across a set of Pods, in order to scale the target resource.
This lets you configure scaling thresholds for the containers that matter most in a particular Pod.
For example, if you have a web application and a sidecar container that provides logging, you can scale based on the resource
use of the web application, ignoring the sidecar container and its resource use.

If you revise the target resource to have a new Pod specification with a different set of containers,
you should revise the HPA spec if that newly added container should also be used for
scaling. If the specified container in the metric source is not present or only present in a subset
of the pods then those pods are ignored and the recommendation is recalculated. See [Algorithm](https://kubernetes.io/docs/concepts/workloads/autoscaling/horizontal-pod-autoscale/#algorithm-details)
for more details about the calculation. To use container resources for autoscaling define a metric
source as follows:

```
type: ContainerResource
containerResource:
  name: cpu
  container: application
  target:
    type: Utilization
    averageUtilization: 60
```

In the above example the HPA controller scales the target such that the average utilization of the cpu
in the `application` container of all the pods is 60%.

#### Note:

If you change the name of a container that a HorizontalPodAutoscaler is tracking, you can
make that change in a specific order to ensure scaling remains available and effective
whilst the change is being applied. Before you update the resource that defines the container
(such as a Deployment), you should update the associated HPA to track both the new and
old container names. This way, the HPA is able to calculate a scaling recommendation
throughout the update process.

Once you have rolled out the container name change to the workload resource, tidy up by removing
the old container name from the HPA specification.