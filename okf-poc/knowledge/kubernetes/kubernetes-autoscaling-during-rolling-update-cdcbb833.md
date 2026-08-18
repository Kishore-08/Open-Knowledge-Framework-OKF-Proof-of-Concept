---
id: kubernetes-autoscaling-during-rolling-update-cdcbb833
type: concept
title: Autoscaling during rolling update
description: Kubernetes lets you perform a rolling update on a Deployment. In that
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/autoscaling/horizontal-pod-autoscale/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

## Autoscaling during rolling update

Kubernetes lets you perform a rolling update on a Deployment. In that
case, the Deployment manages the underlying ReplicaSets for you.
When you configure autoscaling for a Deployment, you bind a
HorizontalPodAutoscaler to a single Deployment. The HorizontalPodAutoscaler
manages the `replicas` field of the Deployment. The deployment controller is responsible
for setting the `replicas` of the underlying ReplicaSets so that they add up to a suitable
number during the rollout and also afterwards.

If you perform a rolling update of a StatefulSet that has an autoscaled number of
replicas, the StatefulSet directly manages its set of Pods (there is no intermediate resource
similar to ReplicaSet).