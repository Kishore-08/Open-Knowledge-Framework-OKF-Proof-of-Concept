---
id: kubernetes-desired-versus-current-state-78d52ac9
type: concept
title: Desired versus current state
description: Kubernetes takes a cloud-native view of systems, and is able to handle
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/architecture/controller/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

## Desired versus current state

Kubernetes takes a cloud-native view of systems, and is able to handle
constant change.

Your cluster could be changing at any point as work happens and
control loops automatically fix failures. This means that,
potentially, your cluster never reaches a stable state.

As long as the controllers for your cluster are running and able to make
useful changes, it doesn't matter if the overall state is stable or not.