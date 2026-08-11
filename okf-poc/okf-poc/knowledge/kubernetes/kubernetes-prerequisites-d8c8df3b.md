---
id: kubernetes-prerequisites-d8c8df3b
type: concept
title: Prerequisites
description: You must have an [Ingress controller](https://kubernetes.io/docs/concepts/services-networking/ingress-controllers/)
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/services-networking/ingress/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

## Prerequisites

You must have an [Ingress controller](https://kubernetes.io/docs/concepts/services-networking/ingress-controllers/)
to satisfy an Ingress. Only creating an Ingress resource has no effect.

You can choose from a number of [Ingress controllers](https://kubernetes.io/docs/concepts/services-networking/ingress-controllers/).

Ideally, all Ingress controllers should fit the reference specification. In reality, the various Ingress
controllers operate slightly differently.

#### Note:

Make sure you review your Ingress controller's documentation to understand the caveats of choosing it.