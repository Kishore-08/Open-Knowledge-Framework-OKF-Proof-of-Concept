---
id: kubernetes-volume-attributes-classes-93807cd8
type: concept
title: Volume Attributes Classes
description: 'FEATURE STATE:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/storage/volume-attributes-classes/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

# Volume Attributes Classes

FEATURE STATE:
`Kubernetes v1.36 [stable]`(enabled by default)

This page assumes that you are familiar with [StorageClasses](https://kubernetes.io/docs/concepts/storage/storage-classes/),
[volumes](https://kubernetes.io/docs/concepts/storage/volumes/) and [PersistentVolumes](https://kubernetes.io/docs/concepts/storage/persistent-volumes/)
in Kubernetes.

A VolumeAttributesClass provides a way for administrators to describe the mutable
"classes" of storage they offer. Different classes might map to different quality-of-service levels.
Kubernetes itself is un-opinionated about what these classes represent.

This feature is generally available (GA) as of version 1.34, and users have the option to disable it.

You can also only use VolumeAttributesClasses with storage backed by
[Container Storage Interface](https://kubernetes.io/docs/concepts/storage/volumes/#csi "The Container Storage Interface (CSI) defines a standard interface to expose storage systems to containers."), and only where the
relevant CSI driver implements the `ModifyVolume` API.