---
id: kubernetes-storage-classes-1915a01d
type: concept
title: Storage Classes
description: This document describes the concept of a StorageClass in Kubernetes.
  Familiarity
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/storage/storage-classes/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

# Storage Classes

This document describes the concept of a StorageClass in Kubernetes. Familiarity
with [volumes](https://kubernetes.io/docs/concepts/storage/volumes/) and
[persistent volumes](https://kubernetes.io/docs/concepts/storage/persistent-volumes/) is suggested.

A StorageClass provides a way for administrators to describe the *classes* of
storage they offer. Different classes might map to quality-of-service levels,
or to backup policies, or to arbitrary policies determined by the cluster
administrators. Kubernetes itself is unopinionated about what classes
represent.

The Kubernetes concept of a storage class is similar to “profiles” in some other
storage system designs.