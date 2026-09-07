---
id: kubernetes-version-skew-safety-e72e225b
type: concept
title: Version-skew safety
description: When the `DRADeviceCompatibilityGroups` feature gate is disabled (the
  default
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/resource-management/dynamic-resource-allocation/dra-features/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

### Version-skew safety

When the `DRADeviceCompatibilityGroups` feature gate is disabled (the default
for alpha), the kube-apiserver strips the `compatibilityGroups` field from any
new or updated ResourceSlice — unless the old object already had the field
set. The scheduler then treats devices in any pool that previously had grouped
devices as belonging to an incomplete pool and skips them entirely.

Only a non-empty list counts as the field being set: `compatibilityGroups: null`
and `compatibilityGroups: []` are treated identically to omitting the field.
Devices with them behave exactly like devices with no groups — they do not
cause the scheduler to treat the pool as incomplete.

Device compatibility groups is controlled by the
[`DRADeviceCompatibilityGroups` feature gate](https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/#DRADeviceCompatibilityGroups)
in the kube-apiserver and kube-scheduler. The
[`DRAPartitionableDevices` feature gate](https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/#DRAPartitionableDevices)
must also be enabled.