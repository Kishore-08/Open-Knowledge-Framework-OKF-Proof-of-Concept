---
id: kubernetes-topology-awareness-50610b7d
type: concept
title: Topology Awareness
description: In [Multi-Zone](https://kubernetes.io/docs/setup/best-practices/multiple-zones/)
  clusters, Pods can be spread across
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/storage/dynamic-provisioning/
updated_at: '2026-08-13'
created_at: '2026-08-13'
---

## Topology Awareness

In [Multi-Zone](https://kubernetes.io/docs/setup/best-practices/multiple-zones/) clusters, Pods can be spread across
Zones in a Region. Single-Zone storage backends should be provisioned in the Zones where
Pods are scheduled. This can be accomplished by setting the
[Volume Binding Mode](https://kubernetes.io/docs/concepts/storage/storage-classes/#volume-binding-mode).