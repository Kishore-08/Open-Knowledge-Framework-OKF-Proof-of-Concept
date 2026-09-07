---
id: kubernetes-what-s-next-bc994bad
type: concept
title: What's next
description: '- Learn about [Pods](https://kubernetes.io/docs/concepts/workloads/pods/).'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/controllers/job/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

## What's next

- Learn about [Pods](https://kubernetes.io/docs/concepts/workloads/pods/).
- Read about different ways of running Jobs:
  - [Coarse Parallel Processing Using a Work Queue](https://kubernetes.io/docs/tasks/job/coarse-parallel-processing-work-queue/)
  - [Fine Parallel Processing Using a Work Queue](https://kubernetes.io/docs/tasks/job/fine-parallel-processing-work-queue/)
  - Use an [indexed Job for parallel processing with static work assignment](https://kubernetes.io/docs/tasks/job/indexed-parallel-processing-static/)
  - Create multiple Jobs based on a template: [Parallel Processing using Expansions](https://kubernetes.io/docs/tasks/job/parallel-processing-expansion/)
- Follow the links within [Clean up finished jobs automatically](https://kubernetes.io/docs/concepts/workloads/controllers/job/#clean-up-finished-jobs-automatically)
  to learn more about how your cluster can clean up completed and / or failed tasks.
- `Job` is part of the Kubernetes REST API.
  Read the
  [Job](https://kubernetes.io/docs/reference/kubernetes-api/batch/job-v1/)
  object definition to understand the API for jobs.
- Read about [`CronJob`](https://kubernetes.io/docs/concepts/workloads/controllers/cron-jobs/), which you
  can use to define a series of Jobs that will run based on a schedule, similar to
  the UNIX tool `cron`.
- Practice how to configure handling of retriable and non-retriable pod failures
  using `podFailurePolicy`, based on the step-by-step [examples](https://kubernetes.io/docs/tasks/job/pod-failure-policy/).
- Learn about [gang scheduling](https://kubernetes.io/docs/concepts/scheduling-eviction/gang-scheduling/)
  for all-or-nothing scheduling of parallel Jobs.