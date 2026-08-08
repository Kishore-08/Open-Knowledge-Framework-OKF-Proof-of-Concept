---
id: kubernetes-podgroup-scheduling-policies-217a0ad5
type: concept
title: PodGroup Scheduling Policies
description: 'FEATURE STATE:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/workload-api/policies/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

# PodGroup Scheduling Policies

FEATURE STATE:
`Kubernetes v1.35 [alpha]`(disabled by default)

Every [PodGroup](https://kubernetes.io/docs/concepts/workloads/podgroup-api/) must declare a scheduling policy
in its `spec.schedulingPolicy` field. This policy dictates how the scheduler treats the
collection of Pods in the group.

## Policy types

The `schedulingPolicy` field supports two policy types: `basic` and `gang`.
You must specify exactly one.