---
id: kubernetes-pod-security-admission-ebd20ed7
type: concept
title: Pod Security Admission
description: An overview of the Pod Security Admission Controller, which can enforce
  the Pod Security Standards.
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/security/pod-security-admission/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

# Pod Security Admission

An overview of the Pod Security Admission Controller, which can enforce the Pod Security Standards.

FEATURE STATE:
`Kubernetes v1.25 [stable]`

The Kubernetes [Pod Security Standards](https://kubernetes.io/docs/concepts/security/pod-security-standards/) define
different isolation levels for Pods. These standards let you define how you want to restrict the
behavior of pods in a clear, consistent fashion.

Kubernetes offers a built-in *Pod Security* [admission controller](https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers/ "A piece of code that intercepts requests to the Kubernetes API server prior to persistence of the object.") to enforce the Pod Security Standards. Pod security restrictions
are applied at the [namespace](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces "An abstraction used by Kubernetes to support isolation of groups of resources within a single cluster.") level when pods are
created.