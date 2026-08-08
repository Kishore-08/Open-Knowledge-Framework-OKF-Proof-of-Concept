---
id: kubernetes-should-i-add-a-custom-resource-to-my-kubernetes-cluster-0f516df7
type: concept
title: Should I add a custom resource to my Kubernetes cluster?
description: When creating a new API, consider whether to
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

## Should I add a custom resource to my Kubernetes cluster?

When creating a new API, consider whether to
[aggregate your API with the Kubernetes cluster APIs](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/apiserver-aggregation/)
or let your API stand alone.

| Consider API aggregation if: | Prefer a stand-alone API if: |
| --- | --- |
| Your API is [Declarative](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/#declarative-apis). | Your API does not fit the [Declarative](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/#declarative-apis) model. |
| You want your new types to be readable and writable using `kubectl`. | `kubectl` support is not required |
| You want to view your new types in a Kubernetes UI, such as dashboard, alongside built-in types. | Kubernetes UI support is not required. |
| You are developing a new API. | You already have a program that serves your API and works well. |
| You are willing to accept the format restriction that Kubernetes puts on REST resource paths, such as API Groups and Namespaces. (See the [API Overview](https://kubernetes.io/docs/concepts/overview/kubernetes-api/).) | You need to have specific REST paths to be compatible with an already defined REST API. |
| Your resources are naturally scoped to a cluster or namespaces of a cluster. | Cluster or namespace scoped resources are a poor fit; you need control over the specifics of resource paths. |
| You want to reuse [Kubernetes API support features](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/#common-features). | You don't need those features. |