---
id: kubernetes-without-selectors-fb91f326
type: concept
title: Without selectors
description: For headless Services that do not define selectors, the control plane
  does
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/services-networking/service/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Without selectors

For headless Services that do not define selectors, the control plane does
not create EndpointSlice objects. However, the DNS system looks for and configures
either:

- DNS CNAME records for [`type: ExternalName`](https://kubernetes.io/docs/concepts/services-networking/service/#externalname) Services.
- DNS A / AAAA records for all IP addresses of the Service's ready endpoints,
  for all Service types other than `ExternalName`.
  - For IPv4 endpoints, the DNS system creates A records.
  - For IPv6 endpoints, the DNS system creates AAAA records.

When you define a headless Service without a selector, the `port` must
match the `targetPort`.

## Discovering services

For clients running inside your cluster, Kubernetes supports two primary modes of
finding a Service: environment variables and DNS.