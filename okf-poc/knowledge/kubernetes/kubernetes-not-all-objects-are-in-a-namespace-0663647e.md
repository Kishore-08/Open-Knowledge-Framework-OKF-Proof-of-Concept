---
id: kubernetes-not-all-objects-are-in-a-namespace-0663647e
type: concept
title: Not all objects are in a namespace
description: Most Kubernetes resources (e.g. Pods, Services, Deployments, and others)
  are in some namespaces. However namespace resources are not themselves in a namespace.
  And low-level resources, such as
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/
updated_at: '2026-08-13'
created_at: '2026-08-13'
---

## Not all objects are in a namespace

Most Kubernetes resources (e.g. Pods, Services, Deployments, and others) are in some namespaces. However namespace resources are not themselves in a namespace. And low-level resources, such as
[Nodes](https://kubernetes.io/docs/concepts/architecture/nodes/) and
[PersistentVolumes](https://kubernetes.io/docs/concepts/storage/persistent-volumes/), are not in any namespace.

To see which Kubernetes resources are and aren't in a namespace:

```
# In a namespace
kubectl api-resources --namespaced=true

# Not in a namespace
kubectl api-resources --namespaced=false
```