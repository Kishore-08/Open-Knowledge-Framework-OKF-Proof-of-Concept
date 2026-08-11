---
id: kubernetes-persistentvolumeclaim-4142258a
type: concept
title: persistentVolumeClaim
description: A `persistentVolumeClaim` volume is used to mount a
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/storage/volumes/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### persistentVolumeClaim

A `persistentVolumeClaim` volume is used to mount a
[PersistentVolume](https://kubernetes.io/docs/concepts/storage/persistent-volumes/) into a Pod. PersistentVolumeClaims
are a way for users to "claim" durable storage (such as an iSCSI volume)
without knowing the details of the particular cloud environment.

See the information about [PersistentVolumes](https://kubernetes.io/docs/concepts/storage/persistent-volumes/) for more
details.