---
id: kubernetes-resizing-pods-3e34f258
type: concept
title: Resizing Pods
description: 'FEATURE STATE:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

## Resizing Pods

FEATURE STATE:
`Kubernetes v1.35 [stable]`(enabled by default)

FEATURE STATE:
`Kubernetes v1.36 [beta]`(enabled by default)

Kubernetes supports changing the CPU and memory resources allocated to Pods
after they are created. (For other infrastructure resources, you would need to
use different techniques specific to those resources.) There are two main
approaches to resizing CPU and memory: