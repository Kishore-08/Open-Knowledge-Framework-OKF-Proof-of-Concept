---
id: kubernetes-trade-offs-57527b9b
type: concept
title: Trade-offs
description: 'Advantages compared to imperative object configuration:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/overview/working-with-objects/object-management/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Trade-offs

Advantages compared to imperative object configuration:

- Changes made directly to live objects are retained, even if they are not merged back into the configuration files.
- Declarative object configuration has better support for operating on directories and automatically detecting operation types (create, patch, delete) per-object.

Disadvantages compared to imperative object configuration:

- Declarative object configuration is harder to debug and understand results when they are unexpected.
- Partial updates using diffs create complex merge and patch operations.