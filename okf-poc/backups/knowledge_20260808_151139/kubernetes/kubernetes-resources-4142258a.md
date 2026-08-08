---
id: kubernetes-resources-4142258a
type: concept
title: Resources
description: The storage medium (such as Disk or SSD) of an `emptyDir` volume is determined
  by the
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/storage/volumes/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

## Resources

The storage medium (such as Disk or SSD) of an `emptyDir` volume is determined by the
medium of the filesystem holding the kubelet root dir (typically
`/var/lib/kubelet`). There is no limit on how much space an `emptyDir` or
`hostPath` volume can consume, and no isolation between containers or
Pods.

To learn about requesting space using a resource specification, see
[how to manage resources](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/).