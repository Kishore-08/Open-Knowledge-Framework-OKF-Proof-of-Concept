---
id: kubernetes-kube-scheduler-metrics-36c52094
type: concept
title: '`kube-scheduler` metrics'
description: The following scheduler metrics are high level metrics aggregating performance
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/cluster-administration/dra/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

### `kube-scheduler` metrics

The following scheduler metrics are high level metrics aggregating performance
across all Pods scheduled, not just those using DRA. It is important to note
that the end-to-end metrics are ultimately influenced by the
`kube-controller-manager`'s performance in creating ResourceClaims from
ResourceClainTemplates in deployments that heavily use ResourceClainTemplates.

- Scheduler End-to-End Duration: Monitor `histogram_quantile(0.99,
  sum(increase(scheduler_pod_scheduling_sli_duration_seconds_bucket[5m])) by
  (le))`.
- Scheduler Algorithm Latency: Track `histogram_quantile(0.99,
  sum(increase(scheduler_scheduling_algorithm_duration_seconds_bucket[5m])) by
  (le))`.