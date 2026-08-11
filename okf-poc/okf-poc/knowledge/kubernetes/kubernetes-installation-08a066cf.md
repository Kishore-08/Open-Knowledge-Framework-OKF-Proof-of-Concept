---
id: kubernetes-installation-08a066cf
type: concept
title: Installation
description: A Container Runtime, in the networking context, is a daemon on a node
  configured to provide CRI
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/extend-kubernetes/compute-storage-net/network-plugins/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

## Installation

A Container Runtime, in the networking context, is a daemon on a node configured to provide CRI
Services for kubelet. In particular, the Container Runtime must be configured to load the CNI
plugins required to implement the Kubernetes network model.

#### Note:

Prior to Kubernetes 1.24, the CNI plugins could also be managed by the kubelet using the
`cni-bin-dir` and `network-plugin` command-line parameters.
These command-line parameters were removed in Kubernetes 1.24, with management of the CNI no
longer in scope for kubelet.

See [Troubleshooting CNI plugin-related errors](https://kubernetes.io/docs/tasks/administer-cluster/migrating-from-dockershim/troubleshooting-cni-plugin-related-errors/)
if you are facing issues following the removal of dockershim.

For specific information about how a Container Runtime manages the CNI plugins, see the
documentation for that Container Runtime, for example:

- [containerd](https://github.com/containerd/containerd/blob/main/script/setup/install-cni)
- [CRI-O](https://github.com/cri-o/cri-o/blob/main/contrib/cni/README.md)

For specific information about how to install and manage a CNI plugin, see the documentation for
that plugin or [networking provider](https://kubernetes.io/docs/concepts/cluster-administration/networking/#how-to-implement-the-kubernetes-network-model).

## Network Plugin Requirements