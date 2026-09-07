---
id: kubernetes-setting-composite-policies-via-templates-217a0ad5
type: concept
title: Setting composite policies via templates
description: When using the [Workload API](https://kubernetes.io/docs/concepts/workloads/workload-api/),
  scheduling policies for
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/workload-api/policies/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

### Setting composite policies via templates

When using the [Workload API](https://kubernetes.io/docs/concepts/workloads/workload-api/), scheduling policies for
`CompositePodGroups` are defined inside `CompositePodGroupTemplates`. Workload controllers copy the
`schedulingPolicy` specified in the templates into each `CompositePodGroup` created at runtime.
Unlike leaf `PodGroupTemplates` where `minCount` can be updated, `minGroupCount` in a
`CompositePodGroupTemplate` is immutable.