---
id: kubernetes-parameters-1915a01d
type: concept
title: Parameters
description: StorageClasses have parameters that describe volumes belonging to the
  storage
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/storage/storage-classes/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

## Parameters

StorageClasses have parameters that describe volumes belonging to the storage
class. Different parameters may be accepted depending on the `provisioner`.
When a parameter is omitted, some default is used.

There can be at most 512 parameters defined for a StorageClass.
The total length of the parameters object including its keys and values cannot
exceed 256 KiB.