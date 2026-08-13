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
updated_at: '2026-08-13'
created_at: '2026-08-13'
---

## Integrate with Workload APIs

FEATURE STATE:
`Kubernetes v1.36 [alpha]`(disabled by default)

When the [`WorkloadWithJob`](https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/) feature gate is enabled,
the Job controller automatically creates
[Workload](https://kubernetes.io/docs/concepts/workloads/workload-api/) and
[PodGroup](https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/workload-v1alpha1/) objects
for [qualifying parallel Jobs](https://kubernetes.io/docs/concepts/workloads/controllers/job/#qualifying-criteria) before creating any Pods.
This enables native [gang scheduling](https://kubernetes.io/docs/concepts/scheduling-eviction/gang-scheduling/)
where all Pods in a Job are scheduled together or none are scheduled.