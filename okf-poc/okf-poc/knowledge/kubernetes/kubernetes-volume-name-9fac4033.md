---
id: kubernetes-volume-name-9fac4033
type: concept
title: Volume Name
description: Claims can use the `volumeName` field to explicitly bind to a specific
  PersistentVolume. You can also leave
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/storage/persistent-volumes/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Volume Name

Claims can use the `volumeName` field to explicitly bind to a specific PersistentVolume. You can also leave
`volumeName` unset, indicating that you'd like Kubernetes to set up a new PersistentVolume
that matches the claim.
If the specified PV is already bound to another PVC, the binding will be stuck
in a pending state.