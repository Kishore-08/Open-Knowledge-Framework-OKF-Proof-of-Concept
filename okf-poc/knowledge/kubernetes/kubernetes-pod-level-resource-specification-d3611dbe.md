---
id: kubernetes-pod-level-resource-specification-d3611dbe
type: concept
title: Pod-level resource specification
description: 'FEATURE STATE:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/
updated_at: '2026-08-13'
created_at: '2026-08-13'
---

## Pod-level resource specification

FEATURE STATE:
`Kubernetes v1.34 [beta]`(enabled by default)

Provided your cluster has the `PodLevelResources`
[feature gate](https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/) enabled,
you can specify resource requests and limits at
the Pod level. At the Pod level, Kubernetes 1.36
only supports resource requests or limits for specific resource types: `cpu` and /
or `memory` and / or `hugepages`. With this feature, Kubernetes allows you to declare an overall resource
budget for the Pod, which is especially helpful when dealing with a large number of
containers where it can be difficult to accurately gauge individual resource needs.
Additionally, it enables containers within a Pod to share idle resources with each
other, improving resource utilization.

For a Pod, you can specify resource limits and requests for CPU and memory by including the following:

- `spec.resources.limits.cpu`
- `spec.resources.limits.memory`
- `spec.resources.limits.hugepages-<size>`
- `spec.resources.requests.cpu`
- `spec.resources.requests.memory`
- `spec.resources.requests.hugepages-<size>`

## Resource units in Kubernetes