---
id: kubernetes-path-segment-names-1fac7624
type: concept
title: Path Segment Names
description: Some resource types require their names to be able to be safely encoded
  as a
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Path Segment Names

Some resource types require their names to be able to be safely encoded as a
path segment. In other words, the name may not be "." or ".." and the name may
not contain "/" or "%".

Here's an example manifest for a Pod named `nginx-demo`.

```
apiVersion: v1
kind: Pod
metadata:
  name: nginx-demo
spec:
  containers:
  - name: nginx
    image: nginx:1.14.2
    ports:
    - containerPort: 80
```

#### Note:

Some resource types have additional restrictions on their names.