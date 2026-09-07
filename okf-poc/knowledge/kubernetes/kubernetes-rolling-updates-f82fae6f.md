---
id: kubernetes-rolling-updates-f82fae6f
type: concept
title: Rolling Updates
description: When a StatefulSet's `.spec.updateStrategy.type` is set to `RollingUpdate`,
  the
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

## Rolling Updates

When a StatefulSet's `.spec.updateStrategy.type` is set to `RollingUpdate`, the
StatefulSet controller will delete and recreate each Pod in the StatefulSet. It will proceed
in the same order as Pod termination (from the largest ordinal to the smallest), updating
each Pod one at a time.

The Kubernetes control plane waits until an updated Pod is Running and Ready prior
to updating its predecessor. If you have set `.spec.minReadySeconds` (see
[Minimum Ready Seconds](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/#minimum-ready-seconds)), the control plane additionally waits that
amount of time after the Pod turns ready, before moving on.