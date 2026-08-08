---
id: kubernetes-node-name-uniqueness-5445bee6
type: concept
title: Node name uniqueness
description: The [name](https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names)
  identifies a Node. Two Nodes
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/architecture/nodes/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Node name uniqueness

The [name](https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names) identifies a Node. Two Nodes
cannot have the same name at the same time. Kubernetes also assumes that a resource with the same
name is the same object. In the case of a Node, it is implicitly assumed that an instance using the
same name will have the same state (e.g. network settings, root disk contents) and attributes like
node labels. This may lead to inconsistencies if an instance was modified without changing its name.
If the Node needs to be replaced or updated significantly, the existing Node object needs to be
removed from API server first and re-added after the update.