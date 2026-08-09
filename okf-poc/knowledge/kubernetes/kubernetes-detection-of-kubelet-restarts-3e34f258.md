---
id: kubernetes-detection-of-kubelet-restarts-3e34f258
type: concept
title: Detection of kubelet restarts
description: 'FEATURE STATE:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Detection of kubelet restarts

FEATURE STATE:
`Kubernetes v1.35 [deprecated]`(disabled by default)

When the kubelet starts, it checks to see if there is already a Node with bound Pods.
If the Node's [`Ready` condition](https://kubernetes.io/docs/reference/node/node-status/#condition) remains unchanged,
in other words the condition has not transitioned from true to false, Kubernetes detects this a *kubelet restart*.
(It's possible to restart the kubelet in other ways, for example to fix a node bug,
but in these cases, Kubernetes picks the safe option and treats this as if you
stopped the kubelet and then later started it).

When the kubelet restarts, the container statuses are managed differently based on the feature gate setting:

- By default, the kubelet does not change container statuses after a restart.
  Containers that were in set to `ready: true` state remain remain ready.

  If you stop the kubelet long enough for it to fail a series of
  [node heartbeat](https://kubernetes.io/docs/concepts/architecture/leases/#node-heart-beats) checks,
  and then you wait before you start the kubelet again, Kubernetes may begin to evict Pods from that Node.
  However, even though Pod evictions begin to happen, Kubernetes does not mark the
  individual containers in those Pods as `ready: false`. The Pod-level eviction
  happens after the control plane taints the node as `node.kubernetes.io/not-ready` (due to the failed heartbeats).
- In Kubernetes 1.36 you can opt in to a legacy behavior where the kubelet always modify
  the containers `ready` value, after a kubelet restart, to be false.

  This legacy behavior was the default for a long time, but caused issue for people using Kubernetes,
  especially in large scale deployments. Although the feature gate allows reverting to this legacy
  behavior temporarily, the Kubernetes project recommends that you file a bug report if you encounter problems.
  The `ChangeContainerStatusOnKubeletRestart`
  [feature gate](https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/#ChangeContainerStatusOnKubeletRestart)
  will be removed in the future.