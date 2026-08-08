---
id: kubernetes-communication-between-nodes-and-the-control-plane-4659e7b7
type: concept
title: Communication between Nodes and the Control Plane
description: This document catalogs the communication paths between the [API server](https://kubernetes.io/docs/concepts/architecture/#kube-apiserver
  "Control plane component that serves the Kubernetes API.")
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/architecture/control-plane-node-communication/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

# Communication between Nodes and the Control Plane

This document catalogs the communication paths between the [API server](https://kubernetes.io/docs/concepts/architecture/#kube-apiserver "Control plane component that serves the Kubernetes API.")
and the Kubernetes [cluster](https://kubernetes.io/docs/reference/glossary/?all=true#term-cluster "A set of worker machines, called nodes, that run containerized applications. Every cluster has at least one worker node.").
The intent is to allow users to customize their installation to harden the network configuration
such that the cluster can be run on an untrusted network (or on fully public IPs on a cloud
provider).