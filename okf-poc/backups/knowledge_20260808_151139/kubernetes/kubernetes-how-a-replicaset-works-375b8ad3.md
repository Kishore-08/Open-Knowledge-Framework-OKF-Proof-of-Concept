---
id: kubernetes-how-a-replicaset-works-375b8ad3
type: concept
title: How a ReplicaSet works
description: A ReplicaSet is defined with fields, including a selector that specifies
  how to identify Pods it can acquire, a number
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/controllers/replicaset/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

## How a ReplicaSet works

A ReplicaSet is defined with fields, including a selector that specifies how to identify Pods it can acquire, a number
of replicas indicating how many Pods it should be maintaining, and a pod template specifying the data of new Pods
it should create to meet the number of replicas criteria. A ReplicaSet then fulfills its purpose by creating
and deleting Pods as needed to reach the desired number. When a ReplicaSet needs to create new Pods, it uses its Pod
template.

A ReplicaSet is linked to its Pods via the Pods' [metadata.ownerReferences](https://kubernetes.io/docs/concepts/architecture/garbage-collection/#owners-dependents)
field, which specifies what resource the current object is owned by. All Pods acquired by a ReplicaSet have their owning
ReplicaSet's identifying information within their ownerReferences field. It's through this link that the ReplicaSet
knows of the state of the Pods it is maintaining and plans accordingly.

A ReplicaSet identifies new Pods to acquire by using its selector. If there is a Pod that has no
OwnerReference or the OwnerReference is not a [Controller](https://kubernetes.io/docs/concepts/architecture/controller/ "A control loop that watches the shared state of the cluster through the apiserver and makes changes attempting to move the current state towards the desired state.") and it
matches a ReplicaSet's selector, it will be immediately acquired by said ReplicaSet.