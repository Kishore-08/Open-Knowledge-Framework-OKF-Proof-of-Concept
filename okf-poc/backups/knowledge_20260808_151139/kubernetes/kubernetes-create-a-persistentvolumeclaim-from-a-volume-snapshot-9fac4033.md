---
id: kubernetes-create-a-persistentvolumeclaim-from-a-volume-snapshot-9fac4033
type: concept
title: Create a PersistentVolumeClaim from a Volume Snapshot
description: '```'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/storage/persistent-volumes/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Create a PersistentVolumeClaim from a Volume Snapshot

```
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: restore-pvc
spec:
  storageClassName: csi-hostpath-sc
  dataSource:
    name: new-snapshot-test
    kind: VolumeSnapshot
    apiGroup: snapshot.storage.k8s.io
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 10Gi
```

## Volume Cloning

[Volume Cloning](https://kubernetes.io/docs/concepts/storage/volume-pvc-datasource/)
only available for CSI volume plugins.