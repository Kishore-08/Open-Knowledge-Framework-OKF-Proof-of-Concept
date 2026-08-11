---
id: kubernetes-loopback-cni-08a066cf
type: concept
title: Loopback CNI
description: In addition to the CNI plugin installed on the nodes for implementing
  the Kubernetes network
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/extend-kubernetes/compute-storage-net/network-plugins/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Loopback CNI

In addition to the CNI plugin installed on the nodes for implementing the Kubernetes network
model, Kubernetes also requires the container runtimes to provide a loopback interface `lo`, which
is used for each sandbox (pod sandboxes, vm sandboxes, ...).
Implementing the loopback interface can be accomplished by re-using the
[CNI loopback plugin.](https://github.com/containernetworking/plugins/blob/master/plugins/main/loopback/loopback.go)
or by developing your own code to achieve this (see
[this example from CRI-O](https://github.com/cri-o/ocicni/blob/release-1.24/pkg/ocicni/util_linux.go#L91)).