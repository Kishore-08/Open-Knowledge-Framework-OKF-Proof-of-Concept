---
id: kubernetes-partition-summary-3d8c59ec
type: concept
title: Partition summary
description: 'FEATURE STATE:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/resource-management/dynamic-resource-allocation/dra-observability/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

### Partition summary

FEATURE STATE:
`Kubernetes v1.37 [alpha]`(disabled by default)

A single physical device such as a GPU may be advertised as several partition
types (for example, a full GPU versus a half-sized MIG slice) that draw from the
same shared counters. Because these partitions compete for the same underlying
capacity, a plain device count does not tell you how many of each type can still
be allocated. For [partitionable](https://kubernetes.io/docs/concepts/resource-management/dynamic-resource-allocation/dra-features/#partitionable-devices)
pools, the `partitionSummary` view answers that question. For each partition type
it reports:

- `attribute`: the fully qualified name of the device attribute whose value
  groups this entry. It is the ResourceSlice's `spec.partitionTypeAttribute`, or
  the request's `spec.defaultPartitionTypeAttribute` when the slice declares none.
- `type`: the value of that attribute on the device (for example, `Full` or
  `Half`).
- `total`: the number of devices of this partition type in the pool.
- `allocatable`: how many *additional* devices of this partition type could still
  be allocated given current shared-counter consumption.

The named attribute must be a string attribute. If a partitionable device's
partition-type attribute is missing or is not a string (for example, an integer,
boolean, or version value), the pool reports a validation error instead of a
partition summary. There is no special handling for
[list-type attributes](https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/#DRAListTypeAttributes);
a non-string attribute is simply not a valid partition-type attribute.

To produce this view, the driver labels each partitionable device with a string
attribute whose value names the partition type, and names that attribute in the
ResourceSlice's `partitionTypeAttribute` field:

```
apiVersion: resource.k8s.io/v1
kind: ResourceSlice
# ...
spec:
  # Every partitionable device in this slice carries this attribute; devices
  # that share a value share the same shared-counter cost.
  partitionTypeAttribute: gpu.example.com/profile
```

If a driver has not yet been updated to declare `partitionTypeAttribute`, a
request can still obtain a partition summary by naming a fallback attribute in
its spec. A slice's own `partitionTypeAttribute` always takes precedence; the
request-level default applies only to devices whose slice does not declare one:

```
apiVersion: resource.k8s.io/v1alpha3
kind: ResourcePoolStatusRequest
metadata:
  name: check-gpu-partitions
spec:
  driver: gpu.example.com
  # Fallback grouping attribute for slices that don't declare one themselves.
  defaultPartitionTypeAttribute: gpu.example.com/profile
```

When neither the slice nor the request names an attribute, a partitionable pool
reports no `partitionSummary`.

The `partitionSummary` view is controlled by the
[`DRAPartitionableDevicesType` feature gate](https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/#DRAPartitionableDevicesType)
in the `kube-apiserver` and `kube-controller-manager`, which in turn requires the
[`DRAResourcePoolStatus`](https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/#DRAResourcePoolStatus)
and
[`DRAPartitionableDevices`](https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/#DRAPartitionableDevices)
feature gates to be enabled.