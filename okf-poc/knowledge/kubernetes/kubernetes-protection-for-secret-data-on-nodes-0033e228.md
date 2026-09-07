---
id: kubernetes-protection-for-secret-data-on-nodes-0033e228
type: concept
title: Protection for Secret data on nodes
description: On Linux nodes, memory-backed volumes (such as [`secret`](https://kubernetes.io/docs/concepts/configuration/secret/)
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/security/linux-security/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

## Protection for Secret data on nodes

On Linux nodes, memory-backed volumes (such as [`secret`](https://kubernetes.io/docs/concepts/configuration/secret/)
volume mounts, or [`emptyDir`](https://kubernetes.io/docs/concepts/storage/volumes/#emptydir) with `medium: Memory`)
are implemented with a `tmpfs` filesystem.

If you have swap configured and use an older Linux kernel (or a current kernel and an unsupported configuration of Kubernetes),
**memory** backed volumes can have data written to persistent storage.

The Linux kernel officially supports the `noswap` option from version 6.3,
therefore it is recommended the used kernel version is 6.3 or later,
or supports the `noswap` option via a backport, if swap is enabled on the node.

Read [swap memory management](https://kubernetes.io/docs/concepts/cluster-administration/swap-memory-management/#memory-backed-volumes)
for more info.