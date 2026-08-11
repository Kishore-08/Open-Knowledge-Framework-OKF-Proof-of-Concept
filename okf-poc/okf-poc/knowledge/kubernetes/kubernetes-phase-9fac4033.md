---
id: kubernetes-phase-9fac4033
type: concept
title: Phase
description: 'A PersistentVolume will be in one of the following phases:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/storage/persistent-volumes/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Phase

A PersistentVolume will be in one of the following phases:

`Available`
:   a free resource that is not yet bound to a claim

`Bound`
:   the volume is bound to a claim

`Released`
:   the claim has been deleted, but the associated storage resource is not yet reclaimed by the cluster

`Failed`
:   the volume has failed its (automated) reclamation

You can see the name of the PVC bound to the PV using `kubectl describe persistentvolume <name>`.

#### Phase transition timestamp

FEATURE STATE:
`Kubernetes v1.31 [stable]`(enabled by default)

The `.status` field for a PersistentVolume can include an alpha `lastPhaseTransitionTime` field. This field records
the timestamp of when the volume last transitioned its phase. For newly created
volumes the phase is set to `Pending` and `lastPhaseTransitionTime` is set to
the current time.