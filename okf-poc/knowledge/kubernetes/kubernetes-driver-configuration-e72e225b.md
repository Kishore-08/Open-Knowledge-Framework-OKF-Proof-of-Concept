---
id: kubernetes-driver-configuration-e72e225b
type: concept
title: Driver configuration
description: Driver authors can specify the `skipNodeOperations` field in
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/resource-management/dynamic-resource-allocation/dra-features/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

### Driver configuration

Driver authors can specify the `skipNodeOperations` field in
`.spec.skipNodeOperations` of a ResourceSlice. This field is a list of unique
strings specifying the node-local operations to bypass for all devices in that
slice.

Valid values are:

- `"NodePrepareResources"`: Skips `NodePrepareResources` gRPC calls. This value
  cannot be specified unless `"NodeUnprepareResources"` is also listed (or `"*"`
  is specified). This limitation avoids Pods getting stuck in Terminating if a
  node-local plugin is missing, since the plugin is not checked during Pod
  startup when preparation is skipped.
- `"NodeUnprepareResources"`: Skips `NodeUnprepareResources` gRPC calls.
- `"*"`: Skips all node-local resource operations.

Here is an example of a ResourceSlice for a control-plane resource that skips
all node-local operations:

```
apiVersion: resource.k8s.io/v1
kind: ResourceSlice
metadata:
  name: control-plane-resources
spec:
  nodeName: worker-1
  pool:
    name: central-pool
    generation: 1
    resourceSliceCount: 1
  driver: control-plane.example.com
  skipNodeOperations:
  - "*"
  devices:
  - name: virtual-device-1
```