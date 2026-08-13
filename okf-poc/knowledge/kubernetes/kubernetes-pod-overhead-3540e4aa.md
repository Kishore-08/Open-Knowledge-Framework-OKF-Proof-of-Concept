---
id: kubernetes-pod-overhead-3540e4aa
type: concept
title: Pod Overhead
description: 'FEATURE STATE:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/containers/runtime-class/
updated_at: '2026-08-13'
created_at: '2026-08-13'
---

### Pod Overhead

FEATURE STATE:
`Kubernetes v1.24 [stable]`

You can specify *overhead* resources that are associated with running a Pod. Declaring overhead allows
the cluster (including the scheduler) to account for it when making decisions about Pods and resources.

Pod overhead is defined in RuntimeClass through the `overhead` field. Through the use of this field,
you can specify the overhead of running pods utilizing this RuntimeClass and ensure these overheads
are accounted for in Kubernetes.