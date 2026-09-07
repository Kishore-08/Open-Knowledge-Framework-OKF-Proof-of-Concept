---
id: kubernetes-pod-backoff-failure-policy-bc994bad
type: concept
title: Pod backoff failure policy
description: There are situations where you want to fail a Job after some amount of
  retries
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/controllers/job/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

### Pod backoff failure policy

There are situations where you want to fail a Job after some amount of retries
due to a logical error in configuration etc.
To do so, set `.spec.backoffLimit` to specify the number of retries before
considering a Job as failed.

The `.spec.backoffLimit` is set by default to 6, unless the
[backoff limit per index](https://kubernetes.io/docs/concepts/workloads/controllers/job/#backoff-limit-per-index) (only Indexed Job) is specified.
When `.spec.backoffLimitPerIndex` is specified, then `.spec.backoffLimit` defaults
to 2147483647 (MaxInt32).

Failed Pods associated with the Job are recreated by the Job controller with an
exponential back-off delay (10s, 20s, 40s ...) capped at six minutes.

The number of retries is calculated in two ways:

- The number of Pods with `.status.phase = "Failed"`.
- When using `restartPolicy = "OnFailure"`, the number of retries in all the
  containers of Pods with `.status.phase` equal to `Pending` or `Running`.

If either of the calculations reaches the `.spec.backoffLimit`, the Job is
considered failed.

#### Note:

If your Job has `restartPolicy = "OnFailure"`, keep in mind that your Pod running the job
will be terminated once the job backoff limit has been reached. This can make debugging
the Job's executable more difficult. We suggest setting
`restartPolicy = "Never"` when debugging the Job or using a logging system to ensure output
from failed Jobs is not lost inadvertently.