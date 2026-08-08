---
id: kubernetes-device-plugin-and-unhealthy-devices-3614a558
type: concept
title: Device plugin and unhealthy devices
description: There are cases when devices fail or are shut down. The responsibility
  of the Device Plugin
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/extend-kubernetes/compute-storage-net/device-plugins/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Device plugin and unhealthy devices

There are cases when devices fail or are shut down. The responsibility of the Device Plugin
in this case is to notify the kubelet about the situation using the `ListAndWatchResponse` API.

Once a device is marked as unhealthy, the kubelet will decrease the allocatable count
for this resource on the Node to reflect how many devices can be used for scheduling new pods.
Capacity count for the resource will not change.

Pods that were assigned to the failed devices will continue be assigned to this device.
It is typical that code relying on the device will start failing and Pod may get
into Failed phase if `restartPolicy` for the Pod was not `Always` or enter the crash loop
otherwise.

Before Kubernetes v1.31, the way to know whether or not a Pod is associated with the
failed device is to use the [PodResources API](https://kubernetes.io/docs/concepts/extend-kubernetes/compute-storage-net/device-plugins/#monitoring-device-plugin-resources).

FEATURE STATE:
`Kubernetes v1.36 [beta]`(enabled by default)

When the feature gate `ResourceHealthStatus` is enabled (beta and enabled by default since v1.36),
the field `allocatedResourcesStatus`
is added to each container status, within the `.status` for each Pod. The `allocatedResourcesStatus`
field reports health information for each device assigned to the container.
Each resource health entry can include an optional `message` field with additional
human readable context about the health status, such as error details or failure reasons.

For a failed Pod, or where you suspect a fault, you can use this status to understand whether
the Pod behavior may be associated with device failure. For example, if an accelerator is reporting
an over-temperature event, the `allocatedResourcesStatus` field may report this.