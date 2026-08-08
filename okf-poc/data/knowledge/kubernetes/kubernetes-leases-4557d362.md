---
id: kubernetes-leases-4557d362
type: concept
title: Leases
description: Distributed systems often have a need for *leases*, which provide a mechanism
  to lock shared resources
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/architecture/leases/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

# Leases

Distributed systems often have a need for *leases*, which provide a mechanism to lock shared resources
and coordinate activity between members of a set.
In Kubernetes, the lease concept is represented by [Lease](https://kubernetes.io/docs/reference/kubernetes-api/cluster-resources/lease-v1/)
objects in the `coordination.k8s.io` [API Group](https://kubernetes.io/docs/concepts/overview/kubernetes-api/#api-groups-and-versioning "A set of related paths in the Kubernetes API."),
which are used for system-critical capabilities such as node heartbeats and component-level leader election.