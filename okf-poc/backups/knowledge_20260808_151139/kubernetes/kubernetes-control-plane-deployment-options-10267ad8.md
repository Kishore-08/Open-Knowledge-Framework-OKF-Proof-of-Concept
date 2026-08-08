---
id: kubernetes-control-plane-deployment-options-10267ad8
type: concept
title: Control plane deployment options
description: 'The control plane components can be deployed in several ways:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/architecture/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Control plane deployment options

The control plane components can be deployed in several ways:

Traditional deployment
:   Control plane components run directly on dedicated machines or VMs, often managed as systemd services.

Static Pods
:   Control plane components are deployed as static Pods, managed by the kubelet on specific nodes.
    This is a common approach used by tools like kubeadm.

Self-hosted
:   The control plane runs as Pods within the Kubernetes cluster itself, managed by Deployments
    and StatefulSets or other Kubernetes primitives.

Managed Kubernetes services
:   Cloud providers often abstract away the control plane, managing its components as part of their service offering.