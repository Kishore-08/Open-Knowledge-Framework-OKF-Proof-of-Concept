---
id: kubernetes-pod-level-resource-managers-2f1e5981
type: concept
title: Pod-level resource managers
description: 'FEATURE STATE:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/resource-managers/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

## Pod-level resource managers

FEATURE STATE:
`Kubernetes v1.36 [alpha]`(disabled by default)

Pod-level resource support for the existing resource managers (Topology, CPU,
and Memory) extends them to handle pod-level resource specifications. When
enabled (via the `PodLevelResources` and `PodLevelResourceManagers` feature
gates), the resource managers can use `.spec.resources` directly as the basis
for their allocation decisions, evolving from a strictly per-container
allocation model to a pod-centric one. This partitioning scheme introduces a
more flexible and powerful resource management model, particularly for
performance-sensitive workloads. It allows you to define hybrid allocation
models where some containers in a Pod receive exclusive, NUMA-aligned resources,
while others share the remaining resources from a pod-level shared pool.

It is important to differentiate between the capabilities offered by each
Topology Manager scope, and how this modifies the behavior of the resource
managers. The `pod` scope enables allocation based on the entire pod's budget,
creating a pod-level shared pool for non-Guaranteed containers, alongside
exclusive allocations. In contrast, the `container` scope allows for a hybrid
allocation model where individual containers can get exclusive, NUMA-aligned
resources while others run in the node's shared pool, without aligning the
entire pod as a single unit.

Both standard init containers and restartable init containers (sidecars) are
fully supported. They can be granted exclusive resource slices or utilize the
pod's shared pool, and their lifecycle rules (e.g., reusable resources for
standard init containers vs. persistent reservations for sidecars) are respected
by the pod-level resource managers.