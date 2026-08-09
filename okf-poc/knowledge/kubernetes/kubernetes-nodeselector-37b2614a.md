---
id: kubernetes-nodeselector-37b2614a
type: concept
title: nodeSelector
description: '`nodeSelector` is the simplest recommended form of node selection constraint.'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

## nodeSelector

`nodeSelector` is the simplest recommended form of node selection constraint.
You can add the `nodeSelector` field to your Pod specification and specify the
[node labels](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#built-in-node-labels) you want the target node to have.
Kubernetes only schedules the Pod onto nodes that have each of the labels you
specify.

See [Assign Pods to Nodes](https://kubernetes.io/docs/tasks/configure-pod-container/assign-pods-nodes/) for more
information.