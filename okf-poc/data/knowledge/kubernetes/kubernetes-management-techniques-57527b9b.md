---
id: kubernetes-management-techniques-57527b9b
type: concept
title: Management techniques
description: A Kubernetes object should be managed using only one technique. Mixing
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/overview/working-with-objects/object-management/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

## Management techniques

#### Warning:

A Kubernetes object should be managed using only one technique. Mixing
and matching techniques for the same object results in undefined behavior.

| Management technique | Operates on | Recommended environment | Supported writers | Learning curve |
| --- | --- | --- | --- | --- |
| Imperative commands | Live objects | Development projects | 1+ | Lowest |
| Imperative object configuration | Individual files | Production projects | 1 | Moderate |
| Declarative object configuration | Directories of files | Production projects | 1+ | Highest |