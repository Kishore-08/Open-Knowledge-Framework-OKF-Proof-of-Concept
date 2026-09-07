---
id: kubernetes-multi-level-topology-aware-scheduling-b35f526f
type: concept
title: Multi-level topology-aware scheduling
description: 'FEATURE STATE:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/workload-api/topology-aware-scheduling/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

## Multi-level topology-aware scheduling

FEATURE STATE:
`Kubernetes v1.37 [alpha]`(disabled by default)

Complex workloads might require co-location of their Pods at different levels of the cluster
infrastructure. For example, an entire workload may need to run within a single availability zone,
while different parts of that workload may require strict co-location within specific server racks.

Such multi-level co-location requirements can be expressed using the `CompositePodGroup` API and
by specifying topology constraints at different levels of a group hierarchy.

Using the `CompositePodGroup` API requires enabling the
[`CompositePodGroup`](https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/#CompositePodGroup)
feature gate and the
`scheduling.k8s.io/v1alpha3` [API group](https://kubernetes.io/docs/concepts/overview/kubernetes-api/#api-groups-and-versioning "A set of related paths in the Kubernetes API.").