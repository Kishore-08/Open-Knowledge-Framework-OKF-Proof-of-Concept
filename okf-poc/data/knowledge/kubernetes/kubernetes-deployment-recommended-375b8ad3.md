---
id: kubernetes-deployment-recommended-375b8ad3
type: concept
title: Deployment (recommended)
description: '[`Deployment`](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/)
  is an object which can own ReplicaSets and update'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/controllers/replicaset/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Deployment (recommended)

[`Deployment`](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/) is an object which can own ReplicaSets and update
them and their Pods via declarative, server-side rolling updates.
While ReplicaSets can be used independently, today they're mainly used by Deployments as a mechanism to orchestrate Pod
creation, deletion and updates. When you use Deployments you don't have to worry about managing the ReplicaSets that
they create. Deployments own and manage their ReplicaSets.
As such, it is recommended to use Deployments when you want ReplicaSets.