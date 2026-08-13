---
id: kubernetes-endpointslices-778be919
type: concept
title: EndpointSlices
description: The EndpointSlice API is the mechanism that Kubernetes uses to let your
  Service scale to handle large numbers of backends, and allows the cluster to update
  its list of healthy backends efficiently.
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/services-networking/endpoint-slices/
updated_at: '2026-08-13'
created_at: '2026-08-13'
---

# EndpointSlices

The EndpointSlice API is the mechanism that Kubernetes uses to let your Service scale to handle large numbers of backends, and allows the cluster to update its list of healthy backends efficiently.

FEATURE STATE:
`Kubernetes v1.21 [stable]`

EndpointSlices track the IP addresses of backend endpoints.
EndpointSlices are normally associated with a
[Service](https://kubernetes.io/docs/concepts/services-networking/service/ "A way to expose an application running on a set of Pods as a network service.") and the backend endpoints typically represent
[Pods](https://kubernetes.io/docs/concepts/workloads/pods/ "A Pod represents a set of running containers in your cluster.").