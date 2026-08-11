---
id: kubernetes-deleting-a-replicaset-and-its-pods-375b8ad3
type: concept
title: Deleting a ReplicaSet and its Pods
description: To delete a ReplicaSet and all of its Pods, use
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/controllers/replicaset/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Deleting a ReplicaSet and its Pods

To delete a ReplicaSet and all of its Pods, use
[`kubectl delete`](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#delete). The
[Garbage collector](https://kubernetes.io/docs/concepts/architecture/garbage-collection/) automatically deletes all of
the dependent Pods by default.

When using the REST API or the `client-go` library, you must set `propagationPolicy` to
`Background` or `Foreground` in the `-d` option. For example:

```
kubectl proxy --port=8080
curl -X DELETE  'localhost:8080/apis/apps/v1/namespaces/default/replicasets/frontend' \
  -d '{"kind":"DeleteOptions","apiVersion":"v1","propagationPolicy":"Foreground"}' \
  -H "Content-Type: application/json"
```