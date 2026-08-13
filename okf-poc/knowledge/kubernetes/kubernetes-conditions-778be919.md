---
id: kubernetes-conditions-778be919
type: concept
title: Conditions
description: The EndpointSlice API stores conditions about endpoints that may be useful
  for consumers.
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/services-networking/endpoint-slices/
updated_at: '2026-08-13'
created_at: '2026-08-13'
---

### Conditions

The EndpointSlice API stores conditions about endpoints that may be useful for consumers.
The three conditions are `serving`, `terminating`, and `ready`.

#### Serving

FEATURE STATE:
`Kubernetes v1.26 [stable]`

The `serving` condition indicates that the endpoint is currently serving responses, and
so it should be used as a target for Service traffic. For endpoints backed by a Pod, this
maps to the Pod's `Ready` condition.

#### Terminating

FEATURE STATE:
`Kubernetes v1.26 [stable]`

The `terminating` condition indicates that the endpoint is
terminating. For endpoints backed by a Pod, this condition is set when
the Pod is first deleted (that is, when it receives a deletion
timestamp, but most likely before the Pod's containers exit).

Service proxies will normally ignore endpoints that are `terminating`,
but they may route traffic to endpoints that are both `serving` and
`terminating` if all available endpoints are `terminating`. (This
helps to ensure that no Service traffic is lost during rolling updates
of the underlying Pods.)

#### Ready

The `ready` condition is essentially a shortcut for checking
"`serving` and not `terminating`" (though it will also always be
`true` for Services with `spec.publishNotReadyAddresses` set to
`true`).