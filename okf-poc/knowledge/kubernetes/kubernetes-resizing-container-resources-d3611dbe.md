---
id: kubernetes-resizing-container-resources-d3611dbe
type: concept
title: Resizing container resources
description: After creating a Pod, you may need to adjust its CPU or memory resources
  based on
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

### Resizing container resources

After creating a Pod, you may need to adjust its CPU or memory resources based on
actual usage patterns. Kubernetes provides two approaches for resizing Pod resources:

#### In-place resize

FEATURE STATE:
`Kubernetes v1.35 [stable]`(enabled by default)

You can modify the CPU and memory `requests` and `limits` of containers
in a running Pod without recreating it. This is called *in-place Pod vertical scaling*
or *in-place Pod resize*. To perform an in-place resize, update the container's resource
specifications using the Pod's `/resize` subresource. You can control whether a container
restart is required by setting the `resizePolicy` field in the container specification.

#### Note:

In-place resize currently applies to container-level resources. For resizing Pod-level
resources, see [Resize Pod CPU and Memory Resources](https://kubernetes.io/docs/tasks/configure-pod-container/resize-pod-resources/).

#### Note:

FEATURE STATE:
`Kubernetes v1.37 [alpha]`(disabled by default)

When the `InPlacePodVerticalScalingSchedulerPreemption` feature gate is enabled,
deferred in-place resize requests can trigger `kube-scheduler` to preempt
lower-priority Pods on the assigned node to make room for the resize.
For more details, see
[Preemption for in-place Pod resize](https://kubernetes.io/docs/concepts/scheduling-eviction/pod-priority-preemption/#preemption-for-in-place-pod-resize).

#### Resizing by launching replacement Pods

The cloud native approach to changing a Pod's resources is to update the Pod template
in the workload object (such as a Deployment or StatefulSet) and let the workload's
controller replace Pods with new ones that have the updated resources. This approach
works with any Kubernetes version and can change any Pod specification.

For more details about Pod resizing, see [Resizing Pods](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#pod-resize).
For detailed instructions on in-place resize, see
[Resize CPU and Memory Resources assigned to Containers](https://kubernetes.io/docs/tasks/configure-pod-container/resize-container-resources/).
You can also use the [Vertical Pod Autoscaler](https://kubernetes.io/docs/concepts/workloads/autoscaling/vertical-pod-autoscale/)
to automatically manage Pod resource recommendations.