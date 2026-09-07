---
id: kubernetes-device-metadata-protocol-3d8c59ec
type: concept
title: Device metadata protocol
description: 'The protocol consists of four rules:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/resource-management/dynamic-resource-allocation/dra-observability/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

### Device metadata protocol

The protocol consists of four rules:

1. **File paths.** Metadata files live inside containers under
   `/var/run/kubernetes.io/dra-device-attributes`. For a directly referenced
   ResourceClaim, the path is
   `resourceclaims/<claimName>/<requestName>/<driverName>-metadata.json`. For a
   claim created from a ResourceClaimTemplate, the path is
   `resourceclaimtemplates/<podClaimName>/<requestName>/<driverName>-metadata.json`,
   where `podClaimName` is `pod.spec.resourceClaims[].name`.

   When a request uses a [prioritized list](https://kubernetes.io/docs/concepts/resource-management/dynamic-resource-allocation/dra-api/#prioritized-list), only the
   top-level request name is used for the `<requestName>` path segment. The
   `requests[].name` field in the file contains the full
   `<request>/<subrequest>` reference, such as `gpu/high-memory`.

   The path constants are defined in
   [`k8s.io/dynamic-resource-allocation/api/metadata`](https://pkg.go.dev/k8s.io/dynamic-resource-allocation/api/metadata).
2. **JSON API.** Each file is a stream of one or more
   [`DeviceMetadata`](https://pkg.go.dev/k8s.io/dynamic-resource-allocation/api/metadata/v1beta1#DeviceMetadata)
   objects. Each object has `apiVersion` and `kind`, following Kubernetes API
   conventions. The same metadata is encoded once per configured API version
   in the order selected by the driver. Consumers use the first version that
   they can decode and skip unknown versions. A malformed object in a known
   version is an error.
3. **Generation.** The initial file has `metadata.generation` set to `1`.
   Each update increments the generation so that consumers can detect changes.
4. **Container exposure.** The DRA kubelet plugin library uses
   [CDI](https://kubernetes.io/docs/concepts/extend-kubernetes/compute-storage-net/device-plugins/ "A CNCF specification for describing device configuration that container runtimes apply when creating containers.") to bind-mount each file
   read-only. Other implementations can use a different mechanism as long as
   the file appears at the required path and is read-only.