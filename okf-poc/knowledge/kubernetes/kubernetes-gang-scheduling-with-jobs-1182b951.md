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
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

## Gang scheduling with Jobs

FEATURE STATE:
`Kubernetes v1.36 [alpha]`(disabled by default)

When the
[`WorkloadWithJob`](https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/)
feature gate is enabled, the
[Job](https://kubernetes.io/docs/concepts/workloads/controllers/job/) controller compiles a Job's
`.spec.scheduling` configuration into `Workload` and `PodGroup` objects before it
creates any Pods. You opt into gang scheduling by setting
`.spec.scheduling.schedulingPolicy.gang` on the Job; an omitted `gang.minCount`
defaults to the Job's `.spec.parallelism`, so all Pods must be schedulable together
before any of them are bound to nodes.

When `.spec.scheduling` is omitted, the Job defaults to the `basic` policy, which
preserves standard pod-by-pod scheduling. Either way the Job controller creates the
`Workload` and `PodGroup` for you, so you do not need to create them yourself.
Other workload controllers (such as JobSet) may manage their own `Workload` and
`PodGroup` objects independently.

For the full set of scheduling fields and examples, see
[Integrate with Workload APIs](https://kubernetes.io/docs/concepts/workloads/controllers/job/#integrate-with-workload-apis).