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
updated_at: '2026-08-17'
created_at: '2026-08-17'
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
feature gate is enabled and a Job matches the
[gang scheduling criteria](https://kubernetes.io/docs/concepts/workloads/controllers/job/#integrate-with-workload-apis),
updates to `.spec.parallelism` are rejected because the `Workload`'s `minCount` field
is immutable. To scale a gang-scheduled Job, delete and recreate it with the
new parallelism value.