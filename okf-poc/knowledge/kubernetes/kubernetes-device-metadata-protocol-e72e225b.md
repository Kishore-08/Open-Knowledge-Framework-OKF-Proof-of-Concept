---
id: kubernetes-device-metadata-protocol-e72e225b
type: concept
title: Device metadata protocol
description: 'The protocol consists of four rules:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/resource-management/dynamic-resource-allocation/dra-features/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

### Device metadata protocol

The protocol consists of four rules:

1. **File paths.** Metadata files live inside containers under
   `/var/run/kubernetes.io/dra-device-attributes`. For a directly referenced
   ResourceClaim the path is
   `resourceclaims/<claimName>/<requestName>/<driverName>-metadata.json`; for a
   claim created from a ResourceClaimTemplate the path is
   `resourceclaimtemplates/<podClaimName>/<requestName>/<driverName>-metadata.json`
   (where `podClaimName` is `pod.spec.resourceClaims[].name`).

   In cases where the ResourceClaim request uses the
   [prioritized list](https://kubernetes.io/docs/concepts/resource-management/dynamic-resource-allocation/dra-features/#prioritized-list) feature, only the top-level request
   name is used for the `<requestName>` segment in the file path (that is,
   the `/<subrequest>` portion is dropped). Inside the
   JSON file, the `requests[].name` field carries the full
   `<request>/<subrequest>` reference (for example, `gpu/high-memory`) so
   that consumers can identify which alternative was allocated.

   The path constants are defined in
   [`k8s.io/dynamic-resource-allocation/api/metadata`](https://pkg.go.dev/k8s.io/dynamic-resource-allocation/api/metadata).
2. **JSON API.** Each file is a stream of one or more
   [`DeviceMetadata`](https://pkg.go.dev/k8s.io/dynamic-resource-allocation/api/metadata/v1alpha1#DeviceMetadata)
   objects serialized as versioned JSON with `apiVersion` and `kind`, following
   Kubernetes API conventions. The same metadata is encoded once per supported
   API version (newest first). All objects in the stream are semantically
   equivalent; consumers should use the first object they can decode.
3. **Generation.** When a driver updates a metadata file the embedded
   `metadata.generation` field must increase so consumers can detect changes.
4. **Container exposure.** Files are typically exposed via
   [CDI](https://kubernetes.io/docs/concepts/extend-kubernetes/compute-storage-net/device-plugins/ "A CNCF specification for describing device configuration that container runtimes apply when creating containers.") bind-mounts, but other
   mechanisms are permitted as long as the file appears at the correct path and
   is read-only inside the container.