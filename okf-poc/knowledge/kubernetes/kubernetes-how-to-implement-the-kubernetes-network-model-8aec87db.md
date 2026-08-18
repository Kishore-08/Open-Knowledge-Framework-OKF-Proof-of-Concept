---
id: kubernetes-how-to-implement-the-kubernetes-network-model-8aec87db
type: concept
title: How to implement the Kubernetes network model
description: The network model is implemented by the container runtime on each node.
  The most common container
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/cluster-administration/networking/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

## How to implement the Kubernetes network model

The network model is implemented by the container runtime on each node. The most common container
runtimes use [Container Network Interface](https://github.com/containernetworking/cni) (CNI)
plugins to manage their network and security capabilities. Many different CNI plugins exist from
many different vendors. Some of these provide only basic features of adding and removing network
interfaces, while others provide more sophisticated solutions, such as integration with other
container orchestration systems, running multiple CNI plugins, advanced IPAM features etc.

See [this page](https://kubernetes.io/docs/concepts/cluster-administration/addons/#networking-and-network-policy)
for a non-exhaustive list of networking addons supported by Kubernetes.