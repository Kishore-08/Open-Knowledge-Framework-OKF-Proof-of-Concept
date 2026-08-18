---
id: kubernetes-autoscaling-workloads-3fee6faa
type: concept
title: Autoscaling Workloads
description: With autoscaling, you can automatically update your workloads in one
  way or another. This allows your cluster to react to changes in resource demand
  more elastically and efficiently.
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/autoscaling/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

# Autoscaling Workloads

With autoscaling, you can automatically update your workloads in one way or another. This allows your cluster to react to changes in resource demand more elastically and efficiently.

In Kubernetes, you can *scale* a workload depending on the current demand of resources.
This allows your cluster to react to changes in resource demand more elastically and efficiently.

When you scale a workload, you can either increase or decrease the number of replicas managed by
the workload, or adjust the resources available to the replicas in-place.

The first approach is referred to as *horizontal scaling*, while the second is referred to as
*vertical scaling*.

There are manual and automatic ways to scale your workloads, depending on your use case.