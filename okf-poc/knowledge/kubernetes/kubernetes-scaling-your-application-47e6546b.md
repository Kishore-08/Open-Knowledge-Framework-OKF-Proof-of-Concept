---
id: kubernetes-scaling-your-application-47e6546b
type: concept
title: Scaling your application
description: When load on your application grows or shrinks, use `kubectl` to scale
  your application.
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/management/
updated_at: '2026-08-13'
created_at: '2026-08-13'
---

## Scaling your application

When load on your application grows or shrinks, use `kubectl` to scale your application.
For instance, to decrease the number of nginx replicas from 3 to 1, do:

```
kubectl scale deployment/my-nginx --replicas=1
```

```
deployment.apps/my-nginx scaled
```

Now you only have one pod managed by the deployment.

```
kubectl get pods -l app=my-nginx
```

```
NAME                        READY     STATUS    RESTARTS   AGE
my-nginx-2035384211-j5fhi   1/1       Running   0          30m
```

To have the system automatically choose the number of nginx replicas as needed,
ranging from 1 to 3, do:

```
# This requires an existing source of container and Pod metrics
kubectl autoscale deployment/my-nginx --min=1 --max=3
```

```
horizontalpodautoscaler.autoscaling/my-nginx autoscaled
```

Now your nginx replicas will be scaled up and down as needed, automatically.

For more information, please see [kubectl scale](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_scale/),
[kubectl autoscale](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_autoscale/) and
[horizontal pod autoscaler](https://kubernetes.io/docs/concepts/workloads/autoscaling/horizontal-pod-autoscale/) document.

## In-place updates of resources

Sometimes it's necessary to make narrow, non-disruptive updates to resources you've created.