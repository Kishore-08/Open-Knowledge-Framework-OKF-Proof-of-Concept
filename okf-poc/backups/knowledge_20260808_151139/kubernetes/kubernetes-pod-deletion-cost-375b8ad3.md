---
id: kubernetes-pod-deletion-cost-375b8ad3
type: concept
title: Pod deletion cost
description: 'FEATURE STATE:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/controllers/replicaset/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Pod deletion cost

FEATURE STATE:
`Kubernetes v1.22 [beta]`

Using the [`controller.kubernetes.io/pod-deletion-cost`](https://kubernetes.io/docs/reference/labels-annotations-taints/#pod-deletion-cost)
annotation, users can set a preference regarding which pods to remove first when downscaling a ReplicaSet.

The annotation should be set on the pod, the range is [-2147483648, 2147483647]. It represents the cost of
deleting a pod compared to other pods belonging to the same ReplicaSet. Pods with lower deletion
cost are preferred to be deleted before pods with higher deletion cost.

The implicit value for this annotation for pods that don't set it is 0; negative values are permitted.
Invalid values will be rejected by the API server.

This feature is beta and enabled by default. You can disable it using the
[feature gate](https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/)
`PodDeletionCost` in both kube-apiserver and kube-controller-manager.

#### Note:

- This is honored on a best-effort basis, so it does not offer any guarantees on pod deletion order.
- Users should avoid updating the annotation frequently, such as updating it based on a metric value,
  because doing so will generate a significant number of pod updates on the apiserver.

#### Example Use Case

The different pods of an application could have different utilization levels. On scale down, the application
may prefer to remove the pods with lower utilization. To avoid frequently updating the pods, the application
should update `controller.kubernetes.io/pod-deletion-cost` once before issuing a scale down (setting the
annotation to a value proportional to pod utilization level). This works if the application itself controls
the down scaling; for example, the driver pod of a Spark deployment.