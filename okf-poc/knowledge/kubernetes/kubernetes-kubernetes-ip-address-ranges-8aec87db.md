---
id: kubernetes-kubernetes-ip-address-ranges-8aec87db
type: concept
title: Kubernetes IP address ranges
description: Kubernetes clusters require to allocate non-overlapping IP addresses
  for Pods, Services and Nodes,
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/cluster-administration/networking/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

## Kubernetes IP address ranges

Kubernetes clusters require to allocate non-overlapping IP addresses for Pods, Services and Nodes,
from a range of available addresses configured in the following components:

- The network plugin is configured to assign IP addresses to Pods.
- The kube-apiserver is configured to assign IP addresses to Services.
- The kubelet or the cloud-controller-manager is configured to assign IP addresses to Nodes.

![A figure illustrating the different network ranges in a kubernetes cluster](https://kubernetes.io/docs/images/kubernetes-cluster-network.svg)