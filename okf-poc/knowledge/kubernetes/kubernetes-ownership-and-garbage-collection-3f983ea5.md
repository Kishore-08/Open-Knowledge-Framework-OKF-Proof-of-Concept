---
id: kubernetes-ownership-and-garbage-collection-3f983ea5
type: concept
title: Ownership and garbage collection
description: A `CompositePodGroup` object, together with its descendant `CompositePodGroup`
  and `PodGroup`
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/compositepodgroup-api/lifecycle/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

## Ownership and garbage collection

A `CompositePodGroup` object, together with its descendant `CompositePodGroup` and `PodGroup`
resources, is owned by the workload controller that created it via Kubernetes `ownerReferences`.
When the owning workload object gets deleted, cascading garbage collection automatically deletes the
associated group hierarchy.

`CompositePodGroup` names must be unique within a namespace and must be valid
[DNS subdomains](https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#dns-subdomain-names).