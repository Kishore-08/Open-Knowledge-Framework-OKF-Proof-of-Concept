---
id: kubernetes-using-configmaps-as-files-from-a-pod-02bcaed0
type: concept
title: Using ConfigMaps as files from a Pod
description: 'To consume a ConfigMap in a volume in a Pod:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/configuration/configmap/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Using ConfigMaps as files from a Pod

To consume a ConfigMap in a volume in a Pod:

1. Create a ConfigMap or use an existing one. Multiple Pods can reference the
   same ConfigMap.
2. Modify your Pod definition to add a volume under `.spec.volumes[]`. Name
   the volume anything, and have a `.spec.volumes[].configMap.name` field set
   to reference your ConfigMap object.
3. Add a `.spec.containers[].volumeMounts[]` to each container that needs the
   ConfigMap. Specify `.spec.containers[].volumeMounts[].readOnly = true` and
   `.spec.containers[].volumeMounts[].mountPath` to an unused directory name
   where you would like the ConfigMap to appear.
4. Modify your image or command line so that the program looks for files in
   that directory. Each key in the ConfigMap `data` map becomes the filename
   under `mountPath`.

This is an example of a Pod that mounts a ConfigMap in a volume:

```
apiVersion: v1
kind: Pod
metadata:
  name: mypod
spec:
  containers:
  - name: mypod
    image: redis
    volumeMounts:
    - name: foo
      mountPath: "/etc/foo"
      readOnly: true
  volumes:
  - name: foo
    configMap:
      name: myconfigmap
```

Each ConfigMap you want to use needs to be referred to in `.spec.volumes`.

If there are multiple containers in the Pod, then each container needs its
own `volumeMounts` block, but only one `.spec.volumes` is needed per ConfigMap.

#### Mounted ConfigMaps are updated automatically

When a ConfigMap currently consumed in a volume is updated, projected keys are eventually updated as well.
The kubelet checks whether the mounted ConfigMap is fresh on every periodic sync.
However, the kubelet uses its local cache for getting the current value of the ConfigMap.
The type of the cache is configurable using the `configMapAndSecretChangeDetectionStrategy` field in
the [KubeletConfiguration struct](https://kubernetes.io/docs/reference/config-api/kubelet-config.v1beta1/).
A ConfigMap can be either propagated by watch (default), ttl-based, or by redirecting
all requests directly to the API server.
As a result, the total delay from the moment when the ConfigMap is updated to the moment
when new keys are projected to the Pod can be as long as the kubelet sync period + cache
propagation delay, where the cache propagation delay depends on the chosen cache type
(it equals to watch propagation delay, ttl of cache, or zero correspondingly).

ConfigMaps consumed as environment variables are not updated automatically and require a pod restart.

#### Note:

A container using a ConfigMap as a [subPath](https://kubernetes.io/docs/concepts/storage/volumes/#using-subpath) volume mount will not receive ConfigMap updates.