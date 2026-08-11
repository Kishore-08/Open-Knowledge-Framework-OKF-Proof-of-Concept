---
id: kubernetes-kube-controller-manager-lock-release-on-exit-4557d362
type: concept
title: Kube controller manager lock release on exit
description: 'FEATURE STATE:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/architecture/leases/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Kube controller manager lock release on exit

FEATURE STATE:
`Kubernetes v1.36 [alpha]`(disabled by default)

When the `ControllerManagerReleaseLeaderElectionLockOnExit` feature gate is enabled,
the `kube-controller-manager` actively releases its leader election lock during
leader transitions, rather than waiting for the lock's TTL to expire. This allows
a new leader to be elected more quickly, reducing leader transition latency.