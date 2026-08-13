---
id: kubernetes-terminal-job-conditions-bc994bad
type: concept
title: Terminal Job conditions
description: A Job has two possible terminal states, each of which has a corresponding
  Job
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/controllers/job/
updated_at: '2026-08-13'
created_at: '2026-08-13'
---

### Terminal Job conditions

A Job has two possible terminal states, each of which has a corresponding Job
condition:

- Succeeded: Job condition `Complete`
- Failed: Job condition `Failed`

Jobs fail for the following reasons:

- The number of Pod failures exceeded the specified `.spec.backoffLimit` in the Job
  specification. For details, see [Pod backoff failure policy](https://kubernetes.io/docs/concepts/workloads/controllers/job/#pod-backoff-failure-policy).
- The Job runtime exceeded the specified `.spec.activeDeadlineSeconds`
- An indexed Job that used `.spec.backoffLimitPerIndex` has failed indexes.
  For details, see [Backoff limit per index](https://kubernetes.io/docs/concepts/workloads/controllers/job/#backoff-limit-per-index).
- The number of failed indexes in the Job exceeded the specified
  `spec.maxFailedIndexes`. For details, see [Backoff limit per index](https://kubernetes.io/docs/concepts/workloads/controllers/job/#backoff-limit-per-index)
- A failed Pod matches a rule in `.spec.podFailurePolicy` that has the `FailJob`
  action. For details about how Pod failure policy rules might affect failure
  evaluation, see [Pod failure policy](https://kubernetes.io/docs/concepts/workloads/controllers/job/#pod-failure-policy).

Jobs succeed for the following reasons:

- The number of succeeded Pods reached the specified `.spec.completions`
- The criteria specified in `.spec.successPolicy` are met. For details, see
  [Success policy](https://kubernetes.io/docs/concepts/workloads/controllers/job/#success-policy).

In Kubernetes v1.31 and later the Job controller delays the addition of the
terminal conditions,`Failed` or `Complete`, until all of the Job Pods are terminated.

In Kubernetes v1.30 and earlier, the Job controller added the `Complete` or the
`Failed` Job terminal conditions as soon as the Job termination process was
triggered and all Pod finalizers were removed. However, some Pods would still
be running or terminating at the moment that the terminal condition was added.

In Kubernetes v1.31 and later, the controller only adds the Job terminal conditions
*after* all of the Pods are terminated. You can control this behavior by using the
`JobManagedBy` and the `JobPodReplacementPolicy` (both enabled by default)
[feature gates](https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/).