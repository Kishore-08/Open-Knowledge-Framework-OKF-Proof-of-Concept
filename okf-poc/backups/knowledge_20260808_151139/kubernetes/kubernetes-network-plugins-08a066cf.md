---
id: kubernetes-network-plugins-08a066cf
type: concept
title: Network Plugins
description: Kubernetes (version 1.3 through to the latest 1.36, and likely onwards)
  lets you use
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/extend-kubernetes/compute-storage-net/network-plugins/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

# Network Plugins

Kubernetes (version 1.3 through to the latest 1.36, and likely onwards) lets you use
[Container Network Interface](https://github.com/containernetworking/cni)
(CNI) plugins for cluster networking. You must use a CNI plugin that is compatible with your
cluster and that suits your needs. Different plugins are available (both open- and closed- source)
in the wider Kubernetes ecosystem.

A CNI plugin is required to implement the
[Kubernetes network model](https://kubernetes.io/docs/concepts/services-networking/#the-kubernetes-network-model).

You must use a CNI plugin that is compatible with the
[v0.4.0](https://github.com/containernetworking/cni/blob/spec-v0.4.0/SPEC.md) or later
releases of the CNI specification. The Kubernetes project recommends using a plugin that is
compatible with the [v1.0.0](https://github.com/containernetworking/cni/blob/spec-v1.0.0/SPEC.md)
CNI specification (plugins can be compatible with multiple spec versions).