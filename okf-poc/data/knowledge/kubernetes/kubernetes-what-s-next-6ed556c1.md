---
id: kubernetes-what-s-next-6ed556c1
type: concept
title: What's next
description: '- Learn about the [lifecycle of a Pod](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/).'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/pods/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

## What's next

- Learn about the [lifecycle of a Pod](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/).
- Read about [PodDisruptionBudget](https://kubernetes.io/docs/concepts/workloads/pods/disruptions/)
  and how you can use it to manage application availability during disruptions.
- Pod is a top-level resource in the Kubernetes REST API.
  The
  [Pod](https://kubernetes.io/docs/reference/kubernetes-api/core/pod-v1/)
  object definition describes the object in detail.
- [The Distributed System Toolkit: Patterns for Composite Containers](https://kubernetes.io/blog/2015/06/the-distributed-system-toolkit-patterns/) explains common layouts for Pods with more than one container.
- Read about [Pod topology spread constraints](https://kubernetes.io/docs/concepts/scheduling-eviction/topology-spread-constraints/)
- Read [Advanced Pod Configuration](https://kubernetes.io/docs/concepts/workloads/pods/advanced-pod-config/) to learn the topic in detail.
  That page covers aspects of Pod configuration beyond the essentials, including:
  - PriorityClasses
  - RuntimeClasses
  - advanced ways to configure *scheduling*: the way that Kubernetes decides which node a Pod should run on.

To understand the context for why Kubernetes wraps a common Pod API in other resources
(such as [StatefulSets](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/ "A StatefulSet manages deployment and scaling of a set of Pods, with durable storage and persistent identifiers for each Pod.") or
[Deployments](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/ "Manages a replicated application on your cluster.")),
you can read about the prior art, including:

- [Aurora](https://aurora.apache.org/documentation/latest/reference/configuration/#job-schema)
- [Borg](https://research.google/pubs/large-scale-cluster-management-at-google-with-borg/)
- [Marathon](https://github.com/d2iq-archive/marathon)
- [Omega](https://research.google/pubs/pub41684/)
- [Tupperware](https://engineering.fb.com/data-center-engineering/tupperware/).