---
id: kubernetes-portworx-volume-deprecated-1915a01d
type: concept
title: Portworx volume (deprecated)
description: '[`storage/storageclass/storageclass-portworx-volume.yaml`](https://raw.githubusercontent.com/kubernetes/website/main/content/en/examples/storage/storageclass/storageclass-portworx-volume.yaml)![](http'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/storage/storage-classes/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

### Portworx volume (deprecated)

[`storage/storageclass/storageclass-portworx-volume.yaml`](https://raw.githubusercontent.com/kubernetes/website/main/content/en/examples/storage/storageclass/storageclass-portworx-volume.yaml)![](https://kubernetes.io/images/copycode.svg "Copy storage/storageclass/storageclass-portworx-volume.yaml to clipboard")

```
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: portworx-io-priority-high
provisioner: kubernetes.io/portworx-volume # This provisioner is deprecated
parameters:
  repl: "1"
  snap_interval: "70"
  priority_io: "high"
```

- `fs`: filesystem to be laid out: `none/xfs/ext4` (default: `ext4`).
- `block_size`: block size in Kbytes (default: `32`).
- `repl`: number of synchronous replicas to be provided in the form of
  replication factor `1..3` (default: `1`) A string is expected here i.e.
  `"1"` and not `1`.
- `priority_io`: determines whether the volume will be created from higher
  performance or a lower priority storage `high/medium/low` (default: `low`).
- `snap_interval`: clock/time interval in minutes for when to trigger snapshots.
  Snapshots are incremental based on difference with the prior snapshot, 0
  disables snaps (default: `0`). A string is expected here i.e.
  `"70"` and not `70`.
- `aggregation_level`: specifies the number of chunks the volume would be
  distributed into, 0 indicates a non-aggregated volume (default: `0`). A string
  is expected here i.e. `"0"` and not `0`
- `ephemeral`: specifies whether the volume should be cleaned-up after unmount
  or should be persistent. `emptyDir` use case can set this value to true and
  `persistent volumes` use case such as for databases like Cassandra should set
  to false, `true/false` (default `false`). A string is expected here i.e.
  `"true"` and not `true`.