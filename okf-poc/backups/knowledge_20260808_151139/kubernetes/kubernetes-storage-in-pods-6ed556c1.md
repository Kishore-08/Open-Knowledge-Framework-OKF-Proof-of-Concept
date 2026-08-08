---
id: kubernetes-storage-in-pods-6ed556c1
type: concept
title: Storage in Pods
description: A Pod can specify a set of shared storage
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/pods/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Storage in Pods

A Pod can specify a set of shared storage
[volumes](https://kubernetes.io/docs/concepts/storage/volumes/ "A directory containing data, accessible to the containers in a pod."). All containers
in the Pod can access the shared volumes, allowing those containers to
share data. Volumes also allow persistent data in a Pod to survive
in case one of the containers within needs to be restarted. See
[Storage](https://kubernetes.io/docs/concepts/storage/) for more information on how
Kubernetes implements shared storage and makes it available to Pods.