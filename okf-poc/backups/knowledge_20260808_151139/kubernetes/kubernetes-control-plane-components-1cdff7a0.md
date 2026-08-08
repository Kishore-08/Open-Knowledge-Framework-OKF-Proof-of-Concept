---
id: kubernetes-control-plane-components-1cdff7a0
type: concept
title: Control Plane Components
description: 'Manage the overall state of the cluster:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/overview/components/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Control Plane Components

Manage the overall state of the cluster:

[kube-apiserver](https://kubernetes.io/docs/concepts/architecture/#kube-apiserver)
:   The core component server that exposes the Kubernetes HTTP API.

[etcd](https://kubernetes.io/docs/concepts/architecture/#etcd)
:   Consistent and highly-available key value store for all API server data.

[kube-scheduler](https://kubernetes.io/docs/concepts/architecture/#kube-scheduler)
:   Looks for Pods not yet bound to a node, and assigns each Pod to a suitable node.

[kube-controller-manager](https://kubernetes.io/docs/concepts/architecture/#kube-controller-manager)
:   Runs [controllers](https://kubernetes.io/docs/concepts/architecture/controller/ "A control loop that watches the shared state of the cluster through the apiserver and makes changes attempting to move the current state towards the desired state.") to implement Kubernetes API behavior.

[cloud-controller-manager](https://kubernetes.io/docs/concepts/architecture/#cloud-controller-manager) (optional)
:   Integrates with underlying cloud provider(s).