---
id: kubernetes-leader-election-4557d362
type: concept
title: Leader election
description: Kubernetes also uses Leases to ensure only one instance of a component
  is running at any given time.
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/architecture/leases/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

## Leader election

Kubernetes also uses Leases to ensure only one instance of a component is running at any given time.
This is used by control plane components like `kube-controller-manager` and `kube-scheduler` in
HA configurations, where only one instance of the component should be actively running while the other
instances are on stand-by.

Read [coordinated leader election](https://kubernetes.io/docs/concepts/cluster-administration/coordinated-leader-election/)
to learn about how Kubernetes builds on the Lease API to select which component instance
acts as leader.