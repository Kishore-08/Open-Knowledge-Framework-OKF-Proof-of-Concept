---
id: kubernetes-aggregation-layer-9c401218
type: concept
title: Aggregation layer
description: The aggregation layer runs in-process with the kube-apiserver. Until
  an extension resource is
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/apiserver-aggregation/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

## Aggregation layer

The aggregation layer runs in-process with the kube-apiserver. Until an extension resource is
registered, the aggregation layer will do nothing. To register an API, you add an *APIService*
object, which "claims" the URL path in the Kubernetes API. At that point, the aggregation layer
will proxy anything sent to that API path (e.g. `/apis/myextension.mycompany.io/v1/…`) to the
registered APIService.

The most common way to implement the APIService is to run an *extension API server* in Pod(s) that
run in your cluster. If you're using the extension API server to manage resources in your cluster,
the extension API server (also written as "extension-apiserver") is typically paired with one or
more [controllers](https://kubernetes.io/docs/concepts/architecture/controller/ "A control loop that watches the shared state of the cluster through the apiserver and makes changes attempting to move the current state towards the desired state."). The apiserver-builder
library provides a skeleton for both extension API servers and the associated controller(s).