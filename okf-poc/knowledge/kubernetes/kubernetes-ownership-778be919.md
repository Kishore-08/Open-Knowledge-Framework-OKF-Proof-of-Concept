---
id: kubernetes-ownership-778be919
type: concept
title: Ownership
description: In most use cases, EndpointSlices are owned by the Service that the endpoint
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/services-networking/endpoint-slices/
updated_at: '2026-08-13'
created_at: '2026-08-13'
---

### Ownership

In most use cases, EndpointSlices are owned by the Service that the endpoint
slice object tracks endpoints for. This ownership is indicated by an owner
reference on each EndpointSlice as well as a `kubernetes.io/service-name`
label that enables simple lookups of all EndpointSlices belonging to a Service.