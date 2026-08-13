---
id: kubernetes-cloud-controller-manager-8c98aece
type: concept
title: Cloud Controller Manager
description: 'FEATURE STATE:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/architecture/cloud-controller/
updated_at: '2026-08-13'
created_at: '2026-08-13'
---

# Cloud Controller Manager

FEATURE STATE:
`Kubernetes v1.11 [beta]`

Cloud infrastructure technologies let you run Kubernetes on public, private, and hybrid clouds.
Kubernetes believes in automated, API-driven infrastructure without tight coupling between
components.

The cloud-controller-manager is a Kubernetes [control plane](https://kubernetes.io/docs/reference/glossary/?all=true#term-control-plane "The container orchestration layer that exposes the API and interfaces to define, deploy, and manage the lifecycle of containers.") component
that embeds cloud-specific control logic. The cloud controller manager lets you link your
cluster into your cloud provider's API, and separates out the components that interact
with that cloud platform from components that only interact with your cluster.

By decoupling the interoperability logic between Kubernetes and the underlying cloud
infrastructure, the cloud-controller-manager component enables cloud providers to release
features at a different pace compared to the main Kubernetes project.

The cloud-controller-manager is structured using a plugin
mechanism that allows different cloud providers to integrate their platforms with Kubernetes.