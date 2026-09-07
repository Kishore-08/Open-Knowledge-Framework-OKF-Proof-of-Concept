---
id: kubernetes-limitations-f82fae6f
type: concept
title: Limitations
description: '- The storage for a given Pod must either be provisioned by a'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

## Limitations

- The storage for a given Pod must either be provisioned by a
  [PersistentVolume Provisioner](https://kubernetes.io/docs/concepts/storage/dynamic-provisioning/)
  based on the requested *storage class*, or pre-provisioned by an admin.
- Deleting and/or scaling a StatefulSet down will *not* delete the volumes associated with the
  StatefulSet. This is done to ensure data safety, which is generally more valuable than an
  automatic purge of all related StatefulSet resources.
- StatefulSets currently require a [Headless Service](https://kubernetes.io/docs/concepts/services-networking/service/#headless-services)
  to be responsible for the network identity of the Pods. You are responsible for creating this
  Service.
- StatefulSets do not provide any guarantees on the termination of pods when a StatefulSet is
  deleted. To achieve ordered and graceful termination of the pods in the StatefulSet, it is
  possible to scale the StatefulSet down to 0 prior to deletion.
- When using [Rolling Updates](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/#rolling-updates) with the default
  [Pod Management Policy](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/#pod-management-policies) (`OrderedReady`),
  it's possible to get into a broken state that requires
  [manual intervention to repair](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/#forced-rollback).