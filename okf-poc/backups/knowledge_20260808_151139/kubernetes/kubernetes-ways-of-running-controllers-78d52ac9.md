---
id: kubernetes-ways-of-running-controllers-78d52ac9
type: concept
title: Ways of running controllers
description: Kubernetes comes with a set of built-in controllers that run inside
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/architecture/controller/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

## Ways of running controllers

Kubernetes comes with a set of built-in controllers that run inside
the [kube-controller-manager](https://kubernetes.io/docs/reference/command-line-tools-reference/kube-controller-manager/ "Control Plane component that runs controller processes."). These
built-in controllers provide important core behaviors.

The Deployment controller and Job controller are examples of controllers that
come as part of Kubernetes itself ("built-in" controllers).
Kubernetes lets you run a resilient control plane, so that if any of the built-in
controllers were to fail, another part of the control plane will take over the work.

You can find controllers that run outside the control plane, to extend Kubernetes.
Or, if you want, you can write a new controller yourself.
You can run your own controller as a set of Pods,
or externally to Kubernetes. What fits best will depend on what that particular
controller does.