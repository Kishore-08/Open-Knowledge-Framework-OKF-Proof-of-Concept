---
id: kubernetes-recreate-f82fae6f
type: concept
title: Recreate
description: 'FEATURE STATE:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

## Recreate

FEATURE STATE:
`Kubernetes v1.37 [alpha]`(disabled by default)

When a StatefulSet's `.spec.updateStrategy.type` is set to `Recreate`, the StatefulSet
controller deletes all of the StatefulSet's Pods at once and waits for them to terminate
completely before creating any new Pods from the updated `.spec.template`. Unlike
[`RollingUpdate`](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/#rolling-updates), the old and new revisions of a Pod are never running at
the same time, so this strategy incurs downtime for the duration of the update. This mirrors
the `Recreate` strategy of Deployments and is useful for applications that cannot run two
versions concurrently, such as workloads that require exclusive access to a shared resource
or that use an on-disk format that is incompatible between versions.

The deletion always removes every Pod together, regardless of the
[Pod Management Policy](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/#pod-management-policies). Once all Pods have terminated, the new
Pods are created according to that policy: with `OrderedReady` (the default) the Pods are
recreated one at a time, in ascending ordinal order, waiting for each to become Running and
Ready before creating the next; with `Parallel` all of the Pods are recreated at once.

Because this is an alpha feature, you must enable the `StatefulSetRecreateStrategy`
[feature gate](https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/#StatefulSetRecreateStrategy)
on the kube-controller-manager and the kube-apiserver to use this strategy.