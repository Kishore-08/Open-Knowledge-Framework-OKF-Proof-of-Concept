---
id: kubernetes-image-pull-per-runtime-class-c440e1a7
type: concept
title: Image pull per runtime class
description: 'FEATURE STATE:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/containers/images/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Image pull per runtime class

FEATURE STATE:
`Kubernetes v1.29 [alpha]`(disabled by default)

Kubernetes includes alpha support for performing image pulls based on the RuntimeClass of a Pod.

If you enable the `RuntimeClassInImageCriApi` [feature gate](https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/),
the kubelet references container images by a tuple of image name and runtime handler
rather than just the image name or digest. Your
[container runtime](https://kubernetes.io/docs/setup/production-environment/container-runtimes "The container runtime is the software that is responsible for running containers.")
may adapt its behavior based on the selected runtime handler.
Pulling images based on runtime class is useful for VM-based containers, such as
Windows Hyper-V containers.