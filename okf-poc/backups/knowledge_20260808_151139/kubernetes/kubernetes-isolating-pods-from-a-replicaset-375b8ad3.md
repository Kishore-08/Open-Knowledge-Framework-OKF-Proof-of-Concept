---
id: kubernetes-isolating-pods-from-a-replicaset-375b8ad3
type: concept
title: Isolating Pods from a ReplicaSet
description: You can remove Pods from a ReplicaSet by changing their labels. This
  technique may be used to remove Pods
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/controllers/replicaset/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Isolating Pods from a ReplicaSet

You can remove Pods from a ReplicaSet by changing their labels. This technique may be used to remove Pods
from service for debugging, data recovery, etc. Pods that are removed in this way will be replaced automatically (
assuming that the number of replicas is not also changed).