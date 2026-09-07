---
id: kubernetes-persistentvolumeclaim-retention-f82fae6f
type: concept
title: PersistentVolumeClaim retention
description: 'FEATURE STATE:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

## PersistentVolumeClaim retention

FEATURE STATE:
`Kubernetes v1.32 [stable]`(enabled by default)

The optional `.spec.persistentVolumeClaimRetentionPolicy` field controls if
and how PVCs are deleted during the lifecycle of a StatefulSet. You must enable the
`StatefulSetAutoDeletePVC` [feature gate](https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/)
on the API server and the controller manager to use this field.
Once enabled, there are two policies you can configure for each StatefulSet:

`whenDeleted`
:   Configures the volume retention behavior that applies when the StatefulSet is deleted.

`whenScaled`
:   Configures the volume retention behavior that applies when the replica count of
    the StatefulSet is reduced; for example, when scaling down the set.

For each policy that you can configure, you can set the value to either `Delete` or `Retain`.

`Delete`
:   The PVCs created from the StatefulSet `volumeClaimTemplate` are deleted for each Pod
    affected by the policy. With the `whenDeleted` policy all PVCs from the
    `volumeClaimTemplate` are deleted after their Pods have been deleted. With the
    `whenScaled` policy, only PVCs corresponding to Pod replicas being scaled down are
    deleted, after their Pods have been deleted.

`Retain` (default)
:   PVCs from the `volumeClaimTemplate` are not affected when their Pod is
    deleted. This is the behavior before this new feature.

Bear in mind that these policies **only** apply when Pods are being removed due to the
StatefulSet being deleted or scaled down. For example, if a Pod associated with a StatefulSet
fails due to node failure, and the control plane creates a replacement Pod, the StatefulSet
retains the existing PVC. The existing volume is unaffected, and the cluster will attach it to
the node where the new Pod is about to launch.

The default for policies is `Retain`, matching the StatefulSet behavior before this new feature.

Here is an example policy:

```
apiVersion: apps/v1
kind: StatefulSet
...
spec:
  persistentVolumeClaimRetentionPolicy:
    whenDeleted: Retain
    whenScaled: Delete
...
```

The StatefulSet [controller](https://kubernetes.io/docs/concepts/architecture/controller/ "A control loop that watches the shared state of the cluster through the apiserver and makes changes attempting to move the current state towards the desired state.") adds
[owner references](https://kubernetes.io/docs/concepts/overview/working-with-objects/owners-dependents/#owner-references-in-object-specifications)
to its PVCs, which are then deleted by the [garbage collector](https://kubernetes.io/docs/concepts/architecture/garbage-collection/ "A collective term for the various mechanisms Kubernetes uses to clean up cluster resources.") after the Pod is terminated. This enables the Pod to
cleanly unmount all volumes before the PVCs are deleted (and before the backing PV and
volume are deleted, depending on the retain policy). When you set the `whenDeleted`
policy to `Delete`, an owner reference to the StatefulSet instance is placed on all PVCs
associated with that StatefulSet.

The `whenScaled` policy must delete PVCs only when a Pod is scaled down, and not when a
Pod is deleted for another reason. When reconciling, the StatefulSet controller compares
its desired replica count to the actual Pods present on the cluster. Any StatefulSet Pod
whose id greater than the replica count is condemned and marked for deletion. If the
`whenScaled` policy is `Delete`, the condemned Pods are first set as owners to the
associated StatefulSet template PVCs, before the Pod is deleted. This causes the PVCs
to be garbage collected after only the condemned Pods have terminated.

This means that if the controller crashes and restarts, no Pod will be deleted before its
owner reference has been updated appropriate to the policy. If a condemned Pod is
force-deleted while the controller is down, the owner reference may or may not have been
set up, depending on when th