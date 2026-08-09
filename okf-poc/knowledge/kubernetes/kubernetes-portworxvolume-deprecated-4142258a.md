---
id: kubernetes-portworxvolume-deprecated-4142258a
type: concept
title: portworxVolume (deprecated)
description: 'FEATURE STATE:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/storage/volumes/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### portworxVolume (deprecated)

FEATURE STATE:
`Kubernetes v1.25 [deprecated]`

A `portworxVolume` is an elastic block storage layer that runs hyperconverged with
Kubernetes. [Portworx](https://portworx.com/use-case/kubernetes-storage/) fingerprints storage
in a server, tiers based on capabilities, and aggregates capacity across multiple servers.
Portworx runs in-guest in virtual machines or on bare metal Linux nodes.

A `portworxVolume` can be dynamically created through Kubernetes, or it can also
be pre-provisioned and referenced inside a Pod.
Here is an example Pod referencing a pre-provisioned Portworx volume:

```
apiVersion: v1
kind: Pod
metadata:
  name: test-portworx-volume-pod
spec:
  containers:
  - image: registry.k8s.io/test-webserver
    name: test-container
    volumeMounts:
    - mountPath: /mnt
      name: pxvol
  volumes:
  - name: pxvol
    # This Portworx volume must already exist.
    portworxVolume:
      volumeID: "pxvol"
      fsType: "<fs-type>"
```

#### Note:

Make sure you have an existing PortworxVolume with the name `pxvol`
before using it in the Pod.

#### Portworx CSI migration

FEATURE STATE:
`Kubernetes v1.33 [stable]`(enabled by default)

In Kubernetes 1.36, all operations for the in-tree
Portworx volumes are redirected to the `pxd.portworx.com`
Container Storage Interface (CSI) Driver by default.  
[Portworx CSI Driver](https://docs.portworx.com/portworx-enterprise/operations/operate-kubernetes/storage-operations/csi)
must be installed on the cluster.