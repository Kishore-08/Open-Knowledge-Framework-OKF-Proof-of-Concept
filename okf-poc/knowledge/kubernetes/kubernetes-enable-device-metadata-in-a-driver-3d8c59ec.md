---
id: kubernetes-enable-device-metadata-in-a-driver-3d8c59ec
type: concept
title: Enable device metadata in a driver
description: Device metadata is a driver-side feature. It has no Kubernetes feature
  gate and
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/resource-management/dynamic-resource-allocation/dra-observability/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

### Enable device metadata in a driver

Device metadata is a driver-side feature. It has no Kubernetes feature gate and
is disabled by default in the DRA kubelet plugin library. A driver must enable
the feature and explicitly select the versions that it writes:

```
kubeletplugin.EnableDeviceMetadata(true, []schema.GroupVersion{
	metadatav1beta1.SchemeGroupVersion,
	metadatav1alpha1.SchemeGroupVersion,
})
```

The `v1beta1` version is required. A driver can also write `v1alpha1` for
compatibility with older consumers. The order in the slice is the order in the
metadata stream; the framework does not sort the versions. Drivers should put
the newest version first. Enabling device metadata with no versions, without
`v1beta1`, or with an unknown version causes the plugin to fail during startup.

For each prepared device, the driver can populate
[`Device.Metadata`](https://pkg.go.dev/k8s.io/dynamic-resource-allocation/kubeletplugin#Device)
with
[`kubeletplugin.DeviceMetadata`](https://pkg.go.dev/k8s.io/dynamic-resource-allocation/kubeletplugin#DeviceMetadata).
Drivers should include the attributes that they publish for that device in its
ResourceSlice, so workloads see the same information at runtime. Drivers can
also include attributes that are only relevant at runtime. For network devices,
drivers can add interface names, IP addresses, and hardware addresses after CNI
configuration by calling
[`UpdateRequestMetadata`](https://pkg.go.dev/k8s.io/dynamic-resource-allocation/kubeletplugin#Helper.UpdateRequestMetadata).

The kubelet plugin API links above describe integration for driver authors.
The DRA framework does not define a universal command-line flag, so cluster
operators enable the feature through the deployment configuration provided by
their driver.

When enabled, the DRA kubelet plugin library writes metadata files while
preparing allocated devices. It also writes CDI specifications to `/var/run/cdi`
by default. The container runtime must be configured to discover CDI
specifications from that directory. The library determines the minimum CDI
specification version required for each generated specification.

When one request allocates devices from multiple DRA drivers, each driver writes
its own metadata file. Consumers that know the driver name should construct the
exact path from the claim, request, and driver names. Go consumers can use
[`ReadResourceClaimMetadata`](https://pkg.go.dev/k8s.io/dynamic-resource-allocation/devicemetadata#ReadResourceClaimMetadata)
or
[`ReadResourceClaimTemplateMetadata`](https://pkg.go.dev/k8s.io/dynamic-resource-allocation/devicemetadata#ReadResourceClaimTemplateMetadata)
to read and merge all per-driver files for a request.