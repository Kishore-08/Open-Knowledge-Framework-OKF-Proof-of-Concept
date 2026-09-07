---
id: kubernetes-scheduling-policy-497d3b3e
type: concept
title: Scheduling policy
description: The scheduling policy block carries the same `basic` and `gang` policies
  as a PodGroup's
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/workload-api/workloadbuilder/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

### Scheduling policy

The scheduling policy block carries the same `basic` and `gang` policies as a PodGroup's
`spec.schedulingPolicy`. See
[PodGroup scheduling policies](https://kubernetes.io/docs/concepts/workloads/workload-api/policies/)
for what each policy means and how the scheduler applies it.

The one difference is that the block's `gang` minimum count is optional. Users may leave
`minCount` unset, in which case the controller supplies a default that makes sense for its
own domain; the Job controller, for example, uses the Job's parallelism.