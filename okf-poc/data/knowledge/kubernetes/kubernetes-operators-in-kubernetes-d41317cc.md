---
id: kubernetes-operators-in-kubernetes-d41317cc
type: concept
title: Operators in Kubernetes
description: Kubernetes is designed for automation. Out of the box, you get lots of
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/extend-kubernetes/operator/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

## Operators in Kubernetes

Kubernetes is designed for automation. Out of the box, you get lots of
built-in automation from the core of Kubernetes. You can use Kubernetes
to automate deploying and running workloads, *and* you can automate how
Kubernetes does that.

Kubernetes' [operator pattern](https://kubernetes.io/docs/concepts/extend-kubernetes/operator/ "A specialized controller used to manage a custom resource")
concept lets you extend the cluster's behaviour without modifying the code of Kubernetes
itself by linking [controllers](https://kubernetes.io/docs/concepts/architecture/controller/ "A control loop that watches the shared state of the cluster through the apiserver and makes changes attempting to move the current state towards the desired state.") to
one or more custom resources. Operators are clients of the Kubernetes API that act as
controllers for a [Custom Resource](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/).