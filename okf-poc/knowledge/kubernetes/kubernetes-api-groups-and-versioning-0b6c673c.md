---
id: kubernetes-api-groups-and-versioning-0b6c673c
type: concept
title: API groups and versioning
description: To make it easier to eliminate fields or restructure resource representations,
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/overview/kubernetes-api/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

## API groups and versioning

To make it easier to eliminate fields or restructure resource representations,
Kubernetes supports multiple API versions, each at a different API path, such
as `/api/v1` or `/apis/rbac.authorization.k8s.io/v1alpha1`.

Versioning is done at the API level rather than at the resource or field level
to ensure that the API presents a clear, consistent view of system resources
and behavior, and to enable controlling access to end-of-life and/or
experimental APIs.

To make it easier to evolve and to extend its API, Kubernetes implements
[API groups](https://kubernetes.io/docs/reference/using-api/#api-groups) that can be
[enabled or disabled](https://kubernetes.io/docs/reference/using-api/#enabling-or-disabling).

API resources are distinguished by their API group, resource type, namespace
(for namespaced resources), and name. The API server handles the conversion between
API versions transparently: all the different versions are actually representations
of the same persisted data. The API server may serve the same underlying data
through multiple API versions.

For example, suppose there are two API versions, `v1` and `v1beta1`, for the same
resource. If you originally created an object using the `v1beta1` version of its
API, you can later read, update, or delete that object using either the `v1beta1`
or the `v1` API version, until the `v1beta1` version is deprecated and removed.
At that point you can continue accessing and modifying the object using the `v1` API.