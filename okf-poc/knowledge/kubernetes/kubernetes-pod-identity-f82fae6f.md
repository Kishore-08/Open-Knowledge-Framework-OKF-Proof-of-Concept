---
id: kubernetes-pod-identity-f82fae6f
type: concept
title: Pod Identity
description: StatefulSet Pods have a unique identity that consists of an ordinal,
  a
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

## Pod Identity

StatefulSet Pods have a unique identity that consists of an ordinal, a
stable network identity, and stable storage. The identity sticks to the Pod,
regardless of which node it's (re)scheduled on.