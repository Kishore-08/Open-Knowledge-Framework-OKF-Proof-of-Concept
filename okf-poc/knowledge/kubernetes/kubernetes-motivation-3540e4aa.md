---
id: kubernetes-motivation-3540e4aa
type: concept
title: Motivation
description: You can set a different RuntimeClass between different Pods to provide
  a balance of
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/containers/runtime-class/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

## Motivation

You can set a different RuntimeClass between different Pods to provide a balance of
performance versus security. For example, if part of your workload deserves a high
level of information security assurance, you might choose to schedule those Pods so
that they run in a container runtime that uses hardware virtualization. You'd then
benefit from the extra isolation of the alternative runtime, at the expense of some
additional overhead.

You can also use RuntimeClass to run different Pods with the same container runtime
but with different settings.

## Setup

1. Configure the CRI implementation on nodes (runtime dependent)
2. Create the corresponding RuntimeClass resources