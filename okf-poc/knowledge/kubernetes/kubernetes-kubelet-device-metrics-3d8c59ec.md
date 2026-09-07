---
id: kubernetes-kubelet-device-metrics-3d8c59ec
type: concept
title: kubelet device metrics
description: The `PodResourcesLister` kubelet gRPC service lets you monitor in-use
  devices.
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/resource-management/dynamic-resource-allocation/dra-observability/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

### kubelet device metrics

The `PodResourcesLister` kubelet gRPC service lets you monitor in-use devices.
The `DynamicResource` message provides information that's specific to dynamic
resource allocation, such as the device name and the claim name. For details,
see
[Monitoring device plugin resources](https://kubernetes.io/docs/concepts/extend-kubernetes/compute-storage-net/device-plugins/#monitoring-device-plugin-resources).