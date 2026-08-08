---
id: kubernetes-what-is-a-podgroup-0cf588b5
type: concept
title: What is a PodGroup?
description: The PodGroup API resource is part of the `scheduling.k8s.io/v1alpha2`
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/podgroup-api/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

## What is a PodGroup?

The PodGroup API resource is part of the `scheduling.k8s.io/v1alpha2`
[API group](https://kubernetes.io/docs/concepts/overview/kubernetes-api/#api-groups-and-versioning "A set of related paths in the Kubernetes API.")
and your cluster must have that API group enabled, as well as the `GenericWorkload`
[feature gate](https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/),
before you can use this API.

A PodGroup is a self-contained scheduling unit. It defines the group of Pods that should be scheduled together, carries the
scheduling policy that governs placement, and records the runtime status of that
scheduling decision.

## API structure

A PodGroup consists of a `spec` that defines the desired scheduling behavior and
a `status` that reflects the current scheduling state.