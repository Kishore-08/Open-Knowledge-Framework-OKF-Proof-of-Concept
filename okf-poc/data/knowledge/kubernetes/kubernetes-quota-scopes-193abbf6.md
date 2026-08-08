---
id: kubernetes-quota-scopes-193abbf6
type: concept
title: Quota scopes
description: Each quota can have an associated set of `scopes`. A quota will only
  measure usage for a resource if it matches
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/policy/resource-quotas/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

## Quota scopes

Each quota can have an associated set of `scopes`. A quota will only measure usage for a resource if it matches
the intersection of enumerated scopes.

When a scope is added to the quota, it limits the number of resources it supports to those that pertain to the scope.
Resources specified on the quota outside of the allowed set results in a validation error.

Kubernetes 1.36 supports the following scopes:

| Scope | Description |
| --- | --- |
| [`BestEffort`](https://kubernetes.io/docs/concepts/policy/resource-quotas/#quota-scope-best-effort) | Match pods that have best effort quality of service. |
| [`CrossNamespacePodAffinity`](https://kubernetes.io/docs/concepts/policy/resource-quotas/#cross-namespace-pod-affinity-scope) | Match pods that have cross-namespace pod [(anti)affinity terms](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/). |
| [`NotBestEffort`](https://kubernetes.io/docs/concepts/policy/resource-quotas/#quota-scope-non-best-effort) | Match pods that do not have best effort quality of service. |
| [`NotTerminating`](https://kubernetes.io/docs/concepts/policy/resource-quotas/#quota-scope-non-terminating) | Match pods where `.spec.activeDeadlineSeconds` is `nil` |
| [`PriorityClass`](https://kubernetes.io/docs/concepts/policy/resource-quotas/#resource-quota-per-priorityclass) | Match pods that references the specified [priority class](https://kubernetes.io/docs/concepts/scheduling-eviction/pod-priority-preemption/). |
| [`Terminating`](https://kubernetes.io/docs/concepts/policy/resource-quotas/#quota-scope-terminating) | Match pods where `.spec.activeDeadlineSeconds` >= `0` |
| [`VolumeAttributesClass`](https://kubernetes.io/docs/concepts/policy/resource-quotas/#quota-scope-volume-attributes-class) | Match PersistentVolumeClaims that reference the specified [volume attributes class](https://kubernetes.io/docs/concepts/storage/volume-attributes-classes/). |

ResourceQuotas with a scope set can also have a optional `scopeSelector` field. You define one or more *match expressions*
that specify an `operators` and, if relevant, a set of `values` to match. For example:

```
  scopeSelector:
    matchExpressions:
      - scopeName: BestEffort # Match pods that have best effort quality of service
        operator: Exists # optional; "Exists" is implied for BestEffort scope
```

The `scopeSelector` supports the following values in the `operator` field:

- `In`
- `NotIn`
- `Exists`
- `DoesNotExist`

If the `operator` is `In` or `NotIn`, the `values` field must have at least
one value. For example:

```
  scopeSelector:
    matchExpressions:
      - scopeName: PriorityClass
        operator: In
        values:
          - middle
```

If the `operator` is `Exists` or `DoesNotExist`, the `values` field must *NOT* be
specified.