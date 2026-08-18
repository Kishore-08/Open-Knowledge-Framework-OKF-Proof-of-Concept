---
id: kubernetes-scaling-workloads-horizontally-3fee6faa
type: concept
title: Scaling workloads horizontally
description: In Kubernetes, you can automatically scale a workload horizontally using
  a [HorizontalPodAutoscaler](https://kubernetes.io/docs/concepts/workloads/autoscaling/horizontal-pod-autoscale/)
  (HPA).
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/autoscaling/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

### Scaling workloads horizontally

In Kubernetes, you can automatically scale a workload horizontally using a [HorizontalPodAutoscaler](https://kubernetes.io/docs/concepts/workloads/autoscaling/horizontal-pod-autoscale/) (HPA).

It is implemented as a Kubernetes API resource and a [controller](https://kubernetes.io/docs/concepts/architecture/controller/ "A control loop that watches the shared state of the cluster through the apiserver and makes changes attempting to move the current state towards the desired state.")
and periodically adjusts the number of [replicas](https://kubernetes.io/docs/reference/glossary/?all=true#term-replica "Replicas are copies of pods, ensuring availability, scalability, and fault tolerance by maintaining identical instances.")
in a workload to match observed resource utilization such as CPU or memory usage.

There is a [walkthrough tutorial](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale-walkthrough/) of configuring a HorizontalPodAutoscaler for a Deployment.