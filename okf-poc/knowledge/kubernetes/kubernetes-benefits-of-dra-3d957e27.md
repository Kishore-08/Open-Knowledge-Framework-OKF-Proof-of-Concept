---
id: kubernetes-benefits-of-dra-3d957e27
type: concept
title: Benefits of DRA
description: DRA provides a flexible way to categorize, request, and use devices in
  your cluster.
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/resource-management/dynamic-resource-allocation/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

### Benefits of DRA

DRA provides a flexible way to categorize, request, and use devices in your cluster.
Using DRA provides benefits like the following:

- **Flexible device filtering**: use common expression language (CEL) to perform
  fine-grained filtering for specific device attributes.
- **Device sharing**: share the same resource with multiple containers or Pods
  by referencing the corresponding resource claim.
- **Device configuration**: attach vendor-specific device configurations to your resource claim, enabling per-workload device configuration, rather than today's per-node device configuration
- **Centralized device categorization**: device drivers and cluster admins can
  use device classes to provide app operators with hardware categories that are
  optimized for various use cases. For example, you can create a cost-optimized
  device class for general-purpose workloads, and a high-performance device
  class for critical jobs.
- **Simplified Pod requests**: with DRA, app operators don't need to specify
  device quantities in Pod resource requests. Instead, the Pod references a
  resource claim, and the device configuration in that claim applies to the Pod.

These benefits provide significant improvements in the device allocation
workflow when compared to
[device plugins](https://kubernetes.io/docs/concepts/extend-kubernetes/compute-storage-net/device-plugins/),
which require per-container device requests, don't support device sharing, and
don't support expression-based device filtering.