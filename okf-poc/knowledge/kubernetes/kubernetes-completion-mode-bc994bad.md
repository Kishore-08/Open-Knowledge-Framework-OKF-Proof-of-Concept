---
id: kubernetes-completion-mode-bc994bad
type: concept
title: Completion mode
description: 'FEATURE STATE:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/controllers/job/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

### Completion mode

FEATURE STATE:
`Kubernetes v1.24 [stable]`

Jobs with *fixed completion count* - that is, jobs that have non null
`.spec.completions` - can have a completion mode that is specified in `.spec.completionMode`:

- `NonIndexed` (default): the Job is considered complete when there have been
  `.spec.completions` successfully completed Pods. In other words, each Pod
  completion is homologous to each other. Note that Jobs that have null
  `.spec.completions` are implicitly `NonIndexed`.
- `Indexed`: the Pods of a Job get an associated completion index from 0 to
  `.spec.completions-1`. The index is available through four mechanisms:

  - The Pod annotation `batch.kubernetes.io/job-completion-index`.
  - The Pod label `batch.kubernetes.io/job-completion-index` (for v1.28 and later). Note
    the feature gate `PodIndexLabel` must be enabled to use this label, and it is enabled
    by default.
  - As part of the Pod hostname, following the pattern `$(job-name)-$(index)`.
    When you use an Indexed Job in combination with a
    [Service](https://kubernetes.io/docs/concepts/services-networking/service/ "A way to expose an application running on a set of Pods as a network service."), Pods within the Job can use
    the deterministic hostnames to address each other via DNS. For more information about
    how to configure this, see [Job with Pod-to-Pod Communication](https://kubernetes.io/docs/tasks/job/job-with-pod-to-pod-communication/).
  - From the containerized task, in the environment variable `JOB_COMPLETION_INDEX`.

  The Job is considered complete when there is one successfully completed Pod
  for each index. For more information about how to use this mode, see
  [Indexed Job for Parallel Processing with Static Work Assignment](https://kubernetes.io/docs/tasks/job/indexed-parallel-processing-static/).

#### Note:

Although rare, more than one Pod could be started for the same index (due to various reasons such as node failures,
kubelet restarts, or Pod evictions). In this case, only the first Pod that completes successfully will
count towards the completion count and update the status of the Job. The other Pods that are running
or completed for the same index will be deleted by the Job controller once they are detected.