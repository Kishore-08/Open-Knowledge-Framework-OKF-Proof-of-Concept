---
id: kubernetes-resource-quotas-193abbf6
type: concept
title: Resource Quotas
description: When several users or teams share a cluster with a fixed number of nodes,
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/policy/resource-quotas/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

# Resource Quotas

When several users or teams share a cluster with a fixed number of nodes,
there is a concern that one team could use more than its fair share of resources.

*Resource quotas* are a tool for administrators to address this concern.

A resource quota, defined by a ResourceQuota object, provides constraints that limit
aggregate resource consumption per [namespace](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces "An abstraction used by Kubernetes to support isolation of groups of resources within a single cluster."). A ResourceQuota can also
limit the [quantity of objects that can be created in a namespace](https://kubernetes.io/docs/concepts/policy/resource-quotas/#quota-on-object-count) by API kind, as well as the total
amount of [infrastructure resources](https://kubernetes.io/docs/reference/glossary/?all=true#term-infrastructure-resource "A defined amount of infrastructure available for consumption (CPU, memory, etc).") that may be consumed by
API objects found in that namespace.

#### Caution:

Neither contention nor changes to quota will affect already created resources.