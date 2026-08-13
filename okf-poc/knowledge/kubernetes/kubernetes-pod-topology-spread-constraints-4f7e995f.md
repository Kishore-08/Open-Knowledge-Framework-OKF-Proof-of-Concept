---
id: kubernetes-pod-topology-spread-constraints-4f7e995f
type: concept
title: Pod Topology Spread Constraints
description: You can use *topology spread constraints* to control how
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/scheduling-eviction/topology-spread-constraints/
updated_at: '2026-08-13'
created_at: '2026-08-13'
---

# Pod Topology Spread Constraints

You can use *topology spread constraints* to control how
[Pods](https://kubernetes.io/docs/concepts/workloads/pods/ "A Pod represents a set of running containers in your cluster.") are spread across your cluster
among failure-domains such as regions, zones, nodes, and other user-defined topology
domains. This can help to achieve high availability as well as efficient resource
utilization.

You can set [cluster-level constraints](https://kubernetes.io/docs/concepts/scheduling-eviction/topology-spread-constraints/#cluster-level-default-constraints) as a default,
or configure topology spread constraints for individual workloads.