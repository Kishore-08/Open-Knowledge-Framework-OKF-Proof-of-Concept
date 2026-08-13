---
id: kubernetes-viewing-namespaces-0663647e
type: concept
title: Viewing namespaces
description: 'You can list the current namespaces in a cluster using:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/
updated_at: '2026-08-13'
created_at: '2026-08-13'
---

### Viewing namespaces

You can list the current namespaces in a cluster using:

```
kubectl get namespace
```

```
NAME              STATUS   AGE
default           Active   1d
kube-node-lease   Active   1d
kube-public       Active   1d
kube-system       Active   1d
```