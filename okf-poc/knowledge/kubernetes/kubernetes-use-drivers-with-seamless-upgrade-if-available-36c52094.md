---
id: kubernetes-use-drivers-with-seamless-upgrade-if-available-36c52094
type: concept
title: Use drivers with seamless upgrade if available
description: DRA drivers implement the [`kubeletplugin` package
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/cluster-administration/dra/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

### Use drivers with seamless upgrade if available

DRA drivers implement the [`kubeletplugin` package
interface](https://pkg.go.dev/k8s.io/dynamic-resource-allocation/kubeletplugin).
Your driver may support *seamless upgrades* by implementing a property of this
interface that allows two versions of the same DRA driver to coexist for a short
time. This is only available for kubelet versions 1.33 and above and may not be
supported by your driver for heterogeneous clusters with attached nodes running
older versions of Kubernetes - check your driver's documentation to be sure.

If seamless upgrades are available for your situation, consider using it to
minimize scheduling delays when your driver updates.

If you cannot use seamless upgrades, during driver downtime for upgrades you may
observe that:

- Pods cannot start unless the claims they depend on were already prepared for
  use.
- Cleanup after the last pod which used a claim gets delayed until the driver is
  available again. The pod is not marked as terminated. This prevents reusing
  the resources used by the pod for other pods.
- Running pods will continue to run.