---
id: kubernetes-podgroup-lifecycle-3f08e71b
type: concept
title: PodGroup Lifecycle
description: 'FEATURE STATE:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/podgroup-api/lifecycle/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

# PodGroup Lifecycle

FEATURE STATE:
`Kubernetes v1.37 [beta]`(disabled by default)

A [PodGroup](https://kubernetes.io/docs/concepts/workloads/podgroup-api/) is scheduled as a unit and protected
from premature deletion while its Pods are still running.