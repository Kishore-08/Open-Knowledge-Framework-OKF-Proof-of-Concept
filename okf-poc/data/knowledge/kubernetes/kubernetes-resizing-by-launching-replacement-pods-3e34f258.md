---
id: kubernetes-resizing-by-launching-replacement-pods-3e34f258
type: concept
title: Resizing by launching replacement Pods
description: The more cloud native approach to changing a Pod's resources is through
  the
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Resizing by launching replacement Pods

The more cloud native approach to changing a Pod's resources is through the
workload resource that manages it (such as a Deployment or StatefulSet).
When you update the resource specifications in the Pod template,
the workload's controller creates new Pods with the updated resources and terminates
the old Pods according to its update strategy.

This approach:

- Works with any Kubernetes version.
- Can change any Pod specification, not just resources.
- Results in Pod replacement, so you should design your workload to handle
  [planned disruptions](https://kubernetes.io/docs/concepts/workloads/pods/disruptions/). Consider using a
  [PodDisruptionBudget](https://kubernetes.io/docs/tasks/run-application/configure-pdb/) to control availability.
- Requires that your Pods are managed by a workload resource.

You can also use a
[VerticalPodAutoscaler](https://kubernetes.io/docs/concepts/workloads/autoscaling/vertical-pod-autoscale/)
to automatically manage Pod resource recommendations and updates.