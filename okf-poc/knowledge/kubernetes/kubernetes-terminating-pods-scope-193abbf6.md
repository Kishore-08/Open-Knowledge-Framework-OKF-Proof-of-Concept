---
id: kubernetes-terminating-pods-scope-193abbf6
type: concept
title: Terminating Pods scope
description: This scope only tracks quota consumed by Pods that are terminating. The
  `operator` for a `scopeSelector`
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/policy/resource-quotas/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Terminating Pods scope

This scope only tracks quota consumed by Pods that are terminating. The `operator` for a `scopeSelector`
must be `Exists`.

A Pod is considered as *terminating* if the `.spec.activeDeadlineSeconds` field is set to any number.

You can use a ResourceQuota with this scope to manage the following resources:

- `count.pods`
- `pods`
- `cpu`
- `memory`
- `requests.cpu`
- `requests.memory`
- `limits.cpu`
- `limits.memory`