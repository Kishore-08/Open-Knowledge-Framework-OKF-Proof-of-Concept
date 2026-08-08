---
id: kubernetes-legacy-built-in-kubelet-credential-provider-c440e1a7
type: concept
title: Legacy built-in kubelet credential provider
description: In older versions of Kubernetes, the kubelet had a direct integration
  with cloud
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/containers/images/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

## Legacy built-in kubelet credential provider

In older versions of Kubernetes, the kubelet had a direct integration with cloud
provider credentials. This provided the ability to dynamically fetch credentials
for image registries.

There were three built-in implementations of the kubelet credential provider
integration: ACR (Azure Container Registry), ECR (Elastic Container Registry),
and GCR (Google Container Registry).

Starting with version 1.26 of Kubernetes, the legacy mechanism has been removed,
so you would need to either:

- configure a kubelet image credential provider on each node; or
- specify image pull credentials using `imagePullSecrets` and at least one Secret.