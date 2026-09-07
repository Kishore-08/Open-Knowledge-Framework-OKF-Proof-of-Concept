---
id: kubernetes-types-of-dra-users-3d957e27
type: concept
title: Types of DRA users
description: 'The workflow of using DRA to allocate devices involves the following
  types of users:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/resource-management/dynamic-resource-allocation/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

### Types of DRA users

The workflow of using DRA to allocate devices involves the following types of users:

- **Device owner**: responsible for devices. Device owners might be commercial
  vendors, the cluster operator, or another entity. To use DRA, devices must
  have DRA-compatible drivers that do the following:

  - Create ResourceSlices that provide Kubernetes with information about
    nodes and resources.
  - Update ResourceSlices when resource capacity in the cluster changes.
  - Configure devices according to the claim, and attach them to containers via Container Device Interface (CDI).
  - Optionally, create DeviceClasses that workload operators can use to
    claim devices.
- **Cluster admin**: responsible for configuring clusters and nodes,
  attaching devices, installing drivers, and similar tasks. To use DRA,
  cluster admins do the following:

  - Attach devices to nodes.
  - Install device drivers that support DRA.
  - Optionally, create DeviceClasses that workload operators can use to claim devices.
- **Workload operator**: responsible for deploying and managing workloads in the
  cluster. To use DRA to allocate devices to Pods, workload operators do the following:

  - Create ResourceClaims or ResourceClaimTemplates to request specific
    configurations within DeviceClasses.
  - Deploy workloads that use specific ResourceClaims or ResourceClaimTemplates.