---
id: kubernetes-iscsi-4142258a
type: concept
title: iscsi
description: An `iscsi` volume allows an existing iSCSI (SCSI over IP) volume to be
  mounted
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/storage/volumes/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### iscsi

An `iscsi` volume allows an existing iSCSI (SCSI over IP) volume to be mounted
into your Pod. Unlike `emptyDir`, which is erased when a Pod is removed, the
contents of an `iscsi` volume are preserved, and the volume is merely
unmounted. This means that an iscsi volume can be pre-populated with data, and
that data can be shared between Pods.

#### Note:

You must have your own iSCSI server running with the volume created before you can use it.

A feature of iSCSI is that it can be mounted as read-only by multiple consumers
simultaneously. This means that you can pre-populate a volume with your dataset
and then serve it in parallel from as many Pods as you need. Unfortunately,
iSCSI volumes can only be mounted by a single consumer in read-write mode.
Simultaneous writers are not allowed.