---
id: kubernetes-forced-storage-detach-on-timeout-e5a13667
type: concept
title: Forced storage detach on timeout
description: In any situation where a pod deletion has not succeeded for 6 minutes,
  kubernetes will
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/cluster-administration/node-shutdown/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Forced storage detach on timeout

In any situation where a pod deletion has not succeeded for 6 minutes, kubernetes will
force detach volumes being unmounted if the node is unhealthy at that instant. Any
workload still running on the node that uses a force-detached volume will cause a
violation of the
[CSI specification](https://github.com/container-storage-interface/spec/blob/master/spec.md#controllerunpublishvolume),
which states that `ControllerUnpublishVolume` "**must** be called after all
`NodeUnstageVolume` and `NodeUnpublishVolume` on the volume are called and succeed".
In such circumstances, volumes on the node in question might encounter data corruption.

The forced storage detach behaviour is optional; users might opt to use the "Non-graceful
node shutdown" feature instead.

Force storage detach on timeout can be disabled by setting the `disable-force-detach-on-timeout`
config field in `kube-controller-manager`. Disabling the force detach on timeout feature means
that a volume that is hosted on a node that is unhealthy for more than 6 minutes will not have
its associated
[VolumeAttachment](https://kubernetes.io/docs/reference/kubernetes-api/config-and-storage-resources/volume-attachment-v1/)
deleted.

After this setting has been applied, unhealthy pods still attached to volumes must be recovered
via the [Non-Graceful Node Shutdown](https://kubernetes.io/docs/concepts/cluster-administration/node-shutdown/#non-graceful-node-shutdown) procedure mentioned above.

#### Note:

- Caution must be taken while using the [Non-Graceful Node Shutdown](https://kubernetes.io/docs/concepts/cluster-administration/node-shutdown/#non-graceful-node-shutdown) procedure.
- Deviation from the steps documented above can result in data corruption.