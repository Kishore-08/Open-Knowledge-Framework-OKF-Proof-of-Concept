---
id: kubernetes-referencing-a-workload-controlling-object-1182b951
type: concept
title: Referencing a workload controlling object
description: The `controllerRef` field links the Workload back to the specific high-level
  object defining the application,
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/workload-api/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Referencing a workload controlling object

The `controllerRef` field links the Workload back to the specific high-level object defining the application,
such as a [Job](https://kubernetes.io/docs/concepts/workloads/controllers/job/) or a custom CRD. This is useful for observability and tooling.
This data is not used to schedule or manage the Workload.