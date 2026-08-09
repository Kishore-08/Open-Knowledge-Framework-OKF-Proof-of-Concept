---
id: kubernetes-unused-pvc-tracking-9fac4033
type: concept
title: Unused PVC tracking
description: 'FEATURE STATE:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/storage/persistent-volumes/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Unused PVC tracking

FEATURE STATE:
`Kubernetes v1.36 [alpha]`(disabled by default)

When enabled, the PVC protection controller adds an `Unused`
[condition](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#pod-conditions) to each
PersistentVolumeClaim to indicate whether it is currently referenced by any
non-terminal Pod.

The condition has two states:

`Unused` with status `"True"` (reason `NoPodsUsingPVC`)
:   No non-terminal Pod references this PVC. The `lastTransitionTime` records when
    the PVC became unused.

`Unused` with status `"False"` (reason `PodUsingPVC`)
:   At least one non-terminal Pod currently references this PVC. The
    `lastTransitionTime` records when the PVC started being used.

A Pod is considered non-terminal if its phase is not `Succeeded` or `Failed`.
This means that a Pending Pod (even one that has not yet been scheduled) counts
as using the PVC.

The `lastTransitionTime` of the `Unused` condition can be used by cluster
administrators, monitoring tools, and external controllers to identify PVCs that
have been unused for a long time. For example, to find all PVCs that have been
unused for more than 30 days, you could query for PVCs where the `Unused`
condition has `status: "True"` and `lastTransitionTime` is older than 30 days.

#### Note:

The unused duration indicated by this condition may be shorter than the actual
unused time because of processing delays in the controller or because the
feature was enabled after the PVC was already unused. The condition is not
updated when a PVC has `deletionTimestamp` set (that is, PVCs that are being deleted).