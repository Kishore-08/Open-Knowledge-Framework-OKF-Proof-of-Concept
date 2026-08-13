---
id: kubernetes-duplicate-endpoints-778be919
type: concept
title: Duplicate endpoints
description: Due to the nature of EndpointSlice changes, endpoints may be represented
  in more
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/services-networking/endpoint-slices/
updated_at: '2026-08-13'
created_at: '2026-08-13'
---

### Duplicate endpoints

Due to the nature of EndpointSlice changes, endpoints may be represented in more
than one EndpointSlice at the same time. This naturally occurs as changes to
different EndpointSlice objects can arrive at the Kubernetes client watch / cache
at different times.

#### Note:

Clients of the EndpointSlice API must iterate through all the existing EndpointSlices
associated to a Service and build a complete list of unique network endpoints. It is
important to mention that endpoints may be duplicated in different EndpointSlices.

You can find a reference implementation for how to perform this endpoint aggregation
and deduplication as part of the `EndpointSliceCache` code within `kube-proxy`.