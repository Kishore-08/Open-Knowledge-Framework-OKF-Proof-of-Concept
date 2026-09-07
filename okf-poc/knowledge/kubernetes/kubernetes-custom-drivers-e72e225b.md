---
id: kubernetes-custom-drivers-e72e225b
type: concept
title: Custom drivers
description: Custom, hand-crafted drivers that do not use the DRA kubelet plugin library
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/resource-management/dynamic-resource-allocation/dra-features/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

### Custom drivers

Custom, hand-crafted drivers that do not use the DRA kubelet plugin library
must implement the [device metadata protocol](https://kubernetes.io/docs/concepts/resource-management/dynamic-resource-allocation/dra-features/#device-metadata-protocol)
themselves. That means writing `DeviceMetadata` JSON at the correct file paths,
incrementing `metadata.generation` on every update, and exposing the files
read-only inside the container through CDI or an equivalent mechanism.