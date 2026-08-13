---
id: kubernetes-resource-monitoring-for-local-ephemeral-storage-d3611dbe
type: concept
title: Resource monitoring for local ephemeral storage
description: The kubelet can measure how much local ephemeral storage is being used.
  It
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/
updated_at: '2026-08-13'
created_at: '2026-08-13'
---

### Resource monitoring for local ephemeral storage

The kubelet can measure how much local ephemeral storage is being used. It
does this as long as you have enabled local ephemeral storage capacity isolation.

Kubernetes tracks the amount of ephemeral storage a Pod uses from the following:

- Writing to the container's writable layer (rootfs), container images, or both.
- Writing to local `emptyDir` volumes.
- The Pod's own logs (usually stored under `/var/log/pods`).
- System files managed by Kubernetes that are mapped into the Pod, such as `/etc/hosts`.