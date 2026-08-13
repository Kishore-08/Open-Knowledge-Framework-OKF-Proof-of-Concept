---
id: kubernetes-topology-information-778be919
type: concept
title: Topology information
description: Each endpoint within an EndpointSlice can contain relevant topology information.
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/services-networking/endpoint-slices/
updated_at: '2026-08-13'
created_at: '2026-08-13'
---

### Topology information

Each endpoint within an EndpointSlice can contain relevant topology information.
The topology information includes the location of the endpoint and information
about the corresponding Node and zone. These are available in the following
per endpoint fields on EndpointSlices:

- `nodeName` - The name of the Node this endpoint is on.
- `zone` - The zone this endpoint is in.