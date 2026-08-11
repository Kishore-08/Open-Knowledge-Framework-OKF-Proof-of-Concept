---
id: kubernetes-progress-deadline-seconds-d9a16560
type: concept
title: Progress Deadline Seconds
description: '`.spec.progressDeadlineSeconds` is an optional field that specifies
  the number of seconds you want'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/controllers/deployment/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Progress Deadline Seconds

`.spec.progressDeadlineSeconds` is an optional field that specifies the number of seconds you want
to wait for your Deployment to progress before the system reports back that the Deployment has
[failed progressing](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/#failed-deployment) - surfaced as a condition with `type: Progressing`, `status: "False"`.
and `reason: ProgressDeadlineExceeded` in the status of the resource. The Deployment controller will keep
retrying the Deployment. This defaults to 600.

If specified, this field needs to be greater than `.spec.minReadySeconds`.