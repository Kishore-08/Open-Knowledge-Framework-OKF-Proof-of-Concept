---
id: kubernetes-best-effort-pods-scope-193abbf6
type: concept
title: Best effort Pods scope
description: This scope only tracks quota consumed by Pods.
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/policy/resource-quotas/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Best effort Pods scope

This scope only tracks quota consumed by Pods.
It only matches pods that have the [best effort](https://kubernetes.io/docs/concepts/workloads/pods/pod-qos/#besteffort)
[QoS class](https://kubernetes.io/docs/concepts/workloads/pods/pod-qos/).

The `operator` for a `scopeSelector` must be `Exists`.