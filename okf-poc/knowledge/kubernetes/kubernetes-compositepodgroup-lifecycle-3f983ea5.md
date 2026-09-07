---
id: kubernetes-compositepodgroup-lifecycle-3f983ea5
type: concept
title: CompositePodGroup Lifecycle
description: 'FEATURE STATE:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/compositepodgroup-api/lifecycle/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

# CompositePodGroup Lifecycle

FEATURE STATE:
`Kubernetes v1.37 [alpha]`(disabled by default)

A [CompositePodGroup](https://kubernetes.io/docs/concepts/workloads/compositepodgroup-api/) represents a non-leaf node
in a multi-level `PodGroup` hierarchy. Unlike `PodGroup` resources, `CompositePodGroup` resources do
not directly contain Pods. Instead, they maintain a hierarchy of descendant `CompositePodGroup` and
`PodGroup` objects and carry scheduling policies that apply to its children groups.