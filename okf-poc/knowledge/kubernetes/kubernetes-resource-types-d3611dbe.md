---
id: kubernetes-resource-types-d3611dbe
type: concept
title: Resource types
description: A *resource type* has a base unit and can be requested, limited, or both.
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

## Resource types

A *resource type* has a base unit and can be requested, limited, or both.
Kubernetes has the following built-in resource types:

| Resource type | Description | Base unit |
| --- | --- | --- |
| `cpu` | Compute processing | cpu (core) |
| `memory` | RAM | Bytes |
| `ephemeral-storage` | [Local ephemeral storage](https://kubernetes.io/docs/concepts/storage/ephemeral-storage/) | Bytes |
| `hugepages-<size>` | [Huge pages](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/#huge-pages) (Linux only) | Bytes |

Clusters can also provide
[extended resources](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/#extended-resources)
(resources with a custom name, typically exposed by device plugins).