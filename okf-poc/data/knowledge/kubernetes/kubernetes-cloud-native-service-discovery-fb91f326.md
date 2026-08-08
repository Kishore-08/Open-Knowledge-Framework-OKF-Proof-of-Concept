---
id: kubernetes-cloud-native-service-discovery-fb91f326
type: concept
title: Cloud-native service discovery
description: If you're able to use Kubernetes APIs for service discovery in your application,
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/services-networking/service/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Cloud-native service discovery

If you're able to use Kubernetes APIs for service discovery in your application,
you can query the [API server](https://kubernetes.io/docs/concepts/architecture/#kube-apiserver "Control plane component that serves the Kubernetes API.")
for matching EndpointSlices. Kubernetes updates the EndpointSlices for a Service
whenever the set of Pods in a Service changes.

For non-native applications, Kubernetes offers ways to place a network port or load
balancer in between your application and the backend Pods.

Either way, your workload can use these [service discovery](https://kubernetes.io/docs/concepts/services-networking/service/#discovering-services)
mechanisms to find the target it wants to connect to.