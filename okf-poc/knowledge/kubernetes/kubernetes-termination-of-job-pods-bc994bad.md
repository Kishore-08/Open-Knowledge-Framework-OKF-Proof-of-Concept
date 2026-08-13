---
id: kubernetes-termination-of-job-pods-bc994bad
type: concept
title: Termination of Job pods
description: The Job controller adds the `FailureTarget` condition or the `SuccessCriteriaMet`
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/controllers/job/
updated_at: '2026-08-13'
created_at: '2026-08-13'
---

### Termination of Job pods

The Job controller adds the `FailureTarget` condition or the `SuccessCriteriaMet`
condition to the Job to trigger Pod termination after a Job meets either the
success or failure criteria.

Factors like `terminationGracePeriodSeconds` might increase the amount of time
from the moment that the Job controller adds the `FailureTarget` condition or the
`SuccessCriteriaMet` condition to the moment that all of the Job Pods terminate
and the Job controller adds a [terminal condition](https://kubernetes.io/docs/concepts/workloads/controllers/job/#terminal-job-conditions)
(`Failed` or `Complete`).

You can use the `FailureTarget` or the `SuccessCriteriaMet` condition to evaluate
whether the Job has failed or succeeded without having to wait for the controller
to add a terminal condition.

For example, you might want to decide when to create a replacement Job
that replaces a failed Job. If you replace the failed Job when the `FailureTarget`
condition appears, your replacement Job runs sooner, but could result in Pods
from the failed and the replacement Job running at the same time, using
extra compute resources.

Alternatively, if your cluster has limited resource capacity, you could choose to
wait until the `Failed` condition appears on the Job, which would delay your
replacement Job but would ensure that you conserve resources by waiting
until all of the failed Pods are removed.