---
id: kubernetes-controller-pattern-78d52ac9
type: concept
title: Controller pattern
description: A controller tracks at least one Kubernetes resource type.
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/architecture/controller/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

## Controller pattern

A controller tracks at least one Kubernetes resource type.
These [objects](https://kubernetes.io/docs/concepts/overview/working-with-objects/#kubernetes-objects "An entity in the Kubernetes system, representing part of the state of your cluster.")
have a spec field that represents the desired state. The
controller(s) for that resource are responsible for making the current
state come closer to that desired state.

The controller might carry the action out itself; more commonly, in Kubernetes,
a controller will send messages to the
[API server](https://kubernetes.io/docs/concepts/architecture/#kube-apiserver "Control plane component that serves the Kubernetes API.") that have
useful side effects. You'll see examples of this below.