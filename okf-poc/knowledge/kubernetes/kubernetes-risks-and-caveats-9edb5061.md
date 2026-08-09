---
id: kubernetes-risks-and-caveats-9edb5061
type: concept
title: Risks and caveats
description: It is deeply encouraged to encrypt the swap space.
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/cluster-administration/swap-memory-management/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

## Risks and caveats

#### Caution:

It is deeply encouraged to encrypt the swap space.
See Memory-backed volumes [memory-backed volumes](https://kubernetes.io/docs/concepts/cluster-administration/swap-memory-management/#memory-backed-volumes) for more info.

Having swap available on a system reduces predictability.
While swap can enhance performance by making more RAM available, swapping data
back to memory is a heavy operation, sometimes slower by many orders of magnitude,
which can cause unexpected performance regressions.
Furthermore, swap changes a system's behaviour under memory pressure.
Enabling swap increases the risk of noisy neighbors,
where Pods that frequently use their RAM may cause other Pods to swap.
In addition, since swap allows for greater memory usage for workloads in Kubernetes that cannot be predictably accounted for,
and due to unexpected packing configurations,
the scheduler currently does not account for swap memory usage.
This heightens the risk of noisy neighbors.

The performance of a node with swap memory enabled depends on the underlying physical storage.
When swap memory is in use, performance will be significantly worse in an I/O
operations per second (IOPS) constrained environment, such as a cloud VM with
I/O throttling, when compared to faster storage mediums like solid-state drives
or NVMe.
As swap might cause IO pressure, it is recommended to give a higher IO latency
priority to system critical daemons. See the relevant section in the
[recommended practices](https://kubernetes.io/docs/concepts/cluster-administration/swap-memory-management/#good-practice-for-using-swap-in-a-kubernetes-cluster) section below.