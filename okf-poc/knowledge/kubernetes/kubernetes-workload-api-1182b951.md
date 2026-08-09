---
id: kubernetes-workload-api-1182b951
type: concept
title: Workload API
description: 'FEATURE STATE:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/workload-api/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

# Workload API

FEATURE STATE:
`Kubernetes v1.35 [alpha]`(disabled by default)

The `Workload` API resource defines the scheduling requirements and structure of a multi-Pod
application. While workload controllers such as [Job](https://kubernetes.io/docs/concepts/workloads/controllers/job/)
manage the application's runtime state, the `Workload` specifies how groups of `Pods`
should be scheduled. The Job controller is the only built-in controller that creates
[PodGroup](https://kubernetes.io/docs/concepts/workloads/podgroup-api/) objects from the `Workload`'s
`PodGroupTemplates` at runtime.