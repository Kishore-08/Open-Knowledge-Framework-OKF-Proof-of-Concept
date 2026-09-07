---
id: kubernetes-cluster-networking-types-8aec87db
type: concept
title: Cluster networking types
description: 'Kubernetes clusters, attending to the IP families configured, can be
  categorized into:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/cluster-administration/networking/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

## Cluster networking types

Kubernetes clusters, attending to the IP families configured, can be categorized into:

- IPv4 only: The network plugin, kube-apiserver and kubelet/cloud-controller-manager are configured to assign only IPv4 addresses.
- IPv6 only: The network plugin, kube-apiserver and kubelet/cloud-controller-manager are configured to assign only IPv6 addresses.
- IPv4/IPv6 or IPv6/IPv4 [dual-stack](https://kubernetes.io/docs/concepts/services-networking/dual-stack/):
  - The network plugin is configured to assign IPv4 and IPv6 addresses.
  - The kube-apiserver is configured to assign IPv4 and IPv6 addresses.
  - The kubelet or cloud-controller-manager is configured to assign IPv4 and IPv6 address.
  - All components must agree on the configured primary IP family.

Kubernetes clusters only consider the IP families present on the Pods, Services and Nodes objects,
independently of the existing IPs of the represented objects. For example, a server or a pod can have multiple
IP addresses assigned to its interfaces, but only the IP addresses in `node.status.addresses` or `pod.status.ips` are
considered when implementing the Kubernetes network model and defining the cluster type.