---
id: kubernetes-control-plane-to-node-4659e7b7
type: concept
title: Control plane to node
description: There are two primary communication paths from the control plane (the
  API server) to the nodes.
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/architecture/control-plane-node-communication/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

## Control plane to node

There are two primary communication paths from the control plane (the API server) to the nodes.
The first is from the API server to the [kubelet](https://kubernetes.io/docs/reference/command-line-tools-reference/kubelet "An agent that runs on each node in the cluster. It makes sure that containers are running in a pod.") process which runs on each node in the cluster.
The second is from the API server to any node, pod, or service through the API server's *proxy*
functionality.