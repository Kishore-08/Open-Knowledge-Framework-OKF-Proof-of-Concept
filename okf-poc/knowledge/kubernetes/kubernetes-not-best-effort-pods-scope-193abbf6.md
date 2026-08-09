---
id: kubernetes-not-best-effort-pods-scope-193abbf6
type: concept
title: Not-best-effort Pods scope
description: This scope only tracks quota consumed by Pods.
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/policy/resource-quotas/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Not-best-effort Pods scope

This scope only tracks quota consumed by Pods.
It only matches pods that have the [Guaranteed](https://kubernetes.io/docs/concepts/workloads/pods/pod-qos/#guaranteed)
or [Burstable](https://kubernetes.io/docs/concepts/workloads/pods/pod-qos/#burstable)
[QoS class](https://kubernetes.io/docs/concepts/workloads/pods/pod-qos/).

The `operator` for a `scopeSelector` must be `Exists`.