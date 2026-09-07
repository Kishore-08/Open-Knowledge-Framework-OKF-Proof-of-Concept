---
id: kubernetes-integrate-with-workload-apis-bc994bad
type: concept
title: Integrate with Workload APIs
description: 'FEATURE STATE:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/controllers/job/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

## Integrate with Workload APIs

FEATURE STATE:
`Kubernetes v1.36 [alpha]`(disabled by default)

When the [`WorkloadWithJob`](https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/)
feature gate is enabled, the Job controller compiles a Job's `.spec.scheduling`
configuration into [Workload](https://kubernetes.io/docs/concepts/workloads/workload-api/) and
[PodGroup](https://kubernetes.io/docs/concepts/workloads/podgroup-api/) objects (`scheduling.k8s.io/v1beta1`)
before it creates any Pods. This lets you express explicit scheduling intent for a Job,
such as [gang scheduling](https://kubernetes.io/docs/concepts/scheduling-eviction/gang-scheduling/) (all Pods
scheduled together or none), topology co-location, and disruption behavior.

When you omit `.spec.scheduling`, the Job defaults to the `Basic` scheduling
policy, which preserves the standard pod-by-pod scheduling outcome of an ordinary
Job. The controller still creates a `Workload` and `PodGroup` for every
eligible Job (including `Basic` ones), so the observable objects are consistent
regardless of the policy.