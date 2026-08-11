---
id: kubernetes-node-heartbeats-5445bee6
type: concept
title: Node heartbeats
description: Heartbeats, sent by Kubernetes nodes, help your cluster determine the
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/architecture/nodes/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

## Node heartbeats

Heartbeats, sent by Kubernetes nodes, help your cluster determine the
availability of each node, and to take action when failures are detected.

For nodes there are two forms of heartbeats:

- Updates to the [`.status`](https://kubernetes.io/docs/reference/node/node-status/) of a Node.
- [Lease](https://kubernetes.io/docs/concepts/architecture/leases/) objects
  within the `kube-node-lease`
  [namespace](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces "An abstraction used by Kubernetes to support isolation of groups of resources within a single cluster.").
  Each Node has an associated Lease object.