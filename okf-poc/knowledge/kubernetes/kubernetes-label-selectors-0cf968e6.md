---
id: kubernetes-label-selectors-0cf968e6
type: concept
title: Label selectors
description: Unlike [names and UIDs](https://kubernetes.io/docs/concepts/overview/working-with-objects/names/),
  labels
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

## Label selectors

Unlike [names and UIDs](https://kubernetes.io/docs/concepts/overview/working-with-objects/names/), labels
do not provide uniqueness. In general, we expect many objects to carry the same label(s).

Via a *label selector*, the client/user can identify a set of objects.
The label selector is the core grouping primitive in Kubernetes.

The API currently supports two types of selectors: *equality-based* and *set-based*.
A label selector can be made of multiple *requirements* which are comma-separated.
In the case of multiple requirements, all must be satisfied so the comma separator
acts as a logical *AND* (`&&`) operator.

The semantics of empty or non-specified selectors are dependent on the context,
and API types that use selectors should document the validity and meaning of
them.

#### Note:

For some API types, such as ReplicaSets, the label selectors of two instances must
not overlap within a namespace, or the controller can see that as conflicting
instructions and fail to determine how many replicas should be present.

#### Caution:

For both equality-based and set-based conditions there is no logical *OR* (`||`) operator.
Ensure your filter statements are structured accordingly.