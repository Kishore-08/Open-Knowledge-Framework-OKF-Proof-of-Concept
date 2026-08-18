---
id: kubernetes-list-and-watch-filtering-0cf968e6
type: concept
title: LIST and WATCH filtering
description: For **list** and **watch** operations, you can specify label selectors
  to filter the sets of objects
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

### LIST and WATCH filtering

For **list** and **watch** operations, you can specify label selectors to filter the sets of objects
returned; you specify the filter using a query parameter.
(To learn in detail about watches in Kubernetes, read
[efficient detection of changes](https://kubernetes.io/docs/reference/using-api/api-concepts/#efficient-detection-of-changes)).
Both requirements are permitted
(presented here as they would appear in a URL query string):

- *equality-based* requirements: `?labelSelector=environment%3Dproduction,tier%3Dfrontend`
- *set-based* requirements: `?labelSelector=environment+in+%28production%2Cqa%29%2Ctier+in+%28frontend%29`

Both label selector styles can be used to list or watch resources via a REST client.
For example, targeting `apiserver` with `kubectl` and using *equality-based* one may write:

```
kubectl get pods -l environment=production,tier=frontend
```

or using *set-based* requirements:

```
kubectl get pods -l 'environment in (production),tier in (frontend)'
```

As already mentioned *set-based* requirements are more expressive.
For instance, they can implement the *OR* operator on values:

```
kubectl get pods -l 'environment in (production, qa)'
```

or restricting negative matching via *notin* operator:

```
kubectl get pods -l 'environment,environment notin (frontend)'
```