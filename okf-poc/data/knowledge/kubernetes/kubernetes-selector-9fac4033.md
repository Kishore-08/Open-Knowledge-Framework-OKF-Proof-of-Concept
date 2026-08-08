---
id: kubernetes-selector-9fac4033
type: concept
title: Selector
description: Claims can specify a
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/storage/persistent-volumes/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Selector

Claims can specify a
[label selector](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#label-selectors)
to further filter the set of volumes.
Only the volumes whose labels match the selector can be bound to the claim.
The selector can consist of two fields:

- `matchLabels` - the volume must have a label with this value
- `matchExpressions` - a list of requirements made by specifying key, list of values,
  and operator that relates the key and values.
  Valid operators include `In`, `NotIn`, `Exists`, and `DoesNotExist`.

All of the requirements, from both `matchLabels` and `matchExpressions`, are
ANDed together – they must all be satisfied in order to match.