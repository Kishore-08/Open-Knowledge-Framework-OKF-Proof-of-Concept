---
id: kubernetes-kubelet-downgrades-and-state-checkpoints-0cecd4eb
type: concept
title: '`kubelet` downgrades and state checkpoints'
description: In Kubernetes 1.36, enabling `PodLevelResourceManagers` updated internal
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/resource-management/pod-level-resource-managers/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

### `kubelet` downgrades and state checkpoints

In Kubernetes 1.36, enabling `PodLevelResourceManagers` updated internal
`kubelet` state checkpoint files (`cpu_manager_state` and
`memory_manager_state`) to a format that older `kubelet` versions cannot
load. If you downgrade a 1.36 `kubelet` after active use, the older
`kubelet` fails to start; you must drain the Node, delete these checkpoint
files, and restart the `kubelet`.

In Kubernetes 1.37, checkpoint files use a forward-compatible format to
prevent start-up failures during downgrades, though 1.36 `kubelet`
versions do not restore active pod-level resource assignments. For
complete details on checkpoint formats and recovery, see the
[Pod-level resource managers reference](https://kubernetes.io/docs/reference/node/pod-level-resource-managers/#state-checkpoints).