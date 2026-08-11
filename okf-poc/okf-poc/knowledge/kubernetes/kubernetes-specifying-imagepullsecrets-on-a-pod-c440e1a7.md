---
id: kubernetes-specifying-imagepullsecrets-on-a-pod-c440e1a7
type: concept
title: Specifying `imagePullSecrets` on a Pod
description: This is the recommended approach to run containers based on images
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/containers/images/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Specifying `imagePullSecrets` on a Pod

#### Note:

This is the recommended approach to run containers based on images
in private registries.

Kubernetes supports specifying container image registry keys on a Pod.
All `imagePullSecrets` must be Secrets that exist in the same
[Namespace](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces "An abstraction used by Kubernetes to support isolation of groups of resources within a single cluster.") as the
Pod. These Secrets must be of type `kubernetes.io/dockercfg` or `kubernetes.io/dockerconfigjson`.