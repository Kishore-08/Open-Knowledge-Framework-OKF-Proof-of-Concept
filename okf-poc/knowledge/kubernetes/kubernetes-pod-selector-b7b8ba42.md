---
id: kubernetes-pod-selector-b7b8ba42
type: concept
title: Pod Selector
description: The `.spec.selector` field is a pod selector. It works the same as the
  `.spec.selector` of
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/
updated_at: '2026-08-13'
created_at: '2026-08-13'
---

### Pod Selector

The `.spec.selector` field is a pod selector. It works the same as the `.spec.selector` of
a [Job](https://kubernetes.io/docs/concepts/workloads/controllers/job/).

You must specify a pod selector that matches the labels of the
`.spec.template`.
Also, once a DaemonSet is created,
its `.spec.selector` can not be mutated. Mutating the pod selector can lead to the
unintentional orphaning of Pods, and it was found to be confusing to users.

The `.spec.selector` is an object consisting of two fields:

- `matchLabels` - works the same as the `.spec.selector` of a
  [ReplicationController](https://kubernetes.io/docs/concepts/workloads/controllers/replicationcontroller/).
- `matchExpressions` - allows to build more sophisticated selectors by specifying key,
  list of values and an operator that relates the key and values.

When the two are specified the result is ANDed.

The `.spec.selector` must match the `.spec.template.metadata.labels`.
Config with these two not matching will be rejected by the API.