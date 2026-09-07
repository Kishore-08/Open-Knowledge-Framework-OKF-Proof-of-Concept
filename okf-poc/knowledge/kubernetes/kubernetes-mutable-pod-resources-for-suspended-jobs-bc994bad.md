---
id: kubernetes-mutable-pod-resources-for-suspended-jobs-bc994bad
type: concept
title: Mutable Pod resources for suspended Jobs
description: 'FEATURE STATE:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/controllers/job/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

### Mutable Pod resources for suspended Jobs

FEATURE STATE:
`Kubernetes v1.36 [beta]`(enabled by default)

A cluster administrator can define admission controls in Kubernetes, modifying the resource requests or limits for a Job, based on policy rules.

With this feature, Kubernetes also lets you modify the pod template of a [suspended job](https://kubernetes.io/docs/concepts/workloads/controllers/job/#suspending-a-job), to change the resource requirements of the Pods in the Job.
This is different from *in-place Pod resize* which lets you update resources, one Pod at a time, for Pods that are already running.

The client that sets the new resource requests or limits can be different from the client that initially created the Job, and does not need to be a cluster administrator.