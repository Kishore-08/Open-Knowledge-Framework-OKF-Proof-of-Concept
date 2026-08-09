---
id: kubernetes-adding-custom-resources-0f516df7
type: concept
title: Adding custom resources
description: 'Kubernetes provides two ways to add custom resources to your cluster:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

## Adding custom resources

Kubernetes provides two ways to add custom resources to your cluster:

- CRDs are simple and can be created without any programming.
- [API Aggregation](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/apiserver-aggregation/)
  requires programming, but allows more control over API behaviors like how data is stored and
  conversion between API versions.

Kubernetes provides these two options to meet the needs of different users, so that neither ease
of use nor flexibility is compromised.

Aggregated APIs are subordinate API servers that sit behind the primary API server, which acts as
a proxy. This arrangement is called [API Aggregation](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/apiserver-aggregation/)(AA).
To users, the Kubernetes API appears extended.

CRDs allow users to create new types of resources without adding another API server. You do not
need to understand API Aggregation to use CRDs.

Regardless of how they are installed, the new resources are referred to as Custom Resources to
distinguish them from built-in Kubernetes resources (like pods).

#### Note:

Avoid using a Custom Resource as data storage for application, end user, or monitoring data:
architecture designs that store application data within the Kubernetes API typically represent
a design that is too closely coupled.

Architecturally, [cloud native](https://www.cncf.io/about/faq/#what-is-cloud-native) application architectures
favor loose coupling between components. If part of your workload requires a backing service for
its routine operation, run that backing service as a component or consume it as an external service.
This way, your workload does not rely on the Kubernetes API for its normal operation.