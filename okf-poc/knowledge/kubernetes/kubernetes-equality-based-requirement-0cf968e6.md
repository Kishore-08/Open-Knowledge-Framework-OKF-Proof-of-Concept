---
id: kubernetes-equality-based-requirement-0cf968e6
type: concept
title: '*Equality-based* requirement'
description: '*Equality-* or *inequality-based* requirements allow filtering by label
  keys and values.'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

### *Equality-based* requirement

*Equality-* or *inequality-based* requirements allow filtering by label keys and values.
Matching objects must satisfy all of the specified label constraints, though they may
have additional labels as well. Three kinds of operators are admitted `=`,`==`,`!=`.
The first two represent *equality* (and are synonyms), while the latter represents *inequality*.
For example:

```
environment = production
tier != frontend
```

The former selects all resources with key equal to `environment` and value equal to `production`.
The latter selects all resources with key equal to `tier` and value distinct from `frontend`,
and all resources with no labels with the `tier` key. One could filter for resources in `production`
excluding `frontend` using the comma operator: `environment=production,tier!=frontend`

One usage scenario for equality-based label requirement is for Pods to specify
node selection criteria. For example, the sample Pod below selects nodes where
the `accelerator` label exists and is set to `nvidia-tesla-p100`.

```
apiVersion: v1
kind: Pod
metadata:
  name: cuda-test
spec:
  containers:
    - name: cuda-test
      image: "registry.k8s.io/cuda-vector-add:v0.1"
      resources:
        limits:
          nvidia.com/gpu: 1
  nodeSelector:
    accelerator: nvidia-tesla-p100
```