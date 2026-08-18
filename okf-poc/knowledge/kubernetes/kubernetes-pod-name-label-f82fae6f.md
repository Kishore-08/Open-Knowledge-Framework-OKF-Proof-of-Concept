---
id: kubernetes-pod-name-label-f82fae6f
type: concept
title: Pod Name Label
description: When the StatefulSet [controller](https://kubernetes.io/docs/concepts/architecture/controller/
  "A control loop that watches the shared state of the cluster through the apiserver
  and makes changes atte
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

### Pod Name Label

When the StatefulSet [controller](https://kubernetes.io/docs/concepts/architecture/controller/ "A control loop that watches the shared state of the cluster through the apiserver and makes changes attempting to move the current state towards the desired state.") creates a Pod,
it adds a label, `statefulset.kubernetes.io/pod-name`, that is set to the name of
the Pod. This label allows you to attach a Service to a specific Pod in
the StatefulSet.