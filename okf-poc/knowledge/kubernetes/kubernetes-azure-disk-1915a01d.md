---
id: kubernetes-azure-disk-1915a01d
type: concept
title: Azure Disk
description: Kubernetes 1.36 does not include a `azureDisk` volume type.
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/storage/storage-classes/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

### Azure Disk

Kubernetes 1.36 does not include a `azureDisk` volume type.

The `azureDisk` in-tree storage driver was deprecated in the Kubernetes v1.19 release
and then removed entirely in the v1.27 release.

The Kubernetes project suggests that you use the [Azure Disk](https://github.com/kubernetes-sigs/azuredisk-csi-driver) third party
storage driver instead.