---
id: kubernetes-updating-your-application-without-an-outage-47e6546b
type: concept
title: Updating your application without an outage
description: At some point, you'll eventually need to update your deployed application,
  typically by specifying
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/management/
updated_at: '2026-08-13'
created_at: '2026-08-13'
---

## Updating your application without an outage

At some point, you'll eventually need to update your deployed application, typically by specifying
a new image or image tag. `kubectl` supports several update operations, each of which is applicable
to different scenarios.

You can run multiple copies of your app, and use a *rollout* to gradually shift the traffic to
new healthy Pods. Eventually, all the running Pods would have the new software.

This section of the page guides you through how to create and update applications with Deployments.

Let's say you were running version 1.14.2 of nginx:

```
kubectl create deployment my-nginx --image=nginx:1.14.2
```

```
deployment.apps/my-nginx created
```

Ensure that there is 1 replica:

```
kubectl scale --replicas 1 deployments/my-nginx --subresource='scale' --type='merge' -p '{"spec":{"replicas": 1}}'
```

```
deployment.apps/my-nginx scaled
```

and allow Kubernetes to add more temporary replicas during a rollout, by setting a *surge maximum* of
100%:

```
kubectl patch --type='merge' -p '{"spec":{"strategy":{"rollingUpdate":{"maxSurge": "100%" }}}}'
```

```
deployment.apps/my-nginx patched
```

To update to version 1.16.1, change `.spec.template.spec.containers[0].image` from `nginx:1.14.2`
to `nginx:1.16.1` using `kubectl edit`:

```
kubectl edit deployment/my-nginx
# Change the manifest to use the newer container image, then save your changes
```

That's it! The Deployment will declaratively update the deployed nginx application progressively
behind the scene. It ensures that only a certain number of old replicas may be down while they are
being updated, and only a certain number of new replicas may be created above the desired number
of pods. To learn more details about how this happens,
visit [Deployment](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/).

You can use rollouts with DaemonSets, Deployments, or StatefulSets.