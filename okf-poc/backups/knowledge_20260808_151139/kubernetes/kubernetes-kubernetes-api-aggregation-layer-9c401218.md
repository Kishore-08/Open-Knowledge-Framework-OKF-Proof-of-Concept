---
id: kubernetes-kubernetes-api-aggregation-layer-9c401218
type: concept
title: Kubernetes API Aggregation Layer
description: The aggregation layer allows Kubernetes to be extended with additional
  APIs, beyond what is
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/apiserver-aggregation/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

# Kubernetes API Aggregation Layer

The aggregation layer allows Kubernetes to be extended with additional APIs, beyond what is
offered by the core Kubernetes APIs.
The additional APIs can either be ready-made solutions such as a
[metrics server](https://github.com/kubernetes-sigs/metrics-server), or APIs that you develop yourself.

The aggregation layer is different from
[Custom Resource Definitions](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/),
which are a way to make the [kube-apiserver](https://kubernetes.io/docs/concepts/architecture/#kube-apiserver "Control plane component that serves the Kubernetes API.")
recognise new kinds of object.