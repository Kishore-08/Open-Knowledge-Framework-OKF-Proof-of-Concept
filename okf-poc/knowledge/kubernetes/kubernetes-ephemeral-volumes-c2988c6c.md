---
id: kubernetes-ephemeral-volumes-c2988c6c
type: concept
title: Ephemeral Volumes
description: This document describes *ephemeral volumes* in Kubernetes. Familiarity
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/storage/ephemeral-volumes/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

# Ephemeral Volumes

This document describes *ephemeral volumes* in Kubernetes. Familiarity
with [volumes](https://kubernetes.io/docs/concepts/storage/volumes/) is suggested, in
particular PersistentVolumeClaim and PersistentVolume.

Some applications need additional storage but don't care whether that
data is stored persistently across restarts. For example, caching
services are often limited by memory size and can move infrequently
used data into storage that is slower than memory with little impact
on overall performance.

Other applications expect some read-only input data to be present in
files, like configuration data or secret keys.

*Ephemeral volumes* are designed for these use cases. Because volumes
follow the Pod's lifetime and get created and deleted along with the
Pod, Pods can be stopped and restarted without being limited to where
some persistent volume is available.

Ephemeral volumes are specified *inline* in the Pod spec, which
simplifies application deployment and management.