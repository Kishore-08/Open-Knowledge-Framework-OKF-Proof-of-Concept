---
id: kubernetes-enabling-dynamic-provisioning-50610b7d
type: concept
title: Enabling Dynamic Provisioning
description: To enable dynamic provisioning, a cluster administrator needs to pre-create
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/storage/dynamic-provisioning/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

## Enabling Dynamic Provisioning

To enable dynamic provisioning, a cluster administrator needs to pre-create
one or more StorageClass objects for users.
StorageClass objects define which provisioner should be used and what parameters
should be passed to that provisioner when dynamic provisioning is invoked.
The name of a StorageClass object must be a valid
[DNS subdomain name](https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#dns-subdomain-names).

The following manifest creates a storage class "slow" which provisions standard
disk-like persistent disks.

```
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: slow
provisioner: kubernetes.io/gce-pd
parameters:
  type: pd-standard
```

The following manifest creates a storage class "fast" which provisions
SSD-like persistent disks.

```
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: fast
provisioner: kubernetes.io/gce-pd
parameters:
  type: pd-ssd
```