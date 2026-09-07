---
id: kubernetes-pod-level-resource-managers-0cecd4eb
type: concept
title: Pod-level resource managers
description: 'FEATURE STATE:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/resource-management/pod-level-resource-managers/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

# Pod-level resource managers

FEATURE STATE:
`Kubernetes v1.37 [beta]`(disabled by default)

Pod-level resource support for the existing resource managers (Topology, CPU,
and Memory) extends them to handle pod-level resource specifications. When
enabled (via the `PodLevelResources` and `PodLevelResourceManagers` feature
gates), the resource managers can use `.spec.resources` directly as the basis
for their allocation decisions, evolving from a strictly per-container
allocation model to a
[Pod](https://kubernetes.io/docs/concepts/workloads/pods/ "A Pod represents a set of running containers in your cluster.")-centric one. This partitioning scheme
introduces a more flexible and powerful resource management model, particularly
for performance-sensitive workloads. It allows you to define hybrid allocation
models where some containers in a Pod receive exclusive, NUMA-aligned resources,
while others share the remaining resources from a pod-level shared pool.

To practice setting up `kubelet` resource managers with pod-level resources and
observe allocation behaviors hands-on, follow the
[Use pod-level resources with `kubelet` resource managers](https://kubernetes.io/docs/tutorials/cluster-management/use-pod-level-resource-managers/)
tutorial.

To understand pod-level resource managers, it is helpful to contrast them with
the traditional container-focused model. Previously, `kubelet` resource
allocations were strictly all or nothing: to receive exclusive NUMA-aligned
resources for your workload, every container in the Pod had to be Guaranteed
(specifying requests equal to limits for both CPU and memory).

Pod-level resource managers use `.spec.resources` to enable flexible
partitioning based on the configured Topology Manager scope:

- **`pod` scope:** The `kubelet` allocates and NUMA-aligns a single Pod
  bubble for the entire Pod based on `.spec.resources`. Containers requesting
  exclusive allocations carve out dedicated slices from within this Pod
  bubble, while all other containers share the remaining bubble capacity in a
  pod-isolated shared pool.
- **`container` scope:** Enables a hybrid allocation model. The `kubelet`
  allows individual containers to receive exclusive, NUMA-aligned resources
  directly from the Node's allocatable pool, while using the Pod's
  `.spec.resources` ceiling to cap collective consumption—allowing sidecars
  to run in the general Node shared pool without requiring every container
  in the Pod to be Guaranteed.

Both standard init containers and restartable init containers (sidecars) are
fully supported. They can receive exclusive resource slices or use the Pod's
shared pool, and the pod-level resource managers respect their lifecycle rules
(for example, reusable resources for standard init containers vs. persistent
reservations for sidecars).