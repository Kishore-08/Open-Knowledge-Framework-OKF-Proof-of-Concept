---
id: kubernetes-scheduling-building-block-apis-and-the-workloadbuilder-libra-497d3b3e
type: concept
title: Scheduling Building Block APIs and the workloadbuilder Library
description: Reusable scheduling API primitives that in-tree and out-of-tree workload
  controllers embed in their own APIs, and the shared workloadbuilder library that
  compiles them into Workload, PodGroup, and Com
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/workload-api/workloadbuilder/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

# Scheduling Building Block APIs and the workloadbuilder Library

Reusable scheduling API primitives that in-tree and out-of-tree workload controllers embed in their own APIs, and the shared workloadbuilder library that compiles them into Workload, PodGroup, and CompositePodGroup objects.

FEATURE STATE:
`Kubernetes v1.37 [beta]`(disabled by default)

Workload-aware Scheduling defines a set of reusable API *building blocks* under the
`scheduling.k8s.io` [API group](https://kubernetes.io/docs/concepts/overview/kubernetes-api/#api-groups-and-versioning "A set of related paths in the Kubernetes API.").
Controller authors embed these primitives into their own APIs so that users express
scheduling intent (gang scheduling, topology, disruption behavior) with a consistent
schema across the ecosystem, and the shared `workloadbuilder` library compiles that
intent into the scheduler-facing [Workload](https://kubernetes.io/docs/concepts/workloads/workload-api/),
[PodGroup](https://kubernetes.io/docs/concepts/workloads/podgroup-api/), and [CompositePodGroup](https://kubernetes.io/docs/concepts/workloads/workload-api/compositepodgroup-api/) objects.

The built-in consumer of these building blocks today is the
[Job](https://kubernetes.io/docs/concepts/workloads/controllers/job/) controller, gated by the
`WorkloadWithJob` [feature gate](https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/).