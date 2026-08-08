---
id: kubernetes-volume-populators-and-data-sources-9fac4033
type: concept
title: Volume populators and data sources
description: '[Volume cloning](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#volume-cloning)
  and'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/storage/persistent-volumes/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

## Volume populators and data sources

[Volume cloning](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#volume-cloning) and
[snapshot restore](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#volume-snapshot-and-restore-volume-from-snapshot-support) pre-populate
a new volume from a built-in *data source*. *Volume populators* extend this mechanism so that
a PersistentVolumeClaim can be pre-populated from other kinds of source (a custom resource),
referenced through its `dataSourceRef` field:

```
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: populated-pvc
spec:
  dataSourceRef:
    name: example-name
    kind: ExampleDataSource
    apiGroup: example.storage.k8s.io
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 10Gi
```

For details, including cross-namespace data sources, see
[Volume Populators and Data Sources](https://kubernetes.io/docs/concepts/storage/volume-populators-and-data-sources/).