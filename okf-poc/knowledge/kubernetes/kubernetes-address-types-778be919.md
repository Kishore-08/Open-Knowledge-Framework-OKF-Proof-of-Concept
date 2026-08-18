---
id: kubernetes-address-types-778be919
type: concept
title: Address types
description: 'EndpointSlices support two address types:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/services-networking/endpoint-slices/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

### Address types

EndpointSlices support two address types:

- IPv4
- IPv6

Each `EndpointSlice` object represents a specific IP address type. If you have
a Service that is available via IPv4 and IPv6, there will be at least two
`EndpointSlice` objects (one for IPv4, and one for IPv6).