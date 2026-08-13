---
id: kubernetes-volume-binding-mode-1915a01d
type: concept
title: Volume binding mode
description: The `volumeBindingMode` field controls when
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/storage/storage-classes/
updated_at: '2026-08-13'
created_at: '2026-08-13'
---

## Volume binding mode

The `volumeBindingMode` field controls when
[volume binding and dynamic provisioning](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#provisioning)
should occur. When unset, `Immediate` mode is used by default.

The `Immediate` mode indicates that volume binding and dynamic
provisioning occurs once the PersistentVolumeClaim is created. For storage
backends that are topology-constrained and not globally accessible from all Nodes
in the cluster, PersistentVolumes will be bound or provisioned without knowledge of the Pod's scheduling
requirements. This may result in unschedulable Pods.

A cluster administrator can address this issue by specifying the `WaitForFirstConsumer` mode which
will delay the binding and provisioning of a PersistentVolume until a Pod using the PersistentVolumeClaim is created.
PersistentVolumes will be selected or provisioned conforming to the topology that is
specified by the Pod's scheduling constraints. These include, but are not limited to, [resource
requirements](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/),
[node selectors](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#nodeselector),
[pod affinity and
anti-affinity](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#affinity-and-anti-affinity),
and [taints and tolerations](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/).

The following plugins support `WaitForFirstConsumer` with dynamic provisioning:

- CSI volumes, provided that the specific CSI driver supports this

The following plugins support `WaitForFirstConsumer` with pre-created PersistentVolume binding:

- CSI volumes, provided that the specific CSI driver supports this
- [`local`](https://kubernetes.io/docs/concepts/storage/storage-classes/#local)

#### Note:

If you choose to use `WaitForFirstConsumer`, do not use `nodeName` in the Pod spec
to specify node affinity.
If `nodeName` is used in this case, the scheduler will be bypassed and PVC will remain in `pending` state.

Instead, you can use node selector for `kubernetes.io/hostname`:

[`storage/storageclass/pod-volume-binding.yaml`](https://raw.githubusercontent.com/kubernetes/website/main/content/en/examples/storage/storageclass/pod-volume-binding.yaml)![](https://kubernetes.io/images/copycode.svg "Copy storage/storageclass/pod-volume-binding.yaml to clipboard")

```
apiVersion: v1
kind: Pod
metadata:
  name: task-pv-pod
spec:
  nodeSelector:
    kubernetes.io/hostname: kube-01
  volumes:
    - name: task-pv-storage
      persistentVolumeClaim:
        claimName: task-pv-claim
  containers:
    - name: task-pv-container
      image: nginx
      ports:
        - containerPort: 80
          name: "http-server"
      volumeMounts:
        - mountPath: "/usr/share/nginx/html"
          name: task-pv-storage
```