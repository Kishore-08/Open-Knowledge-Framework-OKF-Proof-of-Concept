---
id: kubernetes-endpointslices-fb91f326
type: concept
title: EndpointSlices
description: 'FEATURE STATE:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/services-networking/service/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### EndpointSlices

FEATURE STATE:
`Kubernetes v1.21 [stable]`

[EndpointSlices](https://kubernetes.io/docs/concepts/services-networking/endpoint-slices/) are objects that
represent a subset (a *slice*) of the backing network endpoints for a Service.

Your Kubernetes cluster tracks how many endpoints each EndpointSlice represents.
If there are so many endpoints for a Service that a threshold is reached, then
Kubernetes adds another empty EndpointSlice and stores new endpoint information
there.
By default, Kubernetes makes a new EndpointSlice once the existing EndpointSlices
all contain at least 100 endpoints. Kubernetes does not make the new EndpointSlice
until an extra endpoint needs to be added.

See [EndpointSlices](https://kubernetes.io/docs/concepts/services-networking/endpoint-slices/) for more
information about this API.