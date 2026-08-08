---
id: kubernetes-api-server-aggregation-0f516df7
type: concept
title: API server aggregation
description: Usually, each resource in the Kubernetes API requires code that handles
  REST requests and manages
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

## API server aggregation

Usually, each resource in the Kubernetes API requires code that handles REST requests and manages
persistent storage of objects. The main Kubernetes API server handles built-in resources like
*pods* and *services*, and can also generically handle custom resources through
[CRDs](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/#customresourcedefinitions).

The [aggregation layer](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/apiserver-aggregation/)
allows you to provide specialized implementations for your custom resources by writing and
deploying your own API server.
The main API server delegates requests to your API server for the custom resources that you handle,
making them available to all of its clients.