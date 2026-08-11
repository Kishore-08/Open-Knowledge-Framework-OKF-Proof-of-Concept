---
id: kubernetes-swap-and-control-plane-nodes-9edb5061
type: concept
title: Swap and control plane nodes
description: The Kubernetes project recommends running control plane nodes without
  any swap space configured.
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/cluster-administration/swap-memory-management/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Swap and control plane nodes

The Kubernetes project recommends running control plane nodes without any swap space configured.
The control plane primarily hosts Guaranteed QoS Pods, so swap can generally be disabled.
The main concern is that swapping critical services on the control plane could negatively impact performance.