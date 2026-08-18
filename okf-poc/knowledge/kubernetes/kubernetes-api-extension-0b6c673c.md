---
id: kubernetes-api-extension-0b6c673c
type: concept
title: API Extension
description: 'The Kubernetes API can be extended in one of two ways:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/overview/kubernetes-api/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

## API Extension

The Kubernetes API can be extended in one of two ways:

1. [Custom resources](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/)
   let you declaratively define how the API server should provide your chosen resource API.
2. You can also extend the Kubernetes API by implementing an
   [aggregation layer](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/apiserver-aggregation/).