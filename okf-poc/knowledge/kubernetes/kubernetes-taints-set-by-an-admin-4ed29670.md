---
id: kubernetes-taints-set-by-an-admin-4ed29670
type: concept
title: Taints set by an admin
description: 'FEATURE STATE:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/resource-management/dynamic-resource-allocation/device-taints/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

### Taints set by an admin

FEATURE STATE:
`Kubernetes v1.37 [stable]`(enabled by default)

An admin or a control plane component can taint devices without having to tell
the DRA driver to include taints in its device information in ResourceSlices.
They do that by creating DeviceTaintRules.
Each DeviceTaintRule adds one taint to devices which match the device selector.
Without such a selector, no devices are tainted.
This makes it harder to accidentally evict all pods using ResourceClaims when leaving out the selector by mistake.

Devices can be selected by giving the name of a DeviceClass, driver, pool, and/or device.
The DeviceClass selects all devices that are selected by the selectors in that DeviceClass.
With just the driver name, an admin can taint all devices managed by that driver,
for example while doing some kind of maintenance of that driver across the entire cluster.
Adding a pool name can limit the taint to a single node, if the driver manages node-local devices.

Finally, adding the device name can select one specific device.
The device name and pool name can also be used alone, if desired.
For example, drivers for node-local devices are encouraged to use the node name as their pool name.
Then tainting with that pool name automatically taints all devices on a node.

Drivers might use stable names like "gpu-0" that hide which specific device is currently assigned to that name.
To support tainting a specific hardware instance, CEL selectors can be used in a DeviceTaintRule
to match a vendor-specific unique ID attribute, if the driver supports one for its hardware.

The taint applies as long as the DeviceTaintRule exists.
It can be modified and and removed at any time.
Here is one example of a DeviceTaintRule for a fictional DRA driver:

```
apiVersion: resource.k8s.io/v1
kind: DeviceTaintRule
metadata:
  name: example
spec:
  # The entire hardware installation for this
  # particular driver is broken.
  # Evict all pods and don't schedule new ones.
  deviceSelector:
    driver: dra.example.com
  taint:
    key: dra.example.com/unhealthy
    value: Broken
    effect: NoExecute
```

The kube-apiserver automatically tracks when this taint was created by setting the
`timeAdded` field in the `spec`. The toleration period starts at that time
stamp. During updates which change the effect (see simulated eviction flow
below), the kube-apiserver automatically updates the time stamp. Users can control
the time stamp explicitly by setting the field when creating a DeviceTaintRule and
by changing it to some different value when updating.

The status contains a condition added by the eviction controller:

```
kubectl describe devicetaintrules
```

```
Name:         example
...
Spec:
  Device Selector:
    Driver:  dra.example.com
  Taint:
    Effect:      NoExecute
    Key:         dra.example.com/unhealthy
    Time Added:  2025-11-05T18:15:37Z
    Value:       Broken
Status:
  Conditions:
    Last Transition Time:  2025-11-05T18:15:37Z
    Message:               1 pod evicted since starting the controller.
    Observed Generation:   1
    Reason:                Completed
    Status:                False
    Type:                  EvictionInProgress
Events:                    <none>
```

Pods get evicted by deleting them. Usually this happens very quickly,
except when a toleration for the taint delays it for a certain period or
when there are very many pods which need to be evicted. When it takes
longer, the message provides information about the current status:

```
2 pods need to be evicted in 2 different namespaces. 1 pod evicted since starting the controller.
```

The condition can be used to check whether an eviction is currently active:

```
kubectl wait --for=condition=EvictionInProgress=false DeviceTaintRule/example
```

Beware of the potential race between scheduler and controller observing the new
taint at different times, which can lead to pods still being scheduled at a
time when the controller thinks that there are