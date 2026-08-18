---
id: kubernetes-clean-up-finished-jobs-automatically-bc994bad
type: concept
title: Clean up finished jobs automatically
description: Finished Jobs are usually no longer needed in the system. Keeping them
  around in
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/controllers/job/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

## Clean up finished jobs automatically

Finished Jobs are usually no longer needed in the system. Keeping them around in
the system will put pressure on the API server. If the Jobs are managed directly
by a higher level controller, such as
[CronJobs](https://kubernetes.io/docs/concepts/workloads/controllers/cron-jobs/), the Jobs can be
cleaned up by CronJobs based on the specified capacity-based cleanup policy.