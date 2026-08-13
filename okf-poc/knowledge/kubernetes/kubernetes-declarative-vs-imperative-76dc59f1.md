---
id: kubernetes-declarative-vs-imperative-76dc59f1
type: concept
title: Declarative vs imperative
description: For production workloads, prefer [declarative object management](https://kubernetes.io/docs/concepts/overview/working-with-objects/object-management/)
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/overview/kubectl/
updated_at: '2026-08-13'
created_at: '2026-08-13'
---

## Declarative vs imperative

For production workloads, prefer [declarative object management](https://kubernetes.io/docs/concepts/overview/working-with-objects/object-management/)
using `kubectl apply` with version-controlled configuration files.
Declarative management helps you track changes, collaborate, and integrate with GitOps workflows.
Imperative commands (such as `kubectl create` or `kubectl run`) are useful for development and experimentation,
but are harder to reproduce and audit.