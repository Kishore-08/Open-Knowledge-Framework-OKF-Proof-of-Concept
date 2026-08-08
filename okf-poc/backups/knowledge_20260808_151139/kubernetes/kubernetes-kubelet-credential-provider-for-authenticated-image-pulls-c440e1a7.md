---
id: kubernetes-kubelet-credential-provider-for-authenticated-image-pulls-c440e1a7
type: concept
title: Kubelet credential provider for authenticated image pulls
description: You can configure the kubelet to invoke a plugin binary to dynamically
  fetch
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/containers/images/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Kubelet credential provider for authenticated image pulls

You can configure the kubelet to invoke a plugin binary to dynamically fetch
registry credentials for a container image. This is the most robust and versatile
way to fetch credentials for private registries, but also requires kubelet-level
configuration to enable.

This technique can be especially useful for running [static Pods](https://kubernetes.io/docs/tasks/configure-pod-container/static-pod/ "A pod managed directly by the kubelet daemon on a specific node.")
that require container images hosted in a private registry.
Using a [ServiceAccount](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/ "Provides an identity for processes that run in a Pod.") or a
[Secret](https://kubernetes.io/docs/concepts/configuration/secret/ "Stores sensitive information, such as passwords, OAuth tokens, and ssh keys.") to provide private registry credentials
is not possible in the specification of a static Pod, because it *cannot*
have references to other API resources in its specification.

See [Configure a kubelet image credential provider](https://kubernetes.io/docs/tasks/administer-cluster/kubelet-credential-provider/) for more details.