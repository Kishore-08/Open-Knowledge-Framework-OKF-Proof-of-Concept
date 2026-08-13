---
id: kubernetes-role-of-kubectl-76dc59f1
type: concept
title: Role of kubectl
description: The `kubectl` tool is the primary interface for creating, inspecting,
  updating, and deleting Kubernetes objects.
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/overview/kubectl/
updated_at: '2026-08-13'
created_at: '2026-08-13'
---

## Role of kubectl

The `kubectl` tool is the primary interface for creating, inspecting, updating, and deleting Kubernetes objects.
It complements the [Kubernetes Components](https://kubernetes.io/docs/concepts/overview/components/) that run inside your cluster
and the [Kubernetes API](https://kubernetes.io/docs/concepts/overview/kubernetes-api/) that those components implement.
Whether you run `kubectl` from your laptop or from a Pod inside the cluster, it sends requests to the API server.
Other clients, such as [client libraries](https://kubernetes.io/docs/reference/using-api/client-libraries/) and web dashboards
like [Headlamp](https://headlamp.dev/), also communicate through the same API.