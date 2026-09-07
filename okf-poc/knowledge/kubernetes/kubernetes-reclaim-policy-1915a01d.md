---
id: kubernetes-reclaim-policy-1915a01d
type: concept
title: Reclaim policy
description: PersistentVolumes that are dynamically created by a StorageClass will
  have the
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/storage/storage-classes/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

## Reclaim policy

PersistentVolumes that are dynamically created by a StorageClass will have the
[reclaim policy](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#reclaiming)
specified in the `reclaimPolicy` field of the class, which can be
either `Delete` or `Retain`. If no `reclaimPolicy` is specified when a
StorageClass object is created, it will default to `Delete`.

PersistentVolumes that are created manually and managed via a StorageClass will have
whatever reclaim policy they were assigned at creation.