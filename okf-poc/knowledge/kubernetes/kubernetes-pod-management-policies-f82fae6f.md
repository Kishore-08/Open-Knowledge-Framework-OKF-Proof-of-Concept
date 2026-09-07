---
id: kubernetes-pod-management-policies-f82fae6f
type: concept
title: Pod Management Policies
description: StatefulSet allows you to relax its ordering guarantees while
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

### Pod Management Policies

StatefulSet allows you to relax its ordering guarantees while
preserving its uniqueness and identity guarantees via its `.spec.podManagementPolicy` field.

#### OrderedReady Pod Management

`OrderedReady` pod management is the default for StatefulSets. It implements the behavior
described in [Deployment and Scaling Guarantees](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/#deployment-and-scaling-guarantees).

#### Parallel Pod Management

`Parallel` pod management tells the StatefulSet controller to launch or
terminate all Pods in parallel, and to not wait for Pods to become Running
and Ready or completely terminated prior to launching or terminating another
Pod.

For scaling operations, this means all Pods are created or terminated simultaneously.

For rolling updates when [`.spec.updateStrategy.rollingUpdate.maxUnavailable`](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/#maximum-unavailable-pods)
is greater than 1, the StatefulSet controller terminates and creates up to `maxUnavailable` Pods
simultaneously (also known as "bursting"). This can speed up updates but may result in Pods becoming ready out of order, which might not be suitable for applications requiring strict ordering.