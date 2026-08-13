---
id: kubernetes-context-827da0cf
type: concept
title: Context
description: A *context* element in a kubeconfig file is used to group access parameters
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/configuration/organize-cluster-access-kubeconfig/
updated_at: '2026-08-13'
created_at: '2026-08-13'
---

## Context

A *context* element in a kubeconfig file is used to group access parameters
under a convenient name. Each context has three parameters: cluster, namespace, and user.
By default, the `kubectl` command-line tool uses parameters from
the *current context* to communicate with the cluster.

To choose the current context:

```
kubectl config use-context
```