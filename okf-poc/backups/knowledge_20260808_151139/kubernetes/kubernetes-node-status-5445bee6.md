---
id: kubernetes-node-status-5445bee6
type: concept
title: Node status
description: 'A Node''s status contains the following information:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/architecture/nodes/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

## Node status

A Node's status contains the following information:

- [Addresses](https://kubernetes.io/docs/reference/node/node-status/#addresses)
- [Conditions](https://kubernetes.io/docs/reference/node/node-status/#condition)
- [Capacity and Allocatable](https://kubernetes.io/docs/reference/node/node-status/#capacity)
- [Info](https://kubernetes.io/docs/reference/node/node-status/#info)

You can use `kubectl` to view a Node's status and other details:

```
kubectl describe node <insert-node-name-here>
```

See [Node Status](https://kubernetes.io/docs/reference/node/node-status/) for more details.