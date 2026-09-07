---
id: kubernetes-custom-drivers-3d8c59ec
type: concept
title: Custom drivers
description: Custom drivers that do not use the DRA kubelet plugin library must implement
  the
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/resource-management/dynamic-resource-allocation/dra-observability/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

### Custom drivers

Custom drivers that do not use the DRA kubelet plugin library must implement the
[device metadata protocol](https://kubernetes.io/docs/concepts/resource-management/dynamic-resource-allocation/dra-observability/#device-metadata-protocol) themselves. This includes
writing the versioned `DeviceMetadata` stream at the correct paths, incrementing
`metadata.generation` on every update, and exposing files read-only through CDI
or an equivalent mechanism.