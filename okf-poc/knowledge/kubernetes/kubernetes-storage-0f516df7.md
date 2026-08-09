---
id: kubernetes-storage-0f516df7
type: concept
title: Storage
description: Custom resources consume storage space in the same way that ConfigMaps
  do. Creating too many
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Storage

Custom resources consume storage space in the same way that ConfigMaps do. Creating too many
custom resources may overload your API server's storage space.

Custom resources are placed into storage based upon the the current storage
version of the resource, defined in the CRD spec. Any update to a custom
resource will use the currently defined storage version to store the resource.
All other versions either need to have all the fields of that version or define
conversions to work properly.

Aggregated API servers may use the same storage as the main API server, in which case the same
warning applies.