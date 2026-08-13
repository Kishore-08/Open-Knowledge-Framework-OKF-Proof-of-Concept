---
id: kubernetes-dynamic-volume-provisioning-50610b7d
type: concept
title: Dynamic Volume Provisioning
description: Dynamic volume provisioning allows storage volumes to be created on-demand.
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/storage/dynamic-provisioning/
updated_at: '2026-08-13'
created_at: '2026-08-13'
---

# Dynamic Volume Provisioning

Dynamic volume provisioning allows storage volumes to be created on-demand.
Without dynamic provisioning, cluster administrators have to manually make
calls to their cloud or storage provider to create new storage volumes, and
then create [`PersistentVolume` objects](https://kubernetes.io/docs/concepts/storage/persistent-volumes/)
to represent them in Kubernetes. The dynamic provisioning feature eliminates
the need for cluster administrators to pre-provision storage. Instead, it
automatically provisions storage when users create
[`PersistentVolumeClaim` objects](https://kubernetes.io/docs/concepts/storage/persistent-volumes/).