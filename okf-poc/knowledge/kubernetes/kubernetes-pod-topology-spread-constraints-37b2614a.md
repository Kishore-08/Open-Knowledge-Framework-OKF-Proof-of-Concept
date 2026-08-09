---
id: kubernetes-pod-topology-spread-constraints-37b2614a
type: concept
title: Pod topology spread constraints
description: You can use *topology spread constraints* to control how [Pods](https://kubernetes.io/docs/concepts/workloads/pods/
  "A Pod represents a set of running containers in your cluster.")
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

## Pod topology spread constraints

You can use *topology spread constraints* to control how [Pods](https://kubernetes.io/docs/concepts/workloads/pods/ "A Pod represents a set of running containers in your cluster.")
are spread across your cluster among failure-domains such as regions, zones, nodes, or among any other
topology domains that you define. You might do this to improve performance, expected availability, or
overall utilization.

Read [Pod topology spread constraints](https://kubernetes.io/docs/concepts/scheduling-eviction/topology-spread-constraints/)
to learn more about how these work.