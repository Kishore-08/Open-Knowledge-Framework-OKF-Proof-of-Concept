---
id: kubernetes-podresizepending-and-podresizeinprogress-9184beed
type: concept
title: PodResizePending and PodResizeInProgress
description: 'The kubelet updates the Pod''s status conditions to indicate the state
  of a resize request:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/pods/pod-condition/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

### PodResizePending and PodResizeInProgress

The kubelet updates the Pod's status conditions to indicate the state of a resize request:

- `type: PodResizePending`: The kubelet cannot immediately grant the request. The `message` field provides an explanation of why.
  - `reason: Infeasible`: The requested resize is impossible on the current node (for example, requesting more resources than the node has).
  - `reason: Deferred`: The requested resize is currently not possible, but might become feasible later (for example if another pod is removed). The kubelet will retry the resize.
- `type: PodResizeInProgress`: The kubelet has accepted the resize and allocated resources, but the changes are still being applied. This is usually brief but might take longer depending on the resource type and runtime behavior. Any errors during actuation are reported in the `message` field (along with `reason: Error`).

If the requested resize is *Deferred*, the kubelet will periodically re-attempt the resize, for example when another pod is removed or scaled down.

For more details on Pod resize, see [Resize CPU and Memory Resources assigned to Containers](https://kubernetes.io/docs/tasks/configure-pod-container/resize-container-resources/).