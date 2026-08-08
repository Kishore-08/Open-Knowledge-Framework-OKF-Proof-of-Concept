---
id: kubernetes-topology-aware-workload-scheduling-b35f526f
type: concept
title: Topology-Aware Workload Scheduling
description: 'FEATURE STATE:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/workload-api/topology-aware-scheduling/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

# Topology-Aware Workload Scheduling

FEATURE STATE:
`Kubernetes v1.36 [alpha]`(disabled by default)

*Topology-Aware Scheduling* (TAS) is a feature of the Workload API that optimizes the placement of
pods within the cluster.

TAS ensures that all pods within a PodGroup are co-located into a specific topology domain,
such as a single server rack or zone. This minimizes inter-pod communication latency and prevents
workload fragmentation across the cluster infrastructure.