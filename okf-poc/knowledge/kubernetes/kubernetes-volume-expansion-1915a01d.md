---
id: kubernetes-volume-expansion-1915a01d
type: concept
title: Volume expansion
description: PersistentVolumes can be configured to be expandable. This allows you
  to resize the
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/storage/storage-classes/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

## Volume expansion

PersistentVolumes can be configured to be expandable. This allows you to resize the
volume by editing the corresponding PVC object, requesting a new larger amount of
storage.

The following types of volumes support volume expansion, when the underlying
StorageClass has the field `allowVolumeExpansion` set to true.

Table of Volume types and the version of Kubernetes they require

| Volume type | Required Kubernetes version for volume expansion |
| --- | --- |
| Azure File | 1.11 |
| CSI | 1.24 |
| FlexVolume | 1.13 |
| Portworx | 1.11 |
| rbd | 1.11 |

#### Note:

You can only use the volume expansion feature to grow a Volume, not to shrink it.