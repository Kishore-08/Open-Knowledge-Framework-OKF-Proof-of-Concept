---
id: kubernetes-mutable-scheduling-directives-bc994bad
type: concept
title: Mutable Scheduling Directives
description: 'FEATURE STATE:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/controllers/job/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

### Mutable Scheduling Directives

FEATURE STATE:
`Kubernetes v1.27 [stable]`

In most cases, a parallel job will want the pods to run with constraints,
like all in the same zone, or all either on GPU model x or y but not a mix of both.

The [suspend](https://kubernetes.io/docs/concepts/workloads/controllers/job/#suspending-a-job) field is the first step towards achieving those semantics. Suspend allows a
custom queue controller to decide when a job should start; However, once a job is unsuspended,
a custom queue controller has no influence on where the pods of a job will actually land.

This feature allows updating a Job's scheduling directives before it starts, which gives custom queue
controllers the ability to influence pod placement while at the same time offloading actual
pod-to-node assignment to kube-scheduler.

The fields in a Job's pod template that can be updated are node affinity, node selector,
tolerations, labels, annotations and [scheduling gates](https://kubernetes.io/docs/concepts/scheduling-eviction/pod-scheduling-readiness/).

#### Mutable Scheduling Directives for suspended Jobs

FEATURE STATE:
`Kubernetes v1.36 [beta]`(enabled by default)

In Kubernetes 1.34 or earlier mutating of Pod's scheduling directives is allowed only for
suspended Jobs that have never been unsuspended before. In Kubernetes 1.35, this is allowed
for any suspended Jobs when the `MutableSchedulingDirectivesForSuspendedJobs` feature gate is enabled.

Additionally, this feature gate enables clearing of the `.status.startTime` field on [Job suspension](https://kubernetes.io/docs/concepts/workloads/controllers/job/#suspending-a-job).