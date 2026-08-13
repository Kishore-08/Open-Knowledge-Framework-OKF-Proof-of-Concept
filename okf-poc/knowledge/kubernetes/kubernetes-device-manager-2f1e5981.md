---
id: kubernetes-device-manager-2f1e5981
type: concept
title: Device manager
description: 'FEATURE STATE:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/resource-managers/
updated_at: '2026-08-13'
created_at: '2026-08-13'
---

## Device manager

FEATURE STATE:
`Kubernetes v1.26 [stable]`

*Device Manager* is a kubelet component that allocates hardware devices to pods
using the device plugin API. It consults with the Topology Manager, using
topology information provided by device plugins, to make resource assignment
decisions. To learn more, read
[Device Plugin Integration with the Topology Manager](https://kubernetes.io/docs/concepts/extend-kubernetes/compute-storage-net/device-plugins/#device-plugin-integration-with-the-topology-manager).