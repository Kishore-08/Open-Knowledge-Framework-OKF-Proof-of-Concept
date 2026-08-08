---
id: kubernetes-in-place-pod-resize-3e34f258
type: concept
title: In-place Pod resize
description: You can resize a Pod's container-level CPU and memory resources without
  recreating the Pod.
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### In-place Pod resize

You can resize a Pod's container-level CPU and memory resources without recreating the Pod.
This is also called *in-place Pod vertical scaling*. This allows you to adjust resource
allocation for running containers while potentially avoiding application disruption.

If you have specified resources at the pod-level, you can also resize those in-place.
For more details, see [Resize CPU and Memory Resources assigned to Pods](https://kubernetes.io/docs/tasks/configure-pod-container/resize-pod-resources/).

To perform an in-place resize, you update the Pod's desired state using the `/resize`
subresource. The kubelet then attempts to apply the new resource values to the running
containers. The Pod [conditions](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#pod-conditions "A condition represents the current state of a Kubernetes resource, providing information about whether certain aspects of the resource are true.")
`PodResizePending` and `PodResizeInProgress` (described in [Pod conditions](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#pod-conditions))
indicate the status of the resize operation. For more details about resize status, see
[Container Resize Status](https://kubernetes.io/docs/tasks/configure-pod-container/resize-container-resources/#container-resize-status).

Key considerations for in-place resize:

- Only CPU and memory resources can be resized in-place.
- The Pod's [Quality of Service (QoS) class](https://kubernetes.io/docs/concepts/workloads/pods/pod-qos/)
  is determined at creation and cannot be changed by resizing.
- You can configure whether a container restart is required for the resize using
  `resizePolicy` in the container specification.

For detailed instructions on performing in-place resize, see
[Resize CPU and Memory Resources assigned to Containers](https://kubernetes.io/docs/tasks/configure-pod-container/resize-container-resources/).