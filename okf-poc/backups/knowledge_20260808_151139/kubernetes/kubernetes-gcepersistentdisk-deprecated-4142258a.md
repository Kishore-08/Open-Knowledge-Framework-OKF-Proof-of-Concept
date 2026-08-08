---
id: kubernetes-gcepersistentdisk-deprecated-4142258a
type: concept
title: gcePersistentDisk (deprecated)
description: In Kubernetes 1.36, all operations for the in-tree `gcePersistentDisk`
  type
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/storage/volumes/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### gcePersistentDisk (deprecated)

In Kubernetes 1.36, all operations for the in-tree `gcePersistentDisk` type
are redirected to the `pd.csi.storage.gke.io` [CSI](https://kubernetes.io/docs/concepts/storage/volumes/#csi "The Container Storage Interface (CSI) defines a standard interface to expose storage systems to containers.") driver.

The `gcePersistentDisk` in-tree storage driver was deprecated in the Kubernetes v1.17 release
and then removed entirely in the v1.28 release.

The Kubernetes project suggests that you use the
[Google Compute Engine Persistent Disk CSI](https://github.com/kubernetes-sigs/gcp-compute-persistent-disk-csi-driver)
third party storage driver instead.