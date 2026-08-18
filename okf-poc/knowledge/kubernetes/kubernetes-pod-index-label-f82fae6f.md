---
id: kubernetes-pod-index-label-f82fae6f
type: concept
title: Pod index label
description: 'FEATURE STATE:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

### Pod index label

FEATURE STATE:
`Kubernetes v1.32 [stable]`(enabled by default)

When the StatefulSet [controller](https://kubernetes.io/docs/concepts/architecture/controller/ "A control loop that watches the shared state of the cluster through the apiserver and makes changes attempting to move the current state towards the desired state.") creates a Pod,
the new Pod is labelled with `apps.kubernetes.io/pod-index`. The value of this label is the ordinal index of
the Pod. This label allows you to route traffic to a particular pod index, filter logs/metrics
using the pod index label, and more. Note the feature gate `PodIndexLabel` is enabled and locked by default for this
feature, in order to disable it, users will have to use server emulated version v1.31.