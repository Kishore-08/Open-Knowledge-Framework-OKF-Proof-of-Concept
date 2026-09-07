---
id: kubernetes-setting-the-namespace-for-a-request-0663647e
type: concept
title: Setting the namespace for a request
description: To set the namespace for a current request, use the `--namespace` flag.
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

### Setting the namespace for a request

To set the namespace for a current request, use the `--namespace` flag.

For example:

```
kubectl run nginx --image=nginx --namespace=<insert-namespace-name-here>
kubectl get pods --namespace=<insert-namespace-name-here>
```