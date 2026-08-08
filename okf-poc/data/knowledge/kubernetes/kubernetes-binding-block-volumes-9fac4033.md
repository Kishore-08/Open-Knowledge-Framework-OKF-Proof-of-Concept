---
id: kubernetes-binding-block-volumes-9fac4033
type: concept
title: Binding Block Volumes
description: If a user requests a raw block volume by indicating this using the `volumeMode`
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/storage/persistent-volumes/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Binding Block Volumes

If a user requests a raw block volume by indicating this using the `volumeMode`
field in the PersistentVolumeClaim spec, the binding rules differ slightly from
previous releases that didn't consider this mode as part of the spec.
Listed is a table of possible combinations the user and admin might specify for
requesting a raw block device. The table indicates if the volume will be bound or
not given the combinations: Volume binding matrix for statically provisioned volumes:

| PV volumeMode | PVC volumeMode | Result |
| --- | --- | --- |
| unspecified | unspecified | BIND |
| unspecified | Block | NO BIND |
| unspecified | Filesystem | BIND |
| Block | unspecified | NO BIND |
| Block | Block | BIND |
| Block | Filesystem | NO BIND |
| Filesystem | Filesystem | BIND |
| Filesystem | Block | NO BIND |
| Filesystem | unspecified | BIND |

#### Note:

Only statically provisioned volumes are supported for alpha release. Administrators
should take care to consider these values when working with raw block devices.