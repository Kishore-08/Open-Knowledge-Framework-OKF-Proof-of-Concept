---
id: kubernetes-workload-placement-3e9846ed
type: concept
title: Workload placement
description: 'FEATURE STATE:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

## Workload placement

FEATURE STATE:
`Kubernetes v1.35 [alpha]`(disabled by default)

While standard workload resources (like Deployments and Jobs) manage the lifecycle of Pods,
you may have complex scheduling requirements where groups of Pods must be treated as a single unit.

The [Workload API](https://kubernetes.io/docs/concepts/workloads/workload-api/) allows you to define `PodGroupTemplates` to group Pods and apply advanced scheduling policies to them,
such as [gang scheduling](https://kubernetes.io/docs/concepts/scheduling-eviction/gang-scheduling/).
Controllers create [PodGroup](https://kubernetes.io/docs/concepts/workloads/podgroup-api/) objects from these templates at runtime,
and `Pods` reference their `PodGroup` via the
`spec.schedulingGroup` field. This is particularly useful for batch processing and machine
learning workloads where "all-or-nothing" placement is required.