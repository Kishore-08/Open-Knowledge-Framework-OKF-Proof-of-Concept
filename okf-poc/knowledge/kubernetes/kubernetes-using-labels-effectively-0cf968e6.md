---
id: kubernetes-using-labels-effectively-0cf968e6
type: concept
title: Using labels effectively
description: You can apply a single label to any resources, but this is not always
  the
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

## Using labels effectively

You can apply a single label to any resources, but this is not always the
best practice. There are many scenarios where multiple labels should be used to
distinguish resource sets from one another.

For instance, different applications would use different values for the `app` label, but a
multi-tier application, such as the [guestbook example](https://github.com/kubernetes/examples/tree/master/web/guestbook/),
would additionally need to distinguish each tier.

In the following examples, the `app` label is included for convenience in manual queries
and simple CLI usage. The `app.kubernetes.io/name` label follows the recommended Kubernetes
labeling conventions and is better suited for tooling and automation.

The frontend could carry the following labels:

```
labels:
  app: guestbook
  app.kubernetes.io/name: guestbook
  tier: frontend
```

while the Redis master and replica would have different `tier` labels, and perhaps even an
additional `role` label:

```
labels:
  app: guestbook
  app.kubernetes.io/name: guestbook
  tier: backend
  role: master
```

and

```
labels:
  app: guestbook
  app.kubernetes.io/name: guestbook
  tier: backend
  role: replica
```

The labels allow for slicing and dicing the resources along any dimension specified by a label:

```
kubectl apply -f examples/guestbook/all-in-one/guestbook-all-in-one.yaml
kubectl get pods -Lapp -Ltier -Lrole
```

```
NAME                           READY  STATUS    RESTARTS   AGE   APP         TIER       ROLE
guestbook-fe-4nlpb             1/1    Running   0          1m    guestbook   frontend   <none>
guestbook-fe-ght6d             1/1    Running   0          1m    guestbook   frontend   <none>
guestbook-fe-jpy62             1/1    Running   0          1m    guestbook   frontend   <none>
guestbook-redis-master-5pg3b   1/1    Running   0          1m    guestbook   backend    master
guestbook-redis-replica-2q2yf  1/1    Running   0          1m    guestbook   backend    replica
guestbook-redis-replica-qgazl  1/1    Running   0          1m    guestbook   backend    replica
my-nginx-divi2                 1/1    Running   0          29m   nginx       <none>     <none>
my-nginx-o0ef1                 1/1    Running   0          29m   nginx       <none>     <none>
```

```
kubectl get pods -lapp=guestbook,role=replica
```

```
NAME                           READY  STATUS   RESTARTS  AGE
guestbook-redis-replica-2q2yf  1/1    Running  0         3m
guestbook-redis-replica-qgazl  1/1    Running  0         3m
```