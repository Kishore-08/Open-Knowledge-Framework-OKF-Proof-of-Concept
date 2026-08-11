---
id: kubernetes-quota-for-dra-resource-claims-193abbf6
type: concept
title: Quota for DRA resource claims
description: DRA (Dynamic Resource Allocation) resource claims can request DRA resources
  by device class. For an example
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/policy/resource-quotas/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Quota for DRA resource claims

DRA (Dynamic Resource Allocation) resource claims can request DRA resources by device class. For an example
device class named `examplegpu`, you want to limit the total number of GPUs requested in a namespace to 4,
you can define a quota as follows:

- `examplegpu.deviceclass.resource.k8s.io/devices: 4`

When [Extended Resource allocation by DRA](https://kubernetes.io/docs/concepts/scheduling-eviction/dynamic-resource-allocation/#extended-resource)
is enabled, the same device class named `examplegpu` can be requested via extended resource either explicitly
when the device class's ExtendedResourceName field is given, say, `example.com/gpu`, then you can define a quota as follows:

- `requests.example.com/gpu: 4`

or implicitly using the derived extended resource name from device class name `examplegpu`, you can define
a quota as follows:

- `requests.deviceclass.resource.kubernetes.io/examplegpu: 4`

All devices requested from resource claims or extended resources are counted towards all three quotas
listed above. The extended resource quota e.g. `requests.example.com/gpu: 4`, also counts the devices provided
by device plugin.

See [Viewing and Setting Quotas](https://kubernetes.io/docs/concepts/policy/resource-quotas/#viewing-and-setting-quotas) for more details.