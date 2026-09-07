---
id: kubernetes-node-allocatable-resources-d98ef934
type: concept
title: Node allocatable resources
description: 'FEATURE STATE:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/resource-management/dynamic-resource-allocation/how-dra-works/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

## Node allocatable resources

FEATURE STATE:
`Kubernetes v1.36 [alpha]`(disabled by default)

Devices managed by DRA can have an underlying footprint composed of node allocatable
resources, such as `cpu`, `memory`, or `hugepages`.
This feature integrates these DRA-based requests into the scheduler's standard
accounting alongside regular Pod `spec` requests for these resources.

DRA drivers define how devices consume node allocatable resources using two distinct models:

- **Direct Resource Mapping (`mapping`)**: The DRA device directly provides a standard node resource (such as a custom CPU core pool or memory block). The claim allocation directly maps to standard CPU or memory capacity on the node.
- **Auxiliary Device Overhead (`overhead`)**: The DRA device (such as a GPU or accelerator) requires host resources (such as host RAM) as secondary overhead to operate when allocated to a Pod or container.