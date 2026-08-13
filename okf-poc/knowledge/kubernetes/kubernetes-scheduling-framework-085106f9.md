---
id: kubernetes-scheduling-framework-085106f9
type: concept
title: Scheduling Framework
description: 'FEATURE STATE:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/scheduling-eviction/scheduling-framework/
updated_at: '2026-08-13'
created_at: '2026-08-13'
---

# Scheduling Framework

FEATURE STATE:
`Kubernetes v1.19 [stable]`

The *scheduling framework* is a pluggable architecture for the Kubernetes scheduler.
It consists of a set of "plugin" APIs that are compiled directly into the scheduler.
These APIs allow most scheduling features to be implemented as plugins,
while keeping the scheduling "core" lightweight and maintainable. Refer to the
[design proposal of the scheduling framework](https://github.com/kubernetes/enhancements/blob/master/keps/sig-scheduling/624-scheduling-framework/README.md) for more technical information on
the design of the framework.