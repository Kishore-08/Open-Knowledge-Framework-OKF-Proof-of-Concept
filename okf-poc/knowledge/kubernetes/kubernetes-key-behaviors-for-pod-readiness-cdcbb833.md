---
id: kubernetes-key-behaviors-for-pod-readiness-cdcbb833
type: concept
title: Key behaviors for pod readiness
description: '- If a Pod is `Ready` and remains `Ready`, it can be counted as contributing
  metrics even within the delay.'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/autoscaling/horizontal-pod-autoscale/
updated_at: '2026-08-13'
created_at: '2026-08-13'
---

### Key behaviors for pod readiness

- If a Pod is `Ready` and remains `Ready`, it can be counted as contributing metrics even within the delay.
- If a Pod rapidly toggles between `Ready` and `Unready`, metrics are ignored until it’s considered stably `Ready`.