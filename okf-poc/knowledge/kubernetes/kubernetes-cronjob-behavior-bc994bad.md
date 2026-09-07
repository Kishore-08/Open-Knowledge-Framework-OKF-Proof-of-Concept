---
id: kubernetes-cronjob-behavior-bc994bad
type: concept
title: CronJob behavior
description: Jobs created by a `CronJob` are standalone; the `CronJob` does not create
  or manage
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/controllers/job/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

### CronJob behavior

Jobs created by a `CronJob` are standalone; the `CronJob` does not create or manage
`Workload` objects. If a `CronJob`'s `jobTemplate` sets `.spec.scheduling`, the Job
controller creates a separate `Workload` and `PodGroup` for each Job instance,
compiled from that Job's `.spec.scheduling` (defaulting to `Basic` when omitted).
These objects are garbage collected when each Job completes or is deleted.