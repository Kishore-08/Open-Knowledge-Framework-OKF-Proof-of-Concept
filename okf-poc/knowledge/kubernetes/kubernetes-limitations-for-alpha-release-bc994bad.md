---
id: kubernetes-limitations-for-alpha-release-bc994bad
type: concept
title: Limitations for Alpha release
description: '- Each Job maps to exactly one `PodGroup`; all Pods in the Job share
  a single'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/controllers/job/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

### Limitations for Alpha release

- Each Job maps to exactly one `PodGroup`; all Pods in the Job share a single
  scheduling policy.
- Only `schedulingPolicy.gang.minCount` is mutable; all other `.spec.scheduling`
  fields are immutable after creation.
- Suspended Jobs retain their `Workload` and `PodGroup` objects; they are not deleted
  on suspend or recreated on resume.