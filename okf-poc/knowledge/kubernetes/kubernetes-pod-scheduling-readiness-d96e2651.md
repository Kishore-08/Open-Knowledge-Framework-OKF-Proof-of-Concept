---
id: kubernetes-pod-scheduling-readiness-d96e2651
type: concept
title: Pod Scheduling Readiness
description: 'FEATURE STATE:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/scheduling-eviction/pod-scheduling-readiness/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

# Pod Scheduling Readiness

FEATURE STATE:
`Kubernetes v1.30 [stable]`

Pods were considered ready for scheduling once created. Kubernetes scheduler
does its due diligence to find nodes to place all pending Pods. However, in a
real-world case, some Pods may stay in a "miss-essential-resources" state for a long period.
These Pods actually churn the scheduler (and downstream integrators like Cluster AutoScaler)
in an unnecessary manner.

By specifying/removing a Pod's `.spec.schedulingGates`, you can control when a Pod is ready
to be considered for scheduling.