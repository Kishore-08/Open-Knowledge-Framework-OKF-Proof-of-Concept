---
id: kubernetes-how-does-it-work-9edb5061
type: concept
title: How does it work?
description: There are a number of possible ways that one could envision swap use
  on a node.
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/cluster-administration/swap-memory-management/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

## How does it work?

There are a number of possible ways that one could envision swap use on a node.
If kubelet is already running on a node, it would need to be restarted after swap is provisioned in order to identify it.

When kubelet starts on a node in which swap is provisioned and available
(with the `failSwapOn: false` configuration), kubelet will:

- Be able to start on this swap-enabled node.
- Direct the Container Runtime Interface (CRI) implementation, often referred to as the container runtime,
  to allocate zero swap memory to Kubernetes workloads by default.

Swap configuration on a node is exposed to a cluster admin via the
[`memorySwap` in the KubeletConfiguration](https://kubernetes.io/docs/reference/config-api/kubelet-config.v1/).
As a cluster administrator, you can specify the node's behaviour in the
presence of swap memory by setting `memorySwap.swapBehavior`.