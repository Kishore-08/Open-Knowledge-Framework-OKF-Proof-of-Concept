---
id: kubernetes-mount-options-1915a01d
type: concept
title: Mount options
description: PersistentVolumes that are dynamically created by a StorageClass will
  have the
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/storage/storage-classes/
updated_at: '2026-08-13'
created_at: '2026-08-13'
---

## Mount options

PersistentVolumes that are dynamically created by a StorageClass will have the
mount options specified in the `mountOptions` field of the class.

If the volume plugin does not support mount options but mount options are
specified, provisioning will fail. Mount options are **not** validated on either
the class or PV. If a mount option is invalid, the PV mount fails.