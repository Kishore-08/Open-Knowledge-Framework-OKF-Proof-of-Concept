---
id: kubernetes-compositepodgroup-api-cabfab21
type: concept
title: CompositePodGroup API
description: 'FEATURE STATE:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/compositepodgroup-api/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

# CompositePodGroup API

FEATURE STATE:
`Kubernetes v1.37 [alpha]`(disabled by default)

A `CompositePodGroup` is a runtime object that represents a non-leaf node in a multi-level workload
hierarchy. While the [Workload API](https://kubernetes.io/docs/concepts/workloads/workload-api/) defines static scheduling
policy templates, `CompositePodGroup` and `PodGroup` objects are the runtime counterparts that
carry policies and hierarchy references for a specific workload instance.