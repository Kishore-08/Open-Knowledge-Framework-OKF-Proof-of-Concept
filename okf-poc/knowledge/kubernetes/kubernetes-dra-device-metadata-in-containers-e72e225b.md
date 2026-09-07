---
id: kubernetes-dra-device-metadata-in-containers-e72e225b
type: concept
title: DRA device metadata in containers
description: 'FEATURE STATE:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/resource-management/dynamic-resource-allocation/dra-features/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

## DRA device metadata in containers

FEATURE STATE:
`Kubernetes v1.36 [alpha]`

DRA drivers can expose device metadata such as device attributes (PCI bus
addresses or mdevUUID for mediated devices) or network configuration directly
to containers as JSON files.
This lets applications inside the container discover information about allocated
devices without querying the Kubernetes API or building custom controllers.

KEP-5304 defines a
[device metadata protocol](https://kubernetes.io/docs/concepts/resource-management/dynamic-resource-allocation/dra-features/#device-metadata-protocol) that drivers must
follow so applications inside the container see a consistent layout across
drivers and clusters. The
[DRA kubelet plugin library](https://pkg.go.dev/k8s.io/dynamic-resource-allocation/kubeletplugin)
implements this protocol for you; the rest of this section describes how to
use it.

Device metadata follows the same rules as device access: it is available inside
a container only when that container requests the device in its container
specification, and not otherwise. For how to request DRA devices in Pods and
containers, see
[Request devices in workloads using DRA](https://kubernetes.io/docs/tasks/configure-pod-container/assign-resources/allocate-devices-dra/#request-devices-workloads).