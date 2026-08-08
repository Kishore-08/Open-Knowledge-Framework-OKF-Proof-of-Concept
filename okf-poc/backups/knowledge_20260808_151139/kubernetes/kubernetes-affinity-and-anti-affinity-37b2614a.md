---
id: kubernetes-affinity-and-anti-affinity-37b2614a
type: concept
title: Affinity and anti-affinity
description: '`nodeSelector` is the simplest way to constrain Pods to nodes with specific'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

## Affinity and anti-affinity

`nodeSelector` is the simplest way to constrain Pods to nodes with specific
labels. Affinity and anti-affinity expand the types of constraints you can
define. Some of the benefits of affinity and anti-affinity include:

- The affinity/anti-affinity language is more expressive. `nodeSelector` only
  selects nodes with all the specified labels. Affinity/anti-affinity gives you
  more control over the selection logic.
- You can indicate that a rule is *soft* or *preferred*, so that the scheduler
  still schedules the Pod even if it can't find a matching node.
- You can constrain a Pod using labels on other Pods running on the node (or other topological domain),
  instead of just node labels, which allows you to define rules for which Pods
  can be co-located on a node.

The affinity feature consists of two types of affinity:

- *Node affinity* functions like the `nodeSelector` field but is more expressive and
  allows you to specify soft rules.
- *Inter-pod affinity/anti-affinity* allows you to constrain Pods against labels
  on other Pods.