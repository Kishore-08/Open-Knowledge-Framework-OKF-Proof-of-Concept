---
id: kubernetes-linux-18ab9e15
type: concept
title: Linux
description: In Linux pods that have a projected volume and `RunAsUser` set in the
  Pod
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/storage/projected-volumes/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Linux

In Linux pods that have a projected volume and `RunAsUser` set in the Pod
[`SecurityContext`](https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/pod-v1/#security-context),
the projected files have the correct ownership set including container user
ownership.

When all containers in a pod have the same `runAsUser` set in their
[`PodSecurityContext`](https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/pod-v1/#security-context)
or container
[`SecurityContext`](https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/pod-v1/#security-context-1),
then the kubelet ensures that the contents of the `serviceAccountToken` volume are owned by that user,
and the token file has its permission mode set to `0600`.

#### Note:

[Ephemeral containers](https://kubernetes.io/docs/concepts/workloads/pods/ephemeral-containers/ "A type of container type that you can temporarily run inside a Pod")
added to a Pod after it is created do *not* change volume permissions that were
set when the pod was created.

If a Pod's `serviceAccountToken` volume permissions were set to `0600` because
all other containers in the Pod have the same `runAsUser`, ephemeral
containers must use the same `runAsUser` to be able to read the token.