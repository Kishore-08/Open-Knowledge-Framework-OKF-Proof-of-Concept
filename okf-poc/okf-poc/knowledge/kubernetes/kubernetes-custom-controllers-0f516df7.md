---
id: kubernetes-custom-controllers-0f516df7
type: concept
title: Custom controllers
description: On their own, custom resources let you store and retrieve structured
  data.
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

## Custom controllers

On their own, custom resources let you store and retrieve structured data.
When you combine a custom resource with a *custom controller*, custom resources
provide a true *declarative API*.

The Kubernetes [declarative API](https://kubernetes.io/docs/concepts/overview/kubernetes-api/)
enforces a separation of responsibilities. You declare the desired state of
your resource. The Kubernetes controller keeps the current state of Kubernetes
objects in sync with your declared desired state. This is in contrast to an
imperative API, where you *instruct* a server what to do.

You can deploy and update a custom controller on a running cluster, independently
of the cluster's lifecycle. Custom controllers can work with any kind of resource,
but they are especially effective when combined with custom resources. The
[Operator pattern](https://kubernetes.io/docs/concepts/extend-kubernetes/operator/) combines custom
resources and custom controllers. You can use custom controllers to encode domain knowledge
for specific applications into an extension of the Kubernetes API.