---
id: kubernetes-dynamic-resource-allocation-3d957e27
type: concept
title: Dynamic Resource Allocation
description: 'FEATURE STATE:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/resource-management/dynamic-resource-allocation/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

# Dynamic Resource Allocation

FEATURE STATE:
`Kubernetes v1.35 [stable]`(enabled by default)

This section introduces *dynamic resource allocation (DRA)* in Kubernetes.

DRA is a Kubernetes feature that lets you request and share resources among Pods.
These resources are often attached
[devices](https://kubernetes.io/docs/reference/glossary/?all=true#term-device "Any resource that's directly or indirectly attached your cluster's nodes, like GPUs or circuit boards.") like hardware
accelerators.

With DRA, device drivers and cluster admins define device *classes* that are
available to *claim* in workloads. Kubernetes allocates matching devices to
specific claims and places the corresponding Pods on nodes that can access the
allocated devices.

Allocating resources with DRA offers a similar experience to
[dynamic volume provisioning](https://kubernetes.io/docs/concepts/storage/dynamic-provisioning/),
in which you use PersistentVolumeClaims to *claim* storage capacity from storage classes,
and request the claimed capacity for use in your Pods.