---
id: kubernetes-gang-scheduling-with-jobs-1182b951
type: concept
title: Gang scheduling with Jobs
description: 'FEATURE STATE:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/workload-api/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

## Gang scheduling with Jobs

FEATURE STATE:
`Kubernetes v1.36 [alpha]`(disabled by default)

When the
[`WorkloadWithJob`](https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/)
feature gate is enabled, the
[Job](https://kubernetes.io/docs/concepts/workloads/controllers/job/) controller automatically
creates Workload and PodGroup objects for parallel indexed Jobs where
`.spec.parallelism` equals `.spec.completions`. The gang policy's `minCount`
is set to the Job's parallelism, so all Pods must be schedulable together
before any of them are bound to nodes.

This is the built-in path for using gang scheduling with Jobs.
You do not need to create Workload or PodGroup objects yourself as the Job
controller handles it automatically. Other workload controllers (such as
JobSet) may manage their own Workload and PodGroup objects independently.