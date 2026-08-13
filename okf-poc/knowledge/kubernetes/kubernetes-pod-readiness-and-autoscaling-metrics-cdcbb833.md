---
id: kubernetes-pod-readiness-and-autoscaling-metrics-cdcbb833
type: concept
title: Pod readiness and autoscaling metrics
description: 'The HorizontalPodAutoscaler (HPA) controller includes two command line
  options that influence how CPU metrics are collected from Pods during startup:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/autoscaling/horizontal-pod-autoscale/
updated_at: '2026-08-13'
created_at: '2026-08-13'
---

## Pod readiness and autoscaling metrics

The HorizontalPodAutoscaler (HPA) controller includes two command line options that influence how CPU metrics are collected from Pods during startup:

1. `--horizontal-pod-autoscaler-cpu-initialization-period` (default: 5 minutes)

This defines the time window after a Pod starts during which its **CPU usage is ignored** unless:
- The Pod is in a `Ready` state **and**
- The metric sample was taken entirely during the period it was `Ready`.

This command line option helps **exclude misleading high CPU usage** from initializing Pods (for example: Java apps warming up) in HPA scaling decisions.

1. `--horizontal-pod-autoscaler-initial-readiness-delay` (default: 30 seconds)

This defines a short delay period after a Pod starts during which the HPA controller treats Pods that are currently `Unready` as still initializing, **even if they have previously transitioned to `Ready` briefly**.

It is designed to:
- Avoid including Pods that rapidly fluctuate between `Ready` and `Unready` during startup.
- Ensure stability in the initial readiness signal before HPA considers their metrics valid.

You can only set these command line options cluster-wide.