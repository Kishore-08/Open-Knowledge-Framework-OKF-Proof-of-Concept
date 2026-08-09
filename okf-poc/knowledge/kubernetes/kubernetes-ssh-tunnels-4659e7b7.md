---
id: kubernetes-ssh-tunnels-4659e7b7
type: concept
title: SSH tunnels
description: Kubernetes supports [SSH tunnels](https://www.ssh.com/academy/ssh/tunneling)
  to protect the control plane to nodes communication paths. In this
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/architecture/control-plane-node-communication/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### SSH tunnels

Kubernetes supports [SSH tunnels](https://www.ssh.com/academy/ssh/tunneling) to protect the control plane to nodes communication paths. In this
configuration, the API server initiates an SSH tunnel to each node in the cluster (connecting to
the SSH server listening on port 22) and passes all traffic destined for a kubelet, node, pod, or
service through the tunnel.
This tunnel ensures that the traffic is not exposed outside of the network in which the nodes are
running.

#### Note:

SSH tunnels are currently deprecated, so you shouldn't opt to use them unless you know what you
are doing. The [Konnectivity service](https://kubernetes.io/docs/concepts/architecture/control-plane-node-communication/#konnectivity-service) is a replacement for this
communication channel.