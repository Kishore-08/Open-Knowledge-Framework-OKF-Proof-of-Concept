---
id: kubernetes-accessing-a-custom-resource-0f516df7
type: concept
title: Accessing a custom resource
description: Kubernetes [client libraries](https://kubernetes.io/docs/reference/using-api/client-libraries/)
  can be used to access
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

## Accessing a custom resource

Kubernetes [client libraries](https://kubernetes.io/docs/reference/using-api/client-libraries/) can be used to access
custom resources. Not all client libraries support custom resources. The *Go* and *Python* client
libraries do.

When you add a custom resource, you can access it using:

- `kubectl`
- The Kubernetes dynamic client.
- A REST client that you write.
- A client generated using [Kubernetes client generation tools](https://github.com/kubernetes/code-generator)
  (generating one is an advanced undertaking, but some projects may provide a client along with
  the CRD or AA).