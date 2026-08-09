---
id: kubernetes-protect-system-critical-daemons-for-i-o-latency-9edb5061
type: concept
title: Protect system-critical daemons for I/O latency
description: Swap can increase the I/O load on a node.
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/cluster-administration/swap-memory-management/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Protect system-critical daemons for I/O latency

Swap can increase the I/O load on a node.
When memory pressure causes the kernel to rapidly swap pages in and out,
system-critical daemons and services that rely on I/O operations may
experience performance degradation.

To mitigate this, it is recommended for systemd users to prioritize the system slice in terms of I/O latency.
For non-systemd users,
setting up a dedicated cgroup for system daemons and processes and prioritizing I/O latency in the same way is advised.
This can be achieved by setting `io.latency` for the system slice,
thereby granting it higher I/O priority.
See [cgroup's documentation](https://www.kernel.org/doc/Documentation/admin-guide/cgroup-v2.rst) for more info.