---
id: kubernetes-device-binding-conditions-d98ef934
type: concept
title: Device binding conditions
description: 'FEATURE STATE:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/resource-management/dynamic-resource-allocation/how-dra-works/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

## Device binding conditions

FEATURE STATE:
`Kubernetes v1.36 [beta]`(enabled by default)

Device Binding Conditions allow the Kubernetes scheduler to delay Pod binding until
external resources, such as fabric-attached GPUs or reprogrammable FPGAs, are confirmed
to be ready.

This waiting behavior is implemented in the
[PreBind phase](https://kubernetes.io/docs/concepts/scheduling-eviction/scheduling-framework/#pre-bind)
of the scheduling framework.
During this phase, the scheduler checks whether all required device conditions are
satisfied before proceeding with binding.

This improves scheduling reliability by avoiding premature binding and enables coordination
with external device controllers.

To use this feature, device drivers (typically managed by driver owners) must publish the
following fields in the `Device` section of a `ResourceSlice`. Cluster administrators
must enable the `DRADeviceBindingConditions` and `DRAResourceClaimDeviceStatus` feature
gates for the scheduler to honor these fields.

`bindingConditions`
:   A list of *condition types* that must be set to True (in the `.status.conditions` field of the associated ResourceClaim) before the Pod can be bound. These conditions typically represent readiness signals, such as DeviceAttached or DeviceInitialized.

`bindingFailureConditions`
:   A list of condition types that, if set to True in
    status.conditions field of the associated ResourceClaim, indicate a failure state.
    If any of these conditions are True, the scheduler will abort binding and reschedule the Pod.

`bindsToNode`
:   if set to `true`, the scheduler records the selected node name in the
    `status.allocation.nodeSelector` field of the ResourceClaim.
    This does not affect the Pod's `spec.nodeSelector`. Instead, it sets a node selector
    inside the ResourceClaim, which external controllers can use to perform node-specific
    operations such as device attachment or preparation.

All condition types listed in bindingConditions and bindingFailureConditions are evaluated
from the `status.conditions` field of the ResourceClaim.
External controllers are responsible for updating these conditions using standard Kubernetes
condition semantics (`type`, `status`, `reason`, `message`, `lastTransitionTime`).

The scheduler waits up to **600 seconds** (default) for all `bindingConditions` to become `True`.
If the timeout is reached or any `bindingFailureConditions` are `True`, the scheduler
clears the allocation and reschedules the Pod.
A cluster administration can configure this timeout duration by editing the kube-scheduler configuration file.

An example of configuring this timeout in `KubeSchedulerConfiguration` is given below:

```
apiVersion: kubescheduler.config.k8s.io/v1
kind: KubeSchedulerConfiguration
profiles:
- schedulerName: default-scheduler
  pluginConfig:
  - name: DynamicResources
    args:
      apiVersion: kubescheduler.config.k8s.io/v1
      kind: DynamicResourcesArgs
      bindingTimeout: 60s
```