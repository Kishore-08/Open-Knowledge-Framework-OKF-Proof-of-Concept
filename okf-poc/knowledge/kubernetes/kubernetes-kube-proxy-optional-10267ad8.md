---
id: kubernetes-kube-proxy-optional-10267ad8
type: concept
title: kube-proxy (optional)
description: kube-proxy is a network proxy that runs on each
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/architecture/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### kube-proxy (optional)

kube-proxy is a network proxy that runs on each
[node](https://kubernetes.io/docs/concepts/architecture/nodes/ "A node is a worker machine in Kubernetes.") in your cluster,
implementing part of the Kubernetes
[Service](https://kubernetes.io/docs/concepts/services-networking/service/ "A way to expose an application running on a set of Pods as a network service.") concept.

[kube-proxy](https://kubernetes.io/docs/reference/command-line-tools-reference/kube-proxy/)
maintains network rules on nodes. These network rules allow network
communication to your Pods from network sessions inside or outside of
your cluster.

kube-proxy uses the operating system packet filtering layer if there is one
and it's available. Otherwise, kube-proxy forwards the traffic itself.

If you use a [network plugin](https://kubernetes.io/docs/concepts/architecture/#network-plugins) that implements packet forwarding for Services
by itself, and providing equivalent behavior to kube-proxy, then you do not need to run
kube-proxy on the nodes in your cluster.