---
id: kubernetes-imperative-commands-57527b9b
type: concept
title: Imperative commands
description: When using imperative commands, a user operates directly on live objects
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/overview/working-with-objects/object-management/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

## Imperative commands

When using imperative commands, a user operates directly on live objects
in a cluster. The user provides operations to
the `kubectl` command as arguments or flags.

This is the recommended way to get started or to run a one-off task in
a cluster. Because this technique operates directly on live
objects, it provides no history of previous configurations.

### Examples

Run an instance of the nginx container by creating a Deployment object:

```
kubectl create deployment nginx --image nginx
```