---
id: kubernetes-deletion-protection-3f08e71b
type: concept
title: Deletion protection
description: A `PodGroup` cannot be fully deleted while any of its Pods are still
  running.
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/podgroup-api/lifecycle/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

## Deletion protection

A `PodGroup` cannot be fully deleted while any of its Pods are still running.
A dedicated finalizer ensures that deletion is blocked until all `Pods` referencing the
`PodGroup` have reached a terminal phase (`Succeeded` or `Failed`).