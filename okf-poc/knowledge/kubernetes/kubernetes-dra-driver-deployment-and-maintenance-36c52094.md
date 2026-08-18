---
id: kubernetes-dra-driver-deployment-and-maintenance-36c52094
type: concept
title: DRA driver deployment and maintenance
description: DRA drivers are third-party applications that run on each node of your
  cluster
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/cluster-administration/dra/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

## DRA driver deployment and maintenance

DRA drivers are third-party applications that run on each node of your cluster
to interface with the hardware of that node and Kubernetes' native DRA
components. The installation procedure depends on the driver you choose, but is
likely deployed as a DaemonSet to all or a selection of the nodes (using node
selectors or similar mechanisms) in your cluster.