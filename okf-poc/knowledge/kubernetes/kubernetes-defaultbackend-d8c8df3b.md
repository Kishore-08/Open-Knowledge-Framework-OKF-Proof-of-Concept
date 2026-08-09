---
id: kubernetes-defaultbackend-d8c8df3b
type: concept
title: DefaultBackend
description: An Ingress with no rules sends all traffic to a single default backend
  and `.spec.defaultBackend`
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/services-networking/ingress/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### DefaultBackend

An Ingress with no rules sends all traffic to a single default backend and `.spec.defaultBackend`
is the backend that should handle requests in that case.
The `defaultBackend` is conventionally a configuration option of the
[Ingress controller](https://kubernetes.io/docs/concepts/services-networking/ingress-controllers/) and
is not specified in your Ingress resources.
If no `.spec.rules` are specified, `.spec.defaultBackend` must be specified.
If `defaultBackend` is not set, the handling of requests that do not match any of the rules will be up to the
ingress controller (consult the documentation for your ingress controller to find out how it handles this case).

If none of the hosts or paths match the HTTP request in the Ingress objects, the traffic is
routed to your default backend.