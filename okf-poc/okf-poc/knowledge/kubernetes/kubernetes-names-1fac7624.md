---
id: kubernetes-names-1fac7624
type: concept
title: Names
description: A client-provided string that refers to an object in a [resource](https://kubernetes.io/docs/reference/using-api/api-concepts/#standard-api-terminology
  "A Kubernetes entity, representing an endpoint o
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

## Names

A client-provided string that refers to an object in a [resource](https://kubernetes.io/docs/reference/using-api/api-concepts/#standard-api-terminology "A Kubernetes entity, representing an endpoint on the Kubernetes API server.")
URL, such as `/api/v1/pods/some-name`.

Only one object of a given kind can have a given name at a time. However, if you delete the object, you can make a new object with the same name.

Names must be unique across all [API versions](https://kubernetes.io/docs/concepts/overview/kubernetes-api/#api-groups-and-versioning) of the same resource.

Kubernetes uniquely identifies objects using a combination of four attributes:

- **API group** (e.g., `apps`)
- **Resource type** (e.g., `deployments`)
- **Namespace** (for namespaced resources)
- **Name**

While you can access a resource through different API versions (such as `v1` or `v1beta1`), the version is simply a different representation of the same underlying object. Because the version is not part of the unique identification, you cannot create two objects with the same name and resource type in the same namespace by using different API versions.

#### Note:

In cases when objects represent a physical entity, like a Node representing a physical host, when the host is re-created under the same name without deleting and re-creating the Node, Kubernetes treats the new host as the old one, which may lead to inconsistencies.

The server may generate a name when `generateName` is provided instead of `name` in a resource create request.
When `generateName` is used, the provided value is used as a name prefix, which server appends a generated suffix
to. Even though the name is generated, it may conflict with existing names resulting in an HTTP 409 response. This
became far less likely to happen in Kubernetes v1.31 and later, since the server will make up to 8 attempts to generate a
unique name before returning an HTTP 409 response.

Below are four types of commonly used name constraints for resources.