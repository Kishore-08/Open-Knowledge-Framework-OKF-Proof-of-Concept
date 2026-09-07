---
id: kubernetes-comparison-with-podaffinity-and-podantiaffinity-4f7e995f
type: concept
title: Comparison with podAffinity and podAntiAffinity
description: In Kubernetes, [inter-Pod affinity and anti-affinity](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#inter-pod-affinity-and-anti-affinity)
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/scheduling-eviction/topology-spread-constraints/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

## Comparison with podAffinity and podAntiAffinity

In Kubernetes, [inter-Pod affinity and anti-affinity](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#inter-pod-affinity-and-anti-affinity)
control how Pods are scheduled in relation to one another - either more packed
or more scattered.

`podAffinity`
:   attracts Pods; you can try to pack any number of Pods into qualifying
    topology domain(s).

`podAntiAffinity`
:   repels Pods. If you set this to `requiredDuringSchedulingIgnoredDuringExecution` mode then
    only a single Pod can be scheduled into a single topology domain; if you choose
    `preferredDuringSchedulingIgnoredDuringExecution` then you lose the ability to enforce the
    constraint.

For finer control, you can specify topology spread constraints to distribute
Pods across different topology domains - to achieve either high availability or
cost-saving. This can also help on rolling update workloads and scaling out
replicas smoothly.

For more context, see the
[Motivation](https://github.com/kubernetes/enhancements/tree/master/keps/sig-scheduling/895-pod-topology-spread#motivation)
section of the enhancement proposal about Pod topology spread constraints.