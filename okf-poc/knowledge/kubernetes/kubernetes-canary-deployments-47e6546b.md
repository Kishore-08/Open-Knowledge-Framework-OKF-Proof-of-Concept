---
id: kubernetes-canary-deployments-47e6546b
type: concept
title: Canary deployments
description: Another scenario where multiple labels are needed is to distinguish deployments
  of different
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/management/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

## Canary deployments

Another scenario where multiple labels are needed is to distinguish deployments of different
releases or configurations of the same component. It is common practice to deploy a *canary* of a
new application release (specified via image tag in the pod template) side by side with the
previous release so that the new release can receive live production traffic before fully rolling
it out.

For instance, you can use a `track` label to differentiate different releases.

The primary, stable release would have a `track` label with value as `stable`:

```
name: frontend
replicas: 3
...
labels:
   app: guestbook
   tier: frontend
   track: stable
...
image: gb-frontend:v3
```

and then you can create a new release of the guestbook frontend that carries the `track` label
with different value (i.e. `canary`), so that two sets of pods would not overlap:

```
name: frontend-canary
replicas: 1
...
labels:
   app: guestbook
   tier: frontend
   track: canary
...
image: gb-frontend:v4
```

The frontend service would span both sets of replicas by selecting the common subset of their
labels (i.e. omitting the `track` label), so that the traffic will be redirected to both
applications:

```
selector:
   app: guestbook
   tier: frontend
```

You can tweak the number of replicas of the stable and canary releases to determine the ratio of
each release that will receive live production traffic (in this case, 3:1).
Once you're confident, you can update the stable track to the new application release and remove
the canary one.