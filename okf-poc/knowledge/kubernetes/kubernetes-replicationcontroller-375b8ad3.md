---
id: kubernetes-replicationcontroller-375b8ad3
type: concept
title: ReplicationController
description: ReplicaSets are the successors to [ReplicationControllers](https://kubernetes.io/docs/concepts/workloads/controllers/replicationcontroller/).
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/controllers/replicaset/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### ReplicationController

ReplicaSets are the successors to [ReplicationControllers](https://kubernetes.io/docs/concepts/workloads/controllers/replicationcontroller/).
The two serve the same purpose, and behave similarly, except that a ReplicationController does not support set-based
selector requirements as described in the [labels user guide](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#label-selectors).
As such, ReplicaSets are preferred over ReplicationControllers