---
id: kubernetes-managing-rollouts-47e6546b
type: concept
title: Managing rollouts
description: You can use [`kubectl rollout`](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_rollout/)
  to manage a
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/management/
updated_at: '2026-08-13'
created_at: '2026-08-13'
---

### Managing rollouts

You can use [`kubectl rollout`](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_rollout/) to manage a
progressive update of an existing application.

For example:

```
kubectl apply -f my-deployment.yaml

# wait for rollout to finish
kubectl rollout status deployment/my-deployment --timeout 10m # 10 minute timeout
```

or

```
kubectl apply -f backing-stateful-component.yaml

# don't wait for rollout to finish, just check the status
kubectl rollout status statefulsets/backing-stateful-component --watch=false
```

You can also pause, resume or cancel a rollout.
Visit [`kubectl rollout`](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_rollout/) to learn more.