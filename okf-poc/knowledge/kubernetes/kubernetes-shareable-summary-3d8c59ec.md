---
id: kubernetes-shareable-summary-3d8c59ec
type: concept
title: Shareable summary
description: For pools that contain [shareable devices](https://kubernetes.io/docs/concepts/resource-management/dynamic-resource-allocation/dra-features/#consumable-capacity)
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/resource-management/dynamic-resource-allocation/dra-observability/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

### Shareable summary

For pools that contain [shareable devices](https://kubernetes.io/docs/concepts/resource-management/dynamic-resource-allocation/dra-features/#consumable-capacity)
(devices that set `allowMultipleAllocations` and can be consumed by multiple
claims), `shareableSummary` reports aggregate capacity usage across the pool:

- `fullyAvailableDevices`: shareable devices with no capacity consumed.
- `partiallyAvailableDevices`: shareable devices with some, but not all, capacity
  consumed.
- `capacity`: per capacity name, the aggregate `total`, `consumed`, and
  `available` (`total` minus `consumed`, never negative) amounts across the pool.

The `shareableSummary` is populated only when at least one device in the pool is
shareable. It is part of the [resource pool status](https://kubernetes.io/docs/concepts/resource-management/dynamic-resource-allocation/dra-observability/#resource-pool-status)
feature (the
[`DRAResourcePoolStatus`](https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/#DRAResourcePoolStatus)
feature gate) and does not require `DRAPartitionableDevicesType`; the shareable
devices it summarizes come from the
[consumable capacity](https://kubernetes.io/docs/concepts/resource-management/dynamic-resource-allocation/dra-features/#consumable-capacity)
feature.