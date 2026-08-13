---
id: kubernetes-setting-the-namespace-preference-0663647e
type: concept
title: Setting the namespace preference
description: You can permanently save the namespace for all subsequent kubectl commands
  in that
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/
updated_at: '2026-08-13'
created_at: '2026-08-13'
---

### Setting the namespace preference

You can permanently save the namespace for all subsequent kubectl commands in that
context.

```
kubectl config set-context --current --namespace=<insert-namespace-name-here>
# Validate it
kubectl config view --minify | grep namespace:
```