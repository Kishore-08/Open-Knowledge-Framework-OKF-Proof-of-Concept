---
id: kubernetes-device-compatibility-groups-e72e225b
type: concept
title: Device compatibility groups
description: 'FEATURE STATE:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/resource-management/dynamic-resource-allocation/dra-features/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

## Device compatibility groups

FEATURE STATE:
`Kubernetes v1.37 [alpha]`(disabled by default)

Device compatibility groups let a DRA driver declare which partitioned devices
can be co-allocated on the same physical hardware. Without this feature,
incompatible device combinations are only detected when the kubelet prepares
the Pod on a node — resulting in a failed preparation. With compatibility
groups, the scheduler rejects incompatible combinations at scheduling time,
before any node-side work begins.

This is most useful for hardware that supports mutually exclusive operating
modes. For example, a GPU that can run in either MIG mode or vGPU mode: a
device in MIG mode and a device in vGPU mode cannot be co-allocated because
they consume overlapping physical resources in incompatible ways. By declaring
`compatibilityGroups`, the driver makes this constraint visible to the
scheduler.

This feature builds on [partitionable devices](https://kubernetes.io/docs/concepts/resource-management/dynamic-resource-allocation/dra-features/#partitionable-devices): the
`compatibilityGroups` field lives on `device.consumesCounters[]` entries, which
only exist for partitionable devices. Both the `DRADeviceCompatibilityGroups`
and `DRAPartitionableDevices` feature gates must be enabled in the
`kube-apiserver` and `kube-scheduler`.