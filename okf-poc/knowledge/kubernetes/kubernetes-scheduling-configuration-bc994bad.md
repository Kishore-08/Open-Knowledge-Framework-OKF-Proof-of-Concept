---
id: kubernetes-scheduling-configuration-bc994bad
type: concept
title: Scheduling configuration
description: 'The `.spec.scheduling` field accepts the following fields:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/controllers/job/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

### Scheduling configuration

The `.spec.scheduling` field accepts the following fields:

- `schedulingPolicy`: exactly one of `basic` or `gang` must be specified. With `gang`,
  all Pods must be schedulable together before any of them are bound. An omitted
  `gang.minCount` defaults to the Job's `.spec.parallelism`. See
  [PodGroup scheduling policies](https://kubernetes.io/docs/concepts/workloads/workload-api/policies/).
- `schedulingConstraints`:
  [topology](https://kubernetes.io/docs/concepts/workloads/workload-api/topology-aware-scheduling/)
  co-location constraints for the Job's Pods.
- `disruptionMode`: whether the Pods are disrupted individually (`single`) or as a
  group (`all`). See
  [disruption and priority](https://kubernetes.io/docs/concepts/workloads/workload-api/disruption-and-priority/).
- `resourceClaims`: dynamic resource claims shared across the Job's Pods.

All `.spec.scheduling` fields are immutable after the Job is created, except for
`schedulingPolicy.gang.minCount`, which you can change to
[scale a gang elastically](https://kubernetes.io/docs/concepts/workloads/controllers/job/#elastic-indexed-jobs).