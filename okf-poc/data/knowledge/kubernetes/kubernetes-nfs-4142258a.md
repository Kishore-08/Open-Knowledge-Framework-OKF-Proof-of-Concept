---
id: kubernetes-nfs-4142258a
type: concept
title: nfs
description: An `nfs` volume allows an existing NFS (Network File System) share to
  be
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/storage/volumes/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### nfs

An `nfs` volume allows an existing NFS (Network File System) share to be
mounted into a Pod. Unlike `emptyDir`, which is erased when a Pod is
removed, the contents of an `nfs` volume are preserved, and the volume is merely
unmounted. This means that an NFS volume can be pre-populated with data, and
that data can be shared between Pods. NFS can be mounted by multiple
writers simultaneously.

```
apiVersion: v1
kind: Pod
metadata:
  name: test-pd
spec:
  containers:
  - image: registry.k8s.io/test-webserver
    name: test-container
    volumeMounts:
    - mountPath: /my-nfs-data
      name: test-volume
  volumes:
  - name: test-volume
    nfs:
      server: my-nfs-server.example.com
      path: /my-nfs-volume
      readOnly: true
```

#### Note:

You must have your own NFS server running with the share exported before you can use it.

Also note that you can't specify NFS mount options in a Pod spec. You can either set mount options server-side or
use [/etc/nfsmount.conf](https://man7.org/linux/man-pages/man5/nfsmount.conf.5.html).
You can also mount NFS volumes via PersistentVolumes, which do allow you to set mount options.