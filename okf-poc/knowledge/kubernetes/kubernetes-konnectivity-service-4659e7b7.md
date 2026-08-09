---
id: kubernetes-konnectivity-service-4659e7b7
type: concept
title: Konnectivity service
description: 'FEATURE STATE:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/architecture/control-plane-node-communication/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Konnectivity service

FEATURE STATE:
`Kubernetes v1.18 [beta]`

As a replacement to the SSH tunnels, the Konnectivity service provides TCP level proxy for the
control plane to cluster communication. The Konnectivity service consists of two parts: the
Konnectivity server in the control plane network and the Konnectivity agents in the nodes network.
The Konnectivity agents initiate connections to the Konnectivity server and maintain the network
connections.
After enabling the Konnectivity service, all control plane to nodes traffic goes through these
connections.

Follow the [Konnectivity service task](https://kubernetes.io/docs/tasks/extend-kubernetes/setup-konnectivity/) to set
up the Konnectivity service in your cluster.