---
id: kubernetes-migrating-from-ingress-ca23283c
type: concept
title: Migrating from Ingress
description: Gateway API is the successor to the [Ingress](https://kubernetes.io/docs/concepts/services-networking/ingress/)
  API.
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/services-networking/gateway/
updated_at: '2026-08-13'
created_at: '2026-08-13'
---

## Migrating from Ingress

Gateway API is the successor to the [Ingress](https://kubernetes.io/docs/concepts/services-networking/ingress/) API.
However, it does not include the Ingress kind. As a result, a one-time conversion from your existing
Ingress resources to Gateway API resources is necessary.

Refer to the [ingress migration](https://gateway-api.sigs.k8s.io/guides/getting-started/migrating-from-ingress)
guide for details on migrating Ingress resources to Gateway API resources.