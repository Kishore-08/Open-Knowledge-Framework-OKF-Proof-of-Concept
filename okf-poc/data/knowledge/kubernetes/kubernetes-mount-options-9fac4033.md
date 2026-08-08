---
id: kubernetes-mount-options-9fac4033
type: concept
title: Mount Options
description: A Kubernetes administrator can specify additional mount options for when
  a
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/storage/persistent-volumes/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Mount Options

A Kubernetes administrator can specify additional mount options for when a
Persistent Volume is mounted on a node.

#### Note:

Not all Persistent Volume types support mount options.

The following volume types support mount options:

- `csi` (including CSI migrated volume types)
- `iscsi`
- `nfs`

Mount options are not validated. If a mount option is invalid, the mount fails.

In the past, the annotation `volume.beta.kubernetes.io/mount-options` was used instead
of the `mountOptions` attribute. This annotation is still working; however,
it will become fully deprecated in a future Kubernetes release.