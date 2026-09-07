---
id: kubernetes-metadata-schema-3d8c59ec
type: concept
title: Metadata schema
description: Each object in a metadata file conforms to the
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/resource-management/dynamic-resource-allocation/dra-observability/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

### Metadata schema

Each object in a metadata file conforms to the
[`DeviceMetadata`](https://pkg.go.dev/k8s.io/dynamic-resource-allocation/api/metadata/v1beta1#DeviceMetadata)
API (`metadata.resource.k8s.io/v1beta1`).

The schema contains:

- Standard object metadata for the ResourceClaim, including its name,
  namespace, UID, and metadata generation.
- The optional `podClaimName` for a claim generated from a
  ResourceClaimTemplate.
- A list of requests. Each request has a required name and a list of allocated
  devices.
- The driver, pool, and name for each device.
- Optional device attributes and network data.

Attribute values use the same representation as ResourceSlice device
attributes. Each attribute has exactly one scalar value (`int`, `bool`,
`string`, or `version`) or list value (`ints`, `bools`, `strings`, or
`versions`). Device capacity values are not included in device metadata.

Network data can contain `interfaceName`, `ips`, and `hardwareAddress`.
For field constraints, see the
[`DeviceMetadata` API documentation](https://pkg.go.dev/k8s.io/dynamic-resource-allocation/api/metadata/v1beta1#DeviceMetadata).

The following example shows one object in a metadata stream for a GPU device
allocated through a ResourceClaimTemplate:

```
{
  "kind": "DeviceMetadata",
  "apiVersion": "metadata.resource.k8s.io/v1beta1",
  "metadata": {
    "name": "pod0-gpu-2kqrd",
    "namespace": "gpu-test1",
    "uid": "c7e7b22e-239b-4498-b27c-7f1344481e14",
    "generation": 1
  },
  "podClaimName": "gpu",
  "requests": [
    {
      "name": "gpu",
      "devices": [
        {
          "driver": "gpu.example.com",
          "pool": "worker-0",
          "name": "gpu-0",
          "attributes": {
            "driverVersion": {
              "version": "1.0.0"
            },
            "index": {
              "int": 0
            },
            "model": {
              "string": "LATEST-GPU-MODEL"
            },
            "uuid": {
              "string": "gpu-18db0e85-99e9-c746-8531-ffeb86328b39"
            }
          }
        }
      ]
    }
  ]
}
```

The DRA kubelet plugin does not validate metadata before writing it. Go
consumers can opt in to generated validation when decoding a stream. Decoding
and validation have separate results: a validation error does not prevent a
successfully decoded object from being returned. For usage, see
[Access DRA device metadata](https://kubernetes.io/docs/tasks/configure-pod-container/assign-resources/access-dra-device-metadata/#read-metadata-application).