---
id: kubernetes-persistentvolumeclaim-naming-c2988c6c
type: concept
title: PersistentVolumeClaim naming
description: 'Naming of the automatically created PVCs is deterministic: the name
  is'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/storage/ephemeral-volumes/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### PersistentVolumeClaim naming

Naming of the automatically created PVCs is deterministic: the name is
a combination of the Pod name and volume name, with a hyphen (`-`) in the
middle. In the example above, the PVC name will be
`my-app-scratch-volume`. This deterministic naming makes it easier to
interact with the PVC because one does not have to search for it once
the Pod name and volume name are known.

The deterministic naming also introduces a potential conflict between different
Pods (a Pod "pod-a" with volume "scratch" and another Pod with name
"pod" and volume "a-scratch" both end up with the same PVC name
"pod-a-scratch") and between Pods and manually created PVCs.

Such conflicts are detected: a PVC is only used for an ephemeral
volume if it was created for the Pod. This check is based on the
ownership relationship. An existing PVC is not overwritten or
modified. But this does not resolve the conflict because without the
right PVC, the Pod cannot start.

#### Caution:

Take care when naming Pods and volumes inside the
same namespace, so that these conflicts can't occur.