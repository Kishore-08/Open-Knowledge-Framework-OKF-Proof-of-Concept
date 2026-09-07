---
id: kubernetes-immediate-and-deferred-metadata-3d8c59ec
type: concept
title: Immediate and deferred metadata
description: For immediate metadata, the driver supplies attributes or network data
  while it
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/resource-management/dynamic-resource-allocation/dra-observability/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

### Immediate and deferred metadata

For immediate metadata, the driver supplies attributes or network data while it
prepares the claim. The DRA kubelet plugin writes the file with generation `1`
before the consuming container starts.

For deferred metadata, the driver can prepare a device without attributes or
network data. The initial generation `1` file contains the device identity. The
driver later calls `UpdateRequestMetadata` to replace the complete stream
atomically and increment the generation. An update requires the initial file to
exist. If device preparation returns no devices for a request, the framework
creates neither a metadata file nor a metadata CDI device for that request.

Metadata remains available to each consuming container for the lifetime of that
container. The framework removes the metadata files and CDI specifications
after the claim is unprepared.

To learn how to use device metadata in your workloads, see
[Access DRA device metadata](https://kubernetes.io/docs/tasks/configure-pod-container/assign-resources/access-dra-device-metadata/).