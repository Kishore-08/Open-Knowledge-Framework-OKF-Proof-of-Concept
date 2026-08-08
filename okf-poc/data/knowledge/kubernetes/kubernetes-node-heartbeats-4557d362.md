---
id: kubernetes-node-heartbeats-4557d362
type: concept
title: Node heartbeats
description: Kubernetes uses the Lease API to communicate kubelet node heartbeats
  to the Kubernetes API server.
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/architecture/leases/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

## Node heartbeats

Kubernetes uses the Lease API to communicate kubelet node heartbeats to the Kubernetes API server.
For every `Node` , there is a `Lease` object with a matching name in the `kube-node-lease`
namespace. Under the hood, every kubelet heartbeat is an **update** request to this `Lease` object, updating
the `spec.renewTime` field for the Lease. The Kubernetes control plane uses the time stamp of this field
to determine the availability of this `Node`.

See [Node Lease objects](https://kubernetes.io/docs/concepts/architecture/nodes/#node-heartbeats) for more details.