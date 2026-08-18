---
id: kubernetes-observability-d96e2651
type: concept
title: Observability
description: The metric `scheduler_pending_pods` comes with a new label `"gated"`
  to distinguish whether a Pod
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/scheduling-eviction/pod-scheduling-readiness/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

## Observability

The metric `scheduler_pending_pods` comes with a new label `"gated"` to distinguish whether a Pod
has been tried scheduling but claimed as unschedulable, or explicitly marked as not ready for
scheduling. You can use `scheduler_pending_pods{queue="gated"}` to check the metric result.