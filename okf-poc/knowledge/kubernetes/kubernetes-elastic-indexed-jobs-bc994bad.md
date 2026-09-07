---
id: kubernetes-elastic-indexed-jobs-bc994bad
type: concept
title: Elastic Indexed Jobs
description: 'FEATURE STATE:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/controllers/job/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

### Elastic Indexed Jobs

FEATURE STATE:
`Kubernetes v1.31 [stable]`(enabled by default)

You can scale Indexed Jobs up or down by mutating both `.spec.parallelism`
and `.spec.completions` together such that `.spec.parallelism == .spec.completions`.
When scaling down, Kubernetes removes the Pods with higher indexes.

Use cases for elastic Indexed Jobs include batch workloads which require
scaling an indexed Job, such as MPI, Horovod, Ray, and PyTorch training jobs.

#### Note:

When the [`WorkloadWithJob`](https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/)
feature gate is enabled and a Job uses [gang scheduling](https://kubernetes.io/docs/concepts/workloads/controllers/job/#integrate-with-workload-apis),
the gang size follows the mutable `schedulingPolicy.gang.minCount` (or
`.spec.parallelism` when `minCount` is unset).
You can scale the gang in one of two ways:

- set `.spec.scheduling.schedulingPolicy.gang.minCount` directly, or
- change `.spec.parallelism` when `minCount` is unset.

On either change, the controller recompiles the `Workload` and re-syncs the
`PodGroup` size, rescaling the gang in place without recreating the Job. Updates
apply only to Pods evaluated in future scheduling cycles and do not affect
already-scheduled Pods. A `gang.minCount` greater than `.spec.parallelism` is
rejected, since such a gang can never be satisfied.