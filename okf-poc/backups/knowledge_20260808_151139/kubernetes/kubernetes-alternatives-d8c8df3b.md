---
id: kubernetes-alternatives-d8c8df3b
type: concept
title: Alternatives
description: 'You can expose a Service in multiple ways that don''t directly involve
  the Ingress resource:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/services-networking/ingress/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

## Alternatives

You can expose a Service in multiple ways that don't directly involve the Ingress resource:

- Use [Service.Type=LoadBalancer](https://kubernetes.io/docs/concepts/services-networking/service/#loadbalancer)
- Use [Service.Type=NodePort](https://kubernetes.io/docs/concepts/services-networking/service/#type-nodeport)