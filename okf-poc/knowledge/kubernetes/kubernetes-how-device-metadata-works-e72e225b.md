---
id: kubernetes-how-device-metadata-works-e72e225b
type: concept
title: How device metadata works
description: Device metadata is a driver-side feature that does not require any Kubernetes
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/resource-management/dynamic-resource-allocation/dra-features/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

### How device metadata works

Device metadata is a driver-side feature that does not require any Kubernetes
API changes or feature gates. Using the DRA kubelet plugin library is a common
way to implement a driver, but drivers can be built in other ways as well.
Drivers that use the kubelet plugin enable this feature by passing the
`EnableDeviceMetadata` and `MetadataVersions`
[options](https://pkg.go.dev/k8s.io/dynamic-resource-allocation/kubeletplugin#Option)
when starting the plugin. `MetadataVersions` specifies which API versions are
serialized into the metadata file and must be set explicitly by the driver.
Check the documentation of your DRA driver to learn whether device metadata is
supported and how to enable it.

When device metadata is enabled, the driver generates metadata files and CDI
bind-mount specifications while preparing the allocated devices for the pod,
before the consuming containers start. The metadata appears inside containers at
the well-known paths as [defined above](https://kubernetes.io/docs/concepts/resource-management/dynamic-resource-allocation/dra-features/#device-metadata-protocol).

When a single request allocates devices from multiple DRA drivers, each driver
writes its own metadata file. Containers enumerate `*-metadata.json` files in
the request directory to discover all devices.

The Go package
[`k8s.io/dynamic-resource-allocation/devicemetadata`](https://pkg.go.dev/k8s.io/dynamic-resource-allocation/devicemetadata)
provides utilities for reading and decoding these metadata files by applications
inside the container.