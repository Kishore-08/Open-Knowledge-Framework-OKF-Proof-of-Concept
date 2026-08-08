---
id: kubernetes-examples-57527b9b
type: concept
title: Examples
description: Process all object configuration files in the `configs` directory, and
  create or
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/overview/working-with-objects/object-management/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Examples

Process all object configuration files in the `configs` directory, and create or
patch the live objects. You can first `diff` to see what changes are going to be
made, and then apply:

```
kubectl diff -f configs/
kubectl apply -f configs/
```

Recursively process directories:

```
kubectl diff -R -f configs/
kubectl apply -R -f configs/
```