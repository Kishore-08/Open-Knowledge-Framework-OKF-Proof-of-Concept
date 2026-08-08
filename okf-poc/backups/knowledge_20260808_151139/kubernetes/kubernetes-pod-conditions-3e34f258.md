---
id: kubernetes-pod-conditions-3e34f258
type: concept
title: Pod conditions
description: A Pod has a PodStatus, which has an array of
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

## Pod conditions

A Pod has a PodStatus, which has an array of
[PodConditions](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.36/#podcondition-v1-core)
through which the Pod has or has not passed. The kubelet manages the following
PodConditions:

- `PodScheduled`: the Pod has been scheduled to a node.
- `PodReadyToStartContainers`: (beta feature; enabled by [default](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#pod-ready-to-start-containers)) the
  Pod sandbox has been successfully created, networking configured, storage volumes mounted,
  and any dynamic resources (if requested) allocated.
- `ContainersReady`: all containers in the Pod are ready.
- `Initialized`: all [init containers](https://kubernetes.io/docs/concepts/workloads/pods/init-containers/)
  have completed successfully.
- `Ready`: the Pod is able to serve requests and should be added to the load
  balancing pools of all matching Services.
- `DisruptionTarget`: the pod is about to be terminated due to a disruption (such as preemption, eviction or garbage-collection).
- `PodResizePending`: a pod resize was requested but cannot be applied. See [Pod resize status](https://kubernetes.io/docs/tasks/configure-pod-container/resize-container-resources/#pod-resize-status).
- `PodResizeInProgress`: the pod is in the process of resizing. See
  [Pod resize status](https://kubernetes.io/docs/tasks/configure-pod-container/resize-container-resources/#pod-resize-status).

| Field name | Description |
| --- | --- |
| `type` | Name of this Pod condition. |
| `status` | Indicates whether that condition is applicable, with possible values "`True`", "`False`", or "`Unknown`". |
| `lastProbeTime` | Timestamp of when the Pod condition was last probed. |
| `lastTransitionTime` | Timestamp for when the Pod last transitioned from one status to another. |
| `reason` | Machine-readable, UpperCamelCase text indicating the reason for the condition's last transition. |
| `message` | Human-readable message indicating details about the last status transition. |