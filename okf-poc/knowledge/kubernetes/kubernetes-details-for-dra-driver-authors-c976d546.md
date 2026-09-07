---
id: kubernetes-details-for-dra-driver-authors-c976d546
type: concept
title: Details for DRA Driver Authors
description: 'By default, each `DeviceAttribute` holds exactly one scalar value: a
  boolean, an integer,'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/resource-management/dynamic-resource-allocation/dra-api/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

### Details for DRA Driver Authors

By default, each `DeviceAttribute` holds exactly one scalar value: a boolean, an integer,
a string, or a semantic version string. The `DRAListTypeAttributes` feature gate extends
`DeviceAttribute` with four list-type fields, allowing a device to advertise multiple
values for a single attribute:

- **`bools`** — a list of boolean values
- **`ints`** — a list of 64-bit integer values
- **`strings`** — a list of strings (each at most 64 characters)
- **`versions`** — a list of semantic version strings per semver.org spec 2.0.0
  (each at most 64 characters)

The total number of individual attribute values per device (scalar fields plus all list
elements combined) is limited to **48**. When any device in a ResourceSlice uses this feature or other advanced features such as taints,
the ResourceSlice will be limited to at most **64** devices.
use list-type attributes or other advanced features such as taints.

Here is an example of a device advertising multiple supported models using a list-type
string attribute:

```
kind: ResourceSlice
apiVersion: resource.k8s.io/v1
metadata:
  name: example-resourceslice
spec:
  nodeName: worker-1
  pool:
    name: pool
    generation: 1
    resourceSliceCount: 1
  driver: dra.example.com
  devices:
  - name: gpu-0
    attributes:
      dra.example.com/supported-models:
        strings:
        - model-a
        - model-b
```

List type attributes is controlled by the
[`DRAListTypeAttributes` feature gate](https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/#DRAListTypeAttributes)
in the `kube-apiserver` and `kube-scheduler`.