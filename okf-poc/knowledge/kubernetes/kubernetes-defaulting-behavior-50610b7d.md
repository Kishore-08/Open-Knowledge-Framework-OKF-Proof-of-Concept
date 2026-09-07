---
id: kubernetes-defaulting-behavior-50610b7d
type: concept
title: Defaulting Behavior
description: Dynamic provisioning can be enabled on a cluster such that all claims
  are
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/storage/dynamic-provisioning/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

## Defaulting Behavior

Dynamic provisioning can be enabled on a cluster such that all claims are
dynamically provisioned if no storage class is specified. A cluster administrator
can enable this behavior by:

- Marking one `StorageClass` object as *default*.
- Making sure that the [`DefaultStorageClass` admission controller](https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers/#defaultstorageclass)
  is enabled on the API server.

An administrator can mark a specific `StorageClass` as default by adding the
[`storageclass.kubernetes.io/is-default-class` annotation](https://kubernetes.io/docs/reference/labels-annotations-taints/#storageclass-kubernetes-io-is-default-class) to it.
When a default `StorageClass` exists in a cluster and a user creates a
`PersistentVolumeClaim` with `storageClassName` unspecified, the
`DefaultStorageClass` admission controller automatically adds the
`storageClassName` field pointing to the default storage class.

Note that if you set the `storageclass.kubernetes.io/is-default-class`
annotation to true on more than one StorageClass in your cluster, and you then
create a `PersistentVolumeClaim` with no `storageClassName` set, Kubernetes
uses the most recently created default StorageClass.