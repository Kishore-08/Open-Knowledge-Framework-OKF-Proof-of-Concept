---
id: kubernetes-pods-and-controllers-6ed556c1
type: concept
title: Pods and controllers
description: You can use workload resources to create and manage multiple Pods for
  you. A controller
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/pods/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Pods and controllers

You can use workload resources to create and manage multiple Pods for you. A controller
for the resource handles replication and rollout and automatic healing in case of
Pod failure. For example, if a Node fails, a controller notices that Pods on that
Node have stopped working and creates a replacement Pod. The scheduler places the
replacement Pod onto a healthy Node.

Here are some examples of workload resources that manage one or more Pods:

- [Deployment](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/ "Manages a replicated application on your cluster.")
- [StatefulSet](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/ "A StatefulSet manages deployment and scaling of a set of Pods, with durable storage and persistent identifiers for each Pod.")
- [DaemonSet](https://kubernetes.io/docs/concepts/workloads/controllers/daemonset "Ensures a copy of a Pod is running across a set of nodes in a cluster.")