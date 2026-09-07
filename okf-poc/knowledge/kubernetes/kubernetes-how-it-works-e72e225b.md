---
id: kubernetes-how-it-works-e72e225b
type: concept
title: How it works
description: A driver defines a `compatibilityGroups` list for each
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/resource-management/dynamic-resource-allocation/dra-features/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

### How it works

A driver defines a `compatibilityGroups` list for each
`device.consumesCounters[]` entry in a ResourceSlice. The list contains
at most 2 opaque string names that represent the operating mode or partition
type of that device on that particular counter set.

When the scheduler allocates multiple devices that draw from the same counter
set, it computes the intersection of their `compatibilityGroups`. Allocation
succeeds only if that intersection is non-empty — meaning every co-allocated
device shares at least one common group name. Devices drawing from different
counter sets are never compared against each other.

A device that declares no groups (an unset, nil, or empty list) is treated as
a special case: it is only co-allocatable with other no-group devices on the
same counter set. It is never co-allocatable with a device that declares one or
more groups.

The constraint applies across all claims being allocated in a single scheduling
cycle: if two claims each allocate a device from the same counter set, the
cross-claim group intersection is also enforced.