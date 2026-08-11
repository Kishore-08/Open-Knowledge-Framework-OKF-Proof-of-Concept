---
id: kubernetes-swap-behaviors-9edb5061
type: concept
title: Swap behaviors
description: You need to pick a [swap behavior](https://kubernetes.io/docs/reference/node/swap-behavior/)
  to
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/cluster-administration/swap-memory-management/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Swap behaviors

You need to pick a [swap behavior](https://kubernetes.io/docs/reference/node/swap-behavior/) to
use. Different nodes in your cluster can use different swap behaviors.

The swap behaviors you can choose for Linux nodes are:

`NoSwap` (default)
:   Workloads running as Pods on this node do not and cannot use swap.

`LimitedSwap`
:   Kubernetes workloads can utilize swap memory.

#### Note:

If you choose the NoSwap behavior, and you configure the kubelet to tolerate
swap space (`failSwapOn: false`), then your workloads don't use any swap.

However, processes outside of Kubernetes-managed containers, such as systemd
services (and even the kubelet itself!) **can** utilize swap.

You can read [configuring swap memory on Kubernetes nodes](https://kubernetes.io/docs/tutorials/cluster-management/provision-swap-memory/) to learn about enabling swap for your cluster.