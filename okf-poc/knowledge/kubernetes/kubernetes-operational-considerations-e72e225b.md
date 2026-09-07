---
id: kubernetes-operational-considerations-e72e225b
type: concept
title: Operational considerations
description: Because the `skipNodeOperations` setting is copied from the ResourceSlice
  into
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/resource-management/dynamic-resource-allocation/dra-features/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

### Operational considerations

#### In-place driver updates

Because the `skipNodeOperations` setting is copied from the ResourceSlice into
the ResourceClaim at allocation time, running Pods and active allocations
retain whatever setting was in place when they were scheduled.

If a driver's node operation requirements are updated in place (for example,
changing from requiring node operations to skipping them), existing claims will
still use the previous configuration. To avoid issues—such as terminating Pods
hanging while waiting for a decommissioned node plugin—cluster administrators
should ensure no active claims exist for a driver before altering its node
operation requirements or removing node-local driver DaemonSets.

#### Node declared features integration

To prevent Pods from being scheduled onto nodes where the `kubelet` does not
support skipping DRA operations (which would cause the `kubelet` to fail while
waiting for a missing node plugin), this feature integrates with [Node Declared
Features](https://kubernetes.io/docs/concepts/scheduling-eviction/node-declared-features/). When a
Pod uses a ResourceClaim with `skipNodeOperations` configured, the Kubernetes
scheduler verifies that the target node declares support for the
`DRAOptionalNodeOperations` feature in its `.status.declaredFeatures` before
scheduling the Pod.

Optional node operations is controlled by the
[`DRAOptionalNodeOperations`](https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/#DRAOptionalNodeOperations)
feature gate in the `kube-apiserver`, `kube-scheduler`, and `kubelet`.