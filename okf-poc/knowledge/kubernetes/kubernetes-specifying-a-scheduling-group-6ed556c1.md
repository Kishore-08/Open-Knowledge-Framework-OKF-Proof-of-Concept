---
id: kubernetes-specifying-a-scheduling-group-6ed556c1
type: concept
title: Specifying a scheduling group
description: 'FEATURE STATE:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/pods/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Specifying a scheduling group

FEATURE STATE:
`Kubernetes v1.35 [alpha]`(disabled by default)

By default, Kubernetes schedules every Pod individually. However, some tightly-coupled applications
need a group of Pods to be scheduled simultaneously to function correctly.

You can link a Pod to a [PodGroup](https://kubernetes.io/docs/concepts/workloads/podgroup-api/) using the
[scheduling group](https://kubernetes.io/docs/concepts/workloads/pods/scheduling-group/) field
(`spec.schedulingGroup`). This tells the `kube-scheduler` that the `Pod` belongs to a specific
group, enabling it to apply group-level coordinated placement decisions for the entire group at once.