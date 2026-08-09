---
id: kubernetes-graceful-node-shutdown-e5a13667
type: concept
title: Graceful node shutdown
description: The kubelet attempts to detect node system shutdown and terminates pods
  running on the node.
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/cluster-administration/node-shutdown/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

## Graceful node shutdown

The kubelet attempts to detect node system shutdown and terminates pods running on the node.

Kubelet ensures that pods follow the normal
[pod termination process](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#pod-termination)
during the node shutdown. During node shutdown, the kubelet does not accept new
Pods (even if those Pods are already bound to the node).