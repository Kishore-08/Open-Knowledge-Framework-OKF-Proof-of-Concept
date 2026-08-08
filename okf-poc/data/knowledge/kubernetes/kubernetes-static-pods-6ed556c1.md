---
id: kubernetes-static-pods-6ed556c1
type: concept
title: Static Pods
description: '*Static Pods* are managed directly by the kubelet daemon on a specific
  node,'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/pods/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

## Static Pods

*Static Pods* are managed directly by the kubelet daemon on a specific node,
without the [API server](https://kubernetes.io/docs/concepts/architecture/#kube-apiserver "Control plane component that serves the Kubernetes API.")
observing them.
Whereas most Pods are managed by the control plane (for example, a
[Deployment](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/ "Manages a replicated application on your cluster.")), for static
Pods, the kubelet directly supervises each static Pod (and restarts it if it fails).

Static Pods are always bound to one [Kubelet](https://kubernetes.io/docs/reference/command-line-tools-reference/kubelet "An agent that runs on each node in the cluster. It makes sure that containers are running in a pod.") on a specific node.
The main use for static Pods is to run a self-hosted control plane: in other words,
using the kubelet to supervise the individual [control plane components](https://kubernetes.io/docs/concepts/architecture/#control-plane-components).

For details, see [Static Pods](https://kubernetes.io/docs/concepts/workloads/pods/static-pods/).