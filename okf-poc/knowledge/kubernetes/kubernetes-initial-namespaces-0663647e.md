---
id: kubernetes-initial-namespaces-0663647e
type: concept
title: Initial namespaces
description: 'Kubernetes starts with four initial namespaces:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

## Initial namespaces

Kubernetes starts with four initial namespaces:

`default`
:   Kubernetes includes this namespace so that you can start using your new cluster without first creating a namespace.

`kube-node-lease`
:   This namespace holds [Lease](https://kubernetes.io/docs/concepts/architecture/leases/) objects associated with each node. Node leases allow the kubelet to send [heartbeats](https://kubernetes.io/docs/concepts/architecture/nodes/#node-heartbeats) so that the control plane can detect node failure.

`kube-public`
:   This namespace is readable by *all* clients (including those not authenticated). This namespace is mostly reserved for cluster usage, in case that some resources should be visible and readable publicly throughout the whole cluster. The public aspect of this namespace is only a convention, not a requirement.

`kube-system`
:   The namespace for objects created by the Kubernetes system.