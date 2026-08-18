---
id: kubernetes-opt-out-for-higher-level-controllers-bc994bad
type: concept
title: Opt-out for higher-level controllers
description: If a Job's Pod template already has `spec.schedulingGroup` set, the Job
  controller
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/controllers/job/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

### Opt-out for higher-level controllers

If a Job's Pod template already has `spec.schedulingGroup` set, the Job controller
does not create `Workload` or `PodGroup` objects. This allows higher-level controllers
such as `JobSet` to manage the `Workload` and `PodGroup` lifecycle themselves.