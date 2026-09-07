---
id: kubernetes-what-is-a-compositepodgroup-cabfab21
type: concept
title: What is a CompositePodGroup?
description: The `CompositePodGroup` API resource is part of the `scheduling.k8s.io/v1alpha3`
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/compositepodgroup-api/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

## What is a CompositePodGroup?

The `CompositePodGroup` API resource is part of the `scheduling.k8s.io/v1alpha3`
[API group](https://kubernetes.io/docs/concepts/overview/kubernetes-api/#api-groups-and-versioning "A set of related paths in the Kubernetes API."). Your cluster must have that API
group enabled, as well as the `CompositePodGroup`
[feature gate](https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/),
before you can use this API.

A `CompositePodGroup` represents a grouping of child groups (which can be `CompositePodGroup` or
`PodGroup` objects). It carries scheduling policies, disruption modes, priority
settings, and optional topology constraints that apply collectively across its child groups.

## API structure

A `CompositePodGroup` consists of a `spec` that defines the desired scheduling behavior
for its child groups, and a `status` subresource.