---
id: kubernetes-start-ordinal-f82fae6f
type: concept
title: Start ordinal
description: 'FEATURE STATE:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/
updated_at: '2026-08-13'
created_at: '2026-08-13'
---

### Start ordinal

FEATURE STATE:
`Kubernetes v1.31 [stable]`(enabled by default)

`.spec.ordinals` is an optional field that allows you to configure the integer
ordinals assigned to each Pod. It defaults to nil. Within the field, you can
configure the following options:

- `.spec.ordinals.start`: If the `.spec.ordinals.start` field is set, Pods will
  be assigned ordinals from `.spec.ordinals.start` up through
  `.spec.ordinals.start + .spec.replicas - 1`.