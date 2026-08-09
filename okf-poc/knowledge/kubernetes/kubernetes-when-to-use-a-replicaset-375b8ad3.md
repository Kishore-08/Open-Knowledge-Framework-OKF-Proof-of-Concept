---
id: kubernetes-when-to-use-a-replicaset-375b8ad3
type: concept
title: When to use a ReplicaSet
description: A ReplicaSet ensures that a specified number of pod replicas are running
  at any given
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/controllers/replicaset/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

## When to use a ReplicaSet

A ReplicaSet ensures that a specified number of pod replicas are running at any given
time. However, a Deployment is a higher-level concept that manages ReplicaSets and
provides declarative updates to Pods along with a lot of other useful features.
Therefore, we recommend using Deployments instead of directly using ReplicaSets, unless
you require custom update orchestration or don't require updates at all.

This actually means that you may never need to manipulate ReplicaSet objects:
use a Deployment instead, and define your application in the spec section.