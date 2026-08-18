---
id: kubernetes-job-tracking-with-finalizers-bc994bad
type: concept
title: Job tracking with finalizers
description: 'FEATURE STATE:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/controllers/job/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

### Job tracking with finalizers

FEATURE STATE:
`Kubernetes v1.26 [stable]`

The control plane keeps track of the Pods that belong to any Job and notices if
any such Pod is removed from the API server. To do that, the Job controller
creates Pods with the finalizer `batch.kubernetes.io/job-tracking`. The
controller removes the finalizer only after the Pod has been accounted for in
the Job status, allowing the Pod to be removed by other controllers or users.

#### Note:

See [My pod stays terminating](https://kubernetes.io/docs/tasks/debug/debug-application/debug-pods/) if you
observe that pods from a Job are stuck with the tracking finalizer.