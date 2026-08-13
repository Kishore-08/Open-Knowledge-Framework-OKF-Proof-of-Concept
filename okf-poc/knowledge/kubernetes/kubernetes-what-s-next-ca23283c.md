---
id: kubernetes-what-s-next-ca23283c
type: concept
title: What's next
description: Instead of Gateway API resources being natively implemented by Kubernetes,
  the specifications
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/services-networking/gateway/
updated_at: '2026-08-13'
created_at: '2026-08-13'
---

## What's next

Instead of Gateway API resources being natively implemented by Kubernetes, the specifications
are defined as [Custom Resources](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/)
supported by a wide range of [implementations](https://gateway-api.sigs.k8s.io/implementations/).
[Install](https://gateway-api.sigs.k8s.io/guides/#installing-gateway-api) the Gateway API CRDs or
follow the installation instructions of your selected implementation. After installing an
implementation, use the [Getting Started](https://gateway-api.sigs.k8s.io/guides/) guide to help
you quickly start working with Gateway API.

#### Note:

Make sure to review the documentation of your selected implementation to understand any caveats.

Refer to the [API specification](https://gateway-api.sigs.k8s.io/reference/api-spec/main/spec/) for additional
details of all Gateway API kinds.