---
id: kubernetes-a-note-on-namespaces-9fac4033
type: concept
title: A Note on Namespaces
description: PersistentVolumes binds are exclusive, and since PersistentVolumeClaims
  are
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/storage/persistent-volumes/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### A Note on Namespaces

PersistentVolumes binds are exclusive, and since PersistentVolumeClaims are
namespaced objects, mounting claims with "Many" modes (`ROX`, `RWX`) is only
possible within one namespace.