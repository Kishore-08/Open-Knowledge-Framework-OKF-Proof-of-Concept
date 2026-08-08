---
id: kubernetes-reduced-container-restart-delay-3e34f258
type: concept
title: Reduced container restart delay
description: 'FEATURE STATE:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Reduced container restart delay

FEATURE STATE:
`Kubernetes v1.33 [alpha]`(disabled by default)

With the alpha feature gate `ReduceDefaultCrashLoopBackOffDecay` enabled,
container start retries across your cluster will be reduced to begin at 1s
(instead of 10s) and increase exponentially by 2x each restart until a maximum
delay of 60s (instead of 300s which is 5 minutes).

If you use this feature along with the alpha feature
`KubeletCrashLoopBackOffMax` (described below), individual nodes may have
different maximum delays.