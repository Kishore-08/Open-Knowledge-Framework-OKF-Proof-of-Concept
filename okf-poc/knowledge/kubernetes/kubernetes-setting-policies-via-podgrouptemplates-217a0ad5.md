---
id: kubernetes-setting-policies-via-podgrouptemplates-217a0ad5
type: concept
title: Setting policies via PodGroupTemplates
description: When using the [Workload API](https://kubernetes.io/docs/concepts/workloads/workload-api/),
  you define scheduling
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/workload-api/policies/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

## Setting policies via PodGroupTemplates

When using the [Workload API](https://kubernetes.io/docs/concepts/workloads/workload-api/), you define scheduling
policies inside `PodGroupTemplates`. The workload controller copies the policy from the
template into each PodGroup it creates, making the PodGroup self-contained. Changes to the
Workload's templates only affect newly created PodGroups, not existing ones.

For standalone PodGroups (created without a Workload), you set `spec.schedulingPolicy`
directly on the PodGroup itself.