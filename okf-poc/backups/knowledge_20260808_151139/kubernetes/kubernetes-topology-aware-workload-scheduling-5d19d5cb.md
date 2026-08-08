---
id: kubernetes-topology-aware-workload-scheduling-5d19d5cb
type: concept
title: Topology-Aware Workload Scheduling
description: 'FEATURE STATE:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/scheduling-eviction/topology-aware-scheduling/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

# Topology-Aware Workload Scheduling

FEATURE STATE:
`Kubernetes v1.36 [alpha]`(disabled by default)

*Topology-Aware Scheduling* (TAS) is a [placement scheduling algorithm](https://kubernetes.io/docs/concepts/scheduling-eviction/podgroup-scheduling/#placement-scheduling-algorithm)
that allows finding the optimal placement for the considered PodGroup, guaranteeing that all pods
will be collocated within the same topology domain. Users can adapt TAS to their specific
needs by changing TAS plugins configuration.