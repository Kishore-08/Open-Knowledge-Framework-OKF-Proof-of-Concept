---
id: kubernetes-disable-swap-for-system-critical-daemons-9edb5061
type: concept
title: Disable swap for system-critical daemons
description: During the testing phase and based on user feedback, it was observed
  that the performance
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/cluster-administration/swap-memory-management/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Disable swap for system-critical daemons

During the testing phase and based on user feedback, it was observed that the performance
of system-critical daemons and services might degrade.
This implies that system daemons, including the kubelet, could operate slower than usual.
If this issue is encountered, it is advisable to configure the cgroup of the system slice
to prevent swapping (i.e., set `memory.swap.max=0`).