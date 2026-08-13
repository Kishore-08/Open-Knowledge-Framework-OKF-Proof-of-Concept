---
id: kubernetes-pod-selector-f82fae6f
type: concept
title: Pod Selector
description: You must set the `.spec.selector` field of a StatefulSet to match the
  labels of its
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/
updated_at: '2026-08-13'
created_at: '2026-08-13'
---

### Pod Selector

You must set the `.spec.selector` field of a StatefulSet to match the labels of its
`.spec.template.metadata.labels`. Failing to specify a matching Pod Selector will result in a
validation error during StatefulSet creation.