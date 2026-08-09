---
id: kubernetes-ownership-and-lifecycle-3f08e71b
type: concept
title: Ownership and lifecycle
description: '`PodGroups` are owned by the workload controller that created them (for
  example, a Job)'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/podgroup-api/lifecycle/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

## Ownership and lifecycle

`PodGroups` are owned by the workload controller that created them (for example, a Job)
via standard `ownerReferences`. When the owning object is deleted, `PodGroups` are
automatically garbage collected.

`PodGroup` names must be unique within a namespace and must be valid
[DNS subdomains](https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#dns-subdomain-names).