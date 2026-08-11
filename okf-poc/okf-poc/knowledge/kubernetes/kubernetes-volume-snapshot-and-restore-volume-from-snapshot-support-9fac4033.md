---
id: kubernetes-volume-snapshot-and-restore-volume-from-snapshot-support-9fac4033
type: concept
title: Volume Snapshot and Restore Volume from Snapshot Support
description: 'FEATURE STATE:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/storage/persistent-volumes/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

## Volume Snapshot and Restore Volume from Snapshot Support

FEATURE STATE:
`Kubernetes v1.20 [stable]`

Volume snapshots only support the out-of-tree CSI volume plugins.
For details, see [Volume Snapshots](https://kubernetes.io/docs/concepts/storage/volume-snapshots/).
In-tree volume plugins are deprecated. You can read about the deprecated volume
plugins in the
[Volume Plugin FAQ](https://github.com/kubernetes/community/blob/main/sig-storage/volume-plugin-faq.md).