---
id: kubernetes-device-taints-and-tolerations-4ed29670
type: concept
title: Device taints and tolerations
description: 'FEATURE STATE:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/resource-management/dynamic-resource-allocation/device-taints/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

## Device taints and tolerations

FEATURE STATE:
`Kubernetes v1.37 [stable]`(enabled by default)

Device taints are similar to node taints: a taint has a string key, a string value, and an effect.
The effect is applied to the ResourceClaim which is using a tainted device and to all Pods referencing that ResourceClaim.
The "NoSchedule" effect prevents scheduling those Pods.
Tainted devices are ignored when trying to allocate a ResourceClaim because using them would prevent scheduling of Pods.

The "NoExecute" effect implies "NoSchedule" and in addition causes eviction of all Pods
which have been scheduled already.
This eviction is implemented in the device taint eviction controller in kube-controller-manager by deleting affected Pods.

The "None" effect is ignored by the scheduler and eviction controller.
DRA drivers can use it to communicate exceptions to admins or other controllers,
for example degraded health of a device. Admins can also use it to
do dry-runs of pod eviction in DeviceTaintRules (more on that below).

ResourceClaims can tolerate taints. If a taint is tolerated, its effect does not apply.
An empty toleration matches all taints. A toleration can be limited to certain effects
and/or match certain key/value pairs.
A toleration can check that a certain key exists, regardless which value it has, or it can check
for specific values of a key.
For more information on this matching see the
[node taint concepts](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/#concepts).

Eviction can be delayed by tolerating a taint for a certain duration.
That delay starts at the time when a taint gets added to a device, which is recorded in a field of the taint.

Taints apply as described above also to ResourceClaims allocating "all" devices on a node.
All devices must be untainted or all of their taints must be tolerated.
Allocating a device with admin access (described [above](https://kubernetes.io/docs/concepts/resource-management/dynamic-resource-allocation/device-taints/#admin-access))
is not exempt either. An admin using that mode must explicitly tolerate all taints
to access tainted devices.

You can add taints to devices in the following ways, by using the DeviceTaintRule API kind.