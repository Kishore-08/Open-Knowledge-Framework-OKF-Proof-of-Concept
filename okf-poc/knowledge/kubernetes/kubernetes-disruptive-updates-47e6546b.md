---
id: kubernetes-disruptive-updates-47e6546b
type: concept
title: Disruptive updates
description: In some cases, you may need to update resource fields that cannot be
  updated once initialized, or
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/management/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

## Disruptive updates

In some cases, you may need to update resource fields that cannot be updated once initialized, or
you may want to make a recursive change immediately, such as to fix broken pods created by a
Deployment. To change such fields, use `replace --force`, which deletes and re-creates the
resource. In this case, you can modify your original configuration file:

```
kubectl replace -f https://k8s.io/examples/application/nginx/nginx-deployment.yaml --force
```

```
deployment.apps/my-nginx deleted
deployment.apps/my-nginx replaced
```

## What's next

- Learn about [how to use `kubectl` for application introspection and debugging](https://kubernetes.io/docs/tasks/debug/debug-application/debug-running-pod/).