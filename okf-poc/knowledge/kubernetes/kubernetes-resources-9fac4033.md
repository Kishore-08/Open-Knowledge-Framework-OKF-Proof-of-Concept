---
id: kubernetes-resources-9fac4033
type: concept
title: Resources
description: Claims, like Pods, can request specific quantities of a resource. In
  this case,
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/storage/persistent-volumes/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Resources

Claims, like Pods, can request specific quantities of a resource. In this case,
the request is for storage. The same
[resource model](https://git.k8s.io/design-proposals-archive/scheduling/resources.md)
applies to both volumes and claims.

#### Note:

For `Filesystem` volumes, the storage request refers to the "outer" volume size
(i.e. the allocated size from the storage backend).
This means that the writeable size may be slightly lower for providers that
build a filesystem on top of a block device, due to filesystem overhead.
This is especially visible with XFS, where many metadata features are enabled by default.