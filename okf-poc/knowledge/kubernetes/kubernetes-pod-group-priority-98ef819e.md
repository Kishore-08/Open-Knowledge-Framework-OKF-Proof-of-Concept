---
id: kubernetes-pod-group-priority-98ef819e
type: concept
title: Pod group priority
description: PodGroup uses the same concept of [PriorityClass](https://kubernetes.io/docs/concepts/scheduling-eviction/pod-priority-preemption/#priorityclass)
  as single Pods.
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/workload-api/disruption-and-priority/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

## Pod group priority

PodGroup uses the same concept of [PriorityClass](https://kubernetes.io/docs/concepts/scheduling-eviction/pod-priority-preemption/#priorityclass) as single Pods.
Once you have created one or more PriorityClasses,
you can create a PodGroup that specifies one of those PriorityClass names in its specification.
The priority admission controller uses the `priorityClassName` field and populates the integer value of the priority.
If the priority class is not found, the PodGroup is rejected.
When `priorityClassName` is not set for a PodGroup, Kubernetes looks for a default (a PriorityClass with `globalDefault` set true)
If there is no PriorityClass with `globalDefault` set true, a PodGroup with no `priorityClassName` has priority zero.

The priority of the PodGroup is an authoritative priority for all pods in the group during [workload-aware preemption](https://kubernetes.io/docs/concepts/scheduling-eviction/workload-aware-preemption/) events.
This value is also used for the ordering of PodGroups in the scheduling queue.
When the priorities of individual pods forming this PodGroup differ from PodGroup priority
the PodGroup will not be scheduled with `all pods in a single pod group should have the same priority as the pod group` error.

When the [PodGroupPreemptionPolicy](https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/podgroup-preemption-policy/)
feature gate is enabled, PodGroup has also `preemptionPolicy` field. This field is also taken from the PriorirtyClass.
It is an authoratitive field for all pods in the group and it decides whether the PodGroup can perform a preemption of
lower priority pods and pod groups to accomodate a place for itself. When the feature gate is enabled all pods in the PodGroup
must have the same `preemptionPolicy` as PodGroup. Otherwise the PodGroup will not be scheduled with
`all pods in a single pod group should have the same preemption policy as the pod group's preemption policy` error.
When PodGroup has `preemptionPolicy: Never` it will not perform workload aware preemption.
If the feature flag is disabled, all pods forming PodGroup must have the same `preemptionPolicy`.
Otherwise the PodGroup will not be scheduled with
`all pods in a single pod group should have the same preemption policy` error.

The following YAML is an example of a PodGroup configuration that uses the `high-priority` PriorityClass,
which maps to the integer priority value of 1000000.
The priority admission controller checks the specification and resolves the priority of the PodGroup to 1000000.

```
apiVersion: scheduling.k8s.io/v1beta1
kind: PodGroup
metadata:
  namespace: ns-1
  name: job-1
spec:
  priorityClassName: high-priority
```