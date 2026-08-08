---
id: kubernetes-what-is-a-workload-1182b951
type: concept
title: What is a Workload?
description: The Workload API resource is part of the `scheduling.k8s.io/v1alpha2`
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/workload-api/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

## What is a Workload?

The Workload API resource is part of the `scheduling.k8s.io/v1alpha2`
[API group](https://kubernetes.io/docs/concepts/overview/kubernetes-api/#api-groups-and-versioning "A set of related paths in the Kubernetes API.")
and your cluster must have that API group enabled, as well as the `GenericWorkload`
[feature gate](https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/),
before you can use this API.

A `Workload` is a static, long-lived policy template. It defines what scheduling
policies should be applied to groups of Pods, but does not track runtime state itself.
Runtime scheduling state is maintained by [PodGroup](https://kubernetes.io/docs/concepts/workloads/podgroup-api/)
objects, which controllers create from the `Workload`'s `PodGroupTemplates`.