---
id: kubernetes-ordinal-index-f82fae6f
type: concept
title: Ordinal Index
description: For a StatefulSet with N [replicas](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/#replicas),
  each Pod in the StatefulSet
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

### Ordinal Index

For a StatefulSet with N [replicas](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/#replicas), each Pod in the StatefulSet
will be assigned an integer ordinal, that is unique over the Set. By default,
pods will be assigned ordinals from 0 up through N-1. The StatefulSet controller
will also add a pod label with this index: `apps.kubernetes.io/pod-index`.