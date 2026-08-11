---
id: kubernetes-ingress-d8c8df3b
type: concept
title: Ingress
description: Make your HTTP (or HTTPS) network service available using a protocol-aware
  configuration mechanism, that understands web concepts like URIs, hostnames, paths,
  and more. The Ingress concept lets you ma
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/services-networking/ingress/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

# Ingress

Make your HTTP (or HTTPS) network service available using a protocol-aware configuration mechanism, that understands web concepts like URIs, hostnames, paths, and more. The Ingress concept lets you map traffic to different backends based on rules you define via the Kubernetes API.

FEATURE STATE:
`Kubernetes v1.19 [stable]`

An API object that manages external access to the services in a cluster, typically HTTP.

Ingress may provide load balancing, SSL termination and name-based virtual hosting.

#### Note:

The Kubernetes project recommends using [Gateway](https://gateway-api.sigs.k8s.io/) instead of
[Ingress](https://kubernetes.io/docs/concepts/services-networking/ingress/).
The Ingress API has been frozen.

This means that:

- The Ingress API is generally available, and is subject to the [stability guarantees](https://kubernetes.io/docs/reference/using-api/deprecation-policy/#deprecating-parts-of-the-api) for generally available APIs.
  The Kubernetes project has no plans to remove Ingress from Kubernetes.
- The Ingress API is no longer being developed, and will have no further changes
  or updates made to it.