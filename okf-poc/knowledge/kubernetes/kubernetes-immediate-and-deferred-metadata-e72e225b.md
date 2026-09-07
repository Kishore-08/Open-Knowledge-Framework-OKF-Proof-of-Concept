---
id: kubernetes-immediate-and-deferred-metadata-e72e225b
type: concept
title: Immediate and deferred metadata
description: 'Drivers provide metadata in one of two ways:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/resource-management/dynamic-resource-allocation/dra-features/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

### Immediate and deferred metadata

Drivers provide metadata in one of two ways:

Immediate
:   The driver populates metadata while preparing the claim on the
    node and writes the metadata file before the container starts. This is
    typical for GPU drivers where device information is known at preparation time.

Deferred
:   In some cases, for example a network driver, the device information is
    not available during device allocation time but becomes available after the
    pod sandbox is created. In those cases the driver creates the CDI mount with
    an empty metadata file and writes the actual metadata later via an NRI hook
    that runs before the container starts. This ensures applications never see a
    missing or partially written file. Each update must increment
    `metadata.generation` so consumers can detect changes. The `MetadataUpdater`
    API in the DRA kubelet plugin library handles generation bookkeeping
    automatically for driver authors.

In both cases, metadata remains available to each consuming container for the
lifetime of that container. Metadata files are cleaned up after all containers
in the Pod have terminated.

To learn how to use device metadata in your workloads, see
[Access DRA device metadata](https://kubernetes.io/docs/tasks/configure-pod-container/assign-resources/access-dra-device-metadata/).