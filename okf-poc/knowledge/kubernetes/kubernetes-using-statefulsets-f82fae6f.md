---
id: kubernetes-using-statefulsets-f82fae6f
type: concept
title: Using StatefulSets
description: StatefulSets are valuable for applications that require one or more of
  the
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/
updated_at: '2026-08-13'
created_at: '2026-08-13'
---

## Using StatefulSets

StatefulSets are valuable for applications that require one or more of the
following:

- Stable, unique network identifiers.
- Stable, persistent storage.
- Ordered, graceful deployment and scaling.
- Ordered, automated rolling updates.

In the above, stable is synonymous with persistence across Pod (re)scheduling.
If an application doesn't require any stable identifiers or ordered deployment,
deletion, or scaling, you should deploy your application using a workload object
that provides a set of stateless replicas.
[Deployment](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/) or
[ReplicaSet](https://kubernetes.io/docs/concepts/workloads/controllers/replicaset/) may be better suited to your stateless needs.