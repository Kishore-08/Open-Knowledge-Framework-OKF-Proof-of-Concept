---
id: kubernetes-list-type-attributes-c976d546
type: concept
title: List type attributes
description: 'FEATURE STATE:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/resource-management/dynamic-resource-allocation/dra-api/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

## List type attributes

FEATURE STATE:
`Kubernetes v1.36 [alpha]`(disabled by default)

This feature improves the ResourceSlice API, allowing DRA drivers to specify list values for device attributes instead of only scalars.
This is useful for modeling more complex internal node topologies, for example when a CPU has adjacency to multiple PCIe roots.

For ResourceClaim authors (end users), this means that the `matchAttribute` and `distinctAttribute` work better for these cases.

- `matchAttribute` — the two attributes must have a *non-empty list intersection*, rather than be identical (scalar values are treated as single-item lists).
  This just means that if one driver publishes a single value for, say, the PCIe root, and another driver publishes a list, the constraint is met as long as
  the single value appears somewhere in the list.
- `distinctAttribute` — the attribute values must be *pairwise-disjoint* (no value shared between any two devices)

To help ResourceClaim authors use attributes that may be lists inside CEL expressions, this feature also introduces an `includes()` CEL function.

```
# Scalar attribute (backward compatible)
# assume: device.attributes["dra.example.com"].model = "model-a"
device.attributes["dra.example.com"].model.includes("model-a")  # true
device.attributes["dra.example.com"].model.includes("model-b")  # false

# List-type attribute (requires DRAListTypeAttributes)
# assume: device.attributes["dra.example.com"].supported-models= ["model-a", "model-b"]
device.attributes["dra.example.com"].supported-models.includes("model-a")  # true
device.attributes["dra.example.com"].supported-models.includes("model-c")  # false
```