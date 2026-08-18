---
id: kubernetes-postfilter-085106f9
type: concept
title: PostFilter
description: These plugins are called after the Filter phase, but only when no feasible
  nodes
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/scheduling-eviction/scheduling-framework/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

### PostFilter

These plugins are called after the Filter phase, but only when no feasible nodes
were found for the pod. Plugins are called in their configured order. If
any postFilter plugin marks the node as `Schedulable`, the remaining plugins
will not be called. A typical PostFilter implementation is preemption, which
tries to make the pod schedulable by preempting other Pods.

### PreScore

These plugins are used to perform "pre-scoring" work, which generates a sharable
state for Score plugins to use. If a PreScore plugin returns an error, the
scheduling cycle is aborted.