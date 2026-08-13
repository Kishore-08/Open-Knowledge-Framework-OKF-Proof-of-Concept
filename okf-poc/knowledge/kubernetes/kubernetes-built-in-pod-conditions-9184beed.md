---
id: kubernetes-built-in-pod-conditions-9184beed
type: concept
title: Built-in Pod conditions
description: 'Kubernetes manages the following Pod conditions:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/pods/pod-condition/
updated_at: '2026-08-13'
created_at: '2026-08-13'
---

## Built-in Pod conditions

Kubernetes manages the following Pod conditions:

[Lifecycle conditions](https://kubernetes.io/docs/concepts/workloads/pods/pod-condition/#lifecycle-pod-conditions): set as a Pod progresses through its lifecycle, roughly in this order:
`PodScheduled`, `PodReadyToStartContainers`, `Initialized`, `ContainersReady`, `Ready`.

[Other conditions](https://kubernetes.io/docs/concepts/workloads/pods/pod-condition/#other-pod-conditions): set in response to specific operations or events:
`DisruptionTarget`, `PodResizePending`, `PodResizeInProgress`.

In addition to the built-in conditions above, you can define custom conditions
using [Pod readiness gates](https://kubernetes.io/docs/concepts/workloads/pods/pod-condition/#enhanced-pod-readiness).