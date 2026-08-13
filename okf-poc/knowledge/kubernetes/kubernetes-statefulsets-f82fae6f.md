---
id: kubernetes-statefulsets-f82fae6f
type: concept
title: StatefulSets
description: A StatefulSet runs a group of Pods, and maintains a sticky identity for
  each of those Pods. This is useful for managing applications that need persistent
  storage or a stable, unique network identity.
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/
updated_at: '2026-08-13'
created_at: '2026-08-13'
---

# StatefulSets

A StatefulSet runs a group of Pods, and maintains a sticky identity for each of those Pods. This is useful for managing applications that need persistent storage or a stable, unique network identity.

StatefulSet is the workload API object used to manage stateful applications.

Manages the deployment and scaling of a set of [Pods](https://kubernetes.io/docs/concepts/workloads/pods/ "A Pod represents a set of running containers in your cluster."), *and provides guarantees about the ordering and uniqueness* of these Pods.

Like a [Deployment](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/ "Manages a replicated application on your cluster."), a StatefulSet manages Pods that are based on an identical container spec. Unlike a Deployment, a StatefulSet maintains a sticky identity for each of its Pods. These pods are created from the same spec, but are not interchangeable: each has a persistent identifier that it maintains across any rescheduling.

If you want to use storage volumes to provide persistence for your workload, you can use a StatefulSet as part of the solution. Although individual Pods in a StatefulSet are susceptible to failure, the persistent Pod identifiers make it easier to match existing volumes to the new Pods that replace any that have failed.