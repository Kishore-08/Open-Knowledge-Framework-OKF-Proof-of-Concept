---
id: kubernetes-api-configuration-scheduling-constraints-b35f526f
type: concept
title: 'API configuration: scheduling constraints'
description: Every PodGroup (or PodGroupTemplate) may optionally declare the `schedulingConstraints`
  field,
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/workload-api/topology-aware-scheduling/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

## API configuration: scheduling constraints

Every PodGroup (or PodGroupTemplate) may optionally declare the `schedulingConstraints` field,
which is interpreted by the [placement-based PodGroup scheduling algorithm](https://kubernetes.io/docs/concepts/scheduling-eviction/podgroup-scheduling/#placement-scheduling-algorithm).
If constraints are defined in PodGroupTemplate, they will be copied to referencing PodGroups.

As of Kubernetes v1.36, the API supports topology constraints.

#### Note:

As of Kubernetes v1.36, you can specify only a single topology constraint in each PodGroup.