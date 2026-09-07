---
id: kubernetes-dra-device-metadata-in-containers-3d8c59ec
type: concept
title: DRA device metadata in containers
description: 'FEATURE STATE:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/resource-management/dynamic-resource-allocation/dra-observability/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

## DRA device metadata in containers

FEATURE STATE:
`Kubernetes v1.37 [beta]`

DRA drivers can expose device metadata such as device attributes (PCI bus
addresses or mediated device UUIDs) and network configuration directly to
containers as JSON files.
This lets applications discover information about allocated devices without
querying the Kubernetes API or using custom controllers.

KEP-5304 defines a
[device metadata protocol](https://kubernetes.io/docs/concepts/resource-management/dynamic-resource-allocation/dra-observability/#device-metadata-protocol) that drivers must follow
so that applications see a consistent layout across drivers and clusters. The
[DRA kubelet plugin library](https://pkg.go.dev/k8s.io/dynamic-resource-allocation/kubeletplugin)
implements this protocol.

Device metadata follows the same rules as device access: it is available inside
a container only when that container requests the device. For details, see
[Request devices in workloads using DRA](https://kubernetes.io/docs/tasks/configure-pod-container/assign-resources/allocate-devices-dra/#request-devices-workloads).