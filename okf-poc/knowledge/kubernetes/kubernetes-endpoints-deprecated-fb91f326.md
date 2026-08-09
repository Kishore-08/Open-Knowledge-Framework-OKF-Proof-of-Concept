---
id: kubernetes-endpoints-deprecated-fb91f326
type: concept
title: Endpoints (deprecated)
description: 'FEATURE STATE:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/services-networking/service/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Endpoints (deprecated)

FEATURE STATE:
`Kubernetes v1.33 [deprecated]`

The EndpointSlice API is the evolution of the older
[Endpoints](https://kubernetes.io/docs/reference/kubernetes-api/service-resources/endpoints-v1/)
API. The deprecated Endpoints API has several problems relative to
EndpointSlice:

- It does not support dual-stack clusters.
- It does not contain information needed to support newer features, such as
  [trafficDistribution](https://kubernetes.io/docs/concepts/services-networking/service/#traffic-distribution).
- It will truncate the list of endpoints if it is too long to fit in a single object.

Because of this, it is recommended that all clients use the
EndpointSlice API rather than Endpoints.

#### Over-capacity endpoints

Kubernetes limits the number of endpoints that can fit in a single Endpoints
object. When there are over 1000 backing endpoints for a Service, Kubernetes
truncates the data in the Endpoints object. Because a Service can be linked
with more than one EndpointSlice, the 1000 backing endpoint limit only
affects the legacy Endpoints API.

In that case, Kubernetes selects at most 1000 possible backend endpoints to store
into the Endpoints object, and sets an
[annotation](https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations "A key-value pair that is used to attach arbitrary non-identifying metadata to objects.") on the Endpoints:
[`endpoints.kubernetes.io/over-capacity: truncated`](https://kubernetes.io/docs/reference/labels-annotations-taints/#endpoints-kubernetes-io-over-capacity).
The control plane also removes that annotation if the number of backend Pods drops below 1000.

Traffic is still sent to backends, but any load balancing mechanism that relies on the
legacy Endpoints API only sends traffic to at most 1000 of the available backing endpoints.

The same API limit means that you cannot manually update an Endpoints to have more than 1000 endpoints.