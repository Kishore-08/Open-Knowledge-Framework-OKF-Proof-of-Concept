---
id: kubernetes-securitycontext-interactions-18ab9e15
type: concept
title: SecurityContext interactions
description: The [proposal](https://git.k8s.io/enhancements/keps/sig-storage/2451-service-account-token-volumes#proposal)
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/storage/projected-volumes/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

## SecurityContext interactions

The [proposal](https://git.k8s.io/enhancements/keps/sig-storage/2451-service-account-token-volumes#proposal)
for file permission handling in projected service account volume enhancement
introduced the projected files having the correct owner permissions set.