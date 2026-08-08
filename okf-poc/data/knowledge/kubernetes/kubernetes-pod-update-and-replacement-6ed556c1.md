---
id: kubernetes-pod-update-and-replacement-6ed556c1
type: concept
title: Pod update and replacement
description: As mentioned in the previous section, when the Pod template for a workload
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/pods/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

## Pod update and replacement

As mentioned in the previous section, when the Pod template for a workload
resource is changed, the controller creates new Pods based on the updated
template instead of updating or patching the existing Pods.

Kubernetes doesn't prevent you from managing Pods directly. It is possible to
update some fields of a running Pod, in place. However, Pod update operations
like
[`patch`](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.36/#patch-pod-v1-core), and
[`replace`](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.36/#replace-pod-v1-core)
have some limitations:

- Most of the metadata about a Pod is immutable. For example, you cannot
  change the `namespace`, `name`, `uid`, or `creationTimestamp` fields.
- If the `metadata.deletionTimestamp` is set, no new entry can be added to the
  `metadata.finalizers` list.
- Pod updates may not change fields other than `spec.containers[*].image`,
  `spec.initContainers[*].image`, `spec.activeDeadlineSeconds`, `spec.terminationGracePeriodSeconds`,
  `spec.tolerations` or `spec.schedulingGates`. For `spec.tolerations`, you can only add new entries.
- When updating the `spec.activeDeadlineSeconds` field, two types of updates
  are allowed:

  1. setting the unassigned field to a positive number;
  2. updating the field from a positive number to a smaller, non-negative
     number.