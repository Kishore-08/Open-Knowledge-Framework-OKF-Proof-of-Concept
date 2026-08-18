---
id: kubernetes-cronjob-behavior-bc994bad
type: concept
title: CronJob behavior
description: Jobs created by a `CronJob` do not have `schedulingGroup` set in the
  `PodTemplate`.
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/controllers/job/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

### CronJob behavior

Jobs created by a `CronJob` do not have `schedulingGroup` set in the `PodTemplate`.
If a CronJob-created `Job` matches the gang scheduling criteria, the Job controller
creates a separate `Workload` and `PodGroup` for each Job instance.