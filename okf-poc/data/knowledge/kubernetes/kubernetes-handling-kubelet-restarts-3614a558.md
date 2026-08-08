---
id: kubernetes-handling-kubelet-restarts-3614a558
type: concept
title: Handling kubelet restarts
description: A device plugin is expected to detect kubelet restarts and re-register
  itself with the new
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/extend-kubernetes/compute-storage-net/device-plugins/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Handling kubelet restarts

A device plugin is expected to detect kubelet restarts and re-register itself with the new
kubelet instance. A new kubelet instance deletes all the existing Unix sockets under
`/var/lib/kubelet/device-plugins` (the hardcoded path for device plugins) when it starts. A device plugin can monitor the deletion
of its Unix socket and re-register itself upon such an event.