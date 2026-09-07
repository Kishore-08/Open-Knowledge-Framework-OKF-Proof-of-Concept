---
id: kubernetes-deviceclass-c976d546
type: concept
title: DeviceClass
description: A DeviceClass lets cluster admins or device drivers define categories
  of devices
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/resource-management/dynamic-resource-allocation/dra-api/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

### DeviceClass

A DeviceClass lets cluster admins or device drivers define categories of devices
in the cluster. DeviceClasses tell operators what devices they can request and
how they can request those devices. You can use
[common expression language (CEL)](https://cel.dev) to select devices based on
specific attributes. A ResourceClaim that references the DeviceClass can then
request specific configurations within the DeviceClass.

To create a DeviceClass, see
[Set Up DRA in a Cluster](https://kubernetes.io/docs/tasks/configure-pod-container/assign-resources/set-up-dra-cluster/).