---
id: kubernetes-cluster-architecture-10267ad8
type: concept
title: Cluster Architecture
description: The architectural concepts behind Kubernetes.
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/architecture/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

# Cluster Architecture

The architectural concepts behind Kubernetes.

A Kubernetes cluster consists of a control plane plus a set of worker machines, called nodes,
that run containerized applications. Every cluster needs at least one worker node in order to run Pods.

The worker node(s) host the Pods that are the components of the application workload.
The control plane manages the worker nodes and the Pods in the cluster. In production
environments, the control plane usually runs across multiple computers and a cluster
usually runs multiple nodes, providing fault-tolerance and high availability.

This document outlines the various components you need to have for a complete and working Kubernetes cluster.

![The control plane (kube-apiserver, etcd, kube-controller-manager, kube-scheduler) and several nodes. Each node is running a kubelet and kube-proxy.](https://kubernetes.io/images/docs/kubernetes-cluster-architecture.svg)

Figure 1. Kubernetes cluster components.

About this architecture

The diagram in Figure 1 presents an example reference architecture for a Kubernetes cluster.
The actual distribution of components can vary based on specific cluster setups and requirements.

In the diagram, each node runs the [`kube-proxy`](https://kubernetes.io/docs/concepts/architecture/#kube-proxy) component. You need a
network proxy component on each node to ensure that the
[Service](https://kubernetes.io/docs/concepts/services-networking/service/ "A way to expose an application running on a set of Pods as a network service.") API and associated behaviors
are available on your cluster network. However, some network plugins provide their own,
third party implementation of proxying. When you use that kind of network plugin,
the node does not need to run `kube-proxy`.