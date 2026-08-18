---
id: kubernetes-limitations-for-alpha-release-bc994bad
type: concept
title: Limitations for Alpha release
description: '- Each Job maps to exactly one `PodGroup`. All Pods in the Job belong
  to the same'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/controllers/job/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

### Limitations for Alpha release

- Each Job maps to exactly one `PodGroup`. All Pods in the Job belong to the same
  scheduling group.
- The `minCount` in the gang policy is immutable. Updates to `.spec.parallelism`
  are rejected for Jobs that use gang scheduling. See
  [Elastic Indexed Jobs](https://kubernetes.io/docs/concepts/workloads/controllers/job/#elastic-indexed-jobs) for details on this restriction.
- Suspended Jobs retain their `Workload` and `PodGroup` objects; they are not deleted
  on suspend or recreated on resume.