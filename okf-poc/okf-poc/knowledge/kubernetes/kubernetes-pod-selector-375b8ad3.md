---
id: kubernetes-pod-selector-375b8ad3
type: concept
title: Pod Selector
description: The `.spec.selector` field is a [label selector](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/).
  As discussed
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/controllers/replicaset/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Pod Selector

The `.spec.selector` field is a [label selector](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/). As discussed
[earlier](https://kubernetes.io/docs/concepts/workloads/controllers/replicaset/#how-a-replicaset-works) these are the labels used to identify potential Pods to acquire. In our
`frontend.yaml` example, the selector was:

```
matchLabels:
  tier: frontend
```

In the ReplicaSet, `.spec.template.metadata.labels` must match `spec.selector`, or it will
be rejected by the API.

#### Note:

For 2 ReplicaSets specifying the same `.spec.selector` but different
`.spec.template.metadata.labels` and `.spec.template.spec` fields, each ReplicaSet ignores the
Pods created by the other ReplicaSet.