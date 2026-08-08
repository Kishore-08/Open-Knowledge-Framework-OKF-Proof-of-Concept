---
id: kubernetes-replicas-375b8ad3
type: concept
title: Replicas
description: You can specify how many Pods should run concurrently by setting `.spec.replicas`.
  The ReplicaSet will create/delete
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/controllers/replicaset/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Replicas

You can specify how many Pods should run concurrently by setting `.spec.replicas`. The ReplicaSet will create/delete
its Pods to match this number.

If you do not specify `.spec.replicas`, then it defaults to 1.

## Working with ReplicaSets