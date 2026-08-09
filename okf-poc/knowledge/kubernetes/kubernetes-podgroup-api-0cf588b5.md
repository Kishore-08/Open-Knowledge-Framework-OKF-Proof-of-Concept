---
id: kubernetes-podgroup-api-0cf588b5
type: concept
title: PodGroup API
description: 'FEATURE STATE:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/podgroup-api/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

# PodGroup API

FEATURE STATE:
`Kubernetes v1.35 [alpha]`(disabled by default)

A PodGroup is a runtime object that represents a group of Pods scheduled together as a single unit.
While the [Workload API](https://kubernetes.io/docs/concepts/workloads/workload-api/) defines scheduling policy
templates, PodGroups are the runtime counterparts that carry both the policy and the scheduling status
for a specific instance of that group.