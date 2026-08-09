---
id: kubernetes-pod-readiness-to-start-containers-3e34f258
type: concept
title: Pod readiness to start containers
description: 'FEATURE STATE:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Pod readiness to start containers

FEATURE STATE:
`Kubernetes v1.29 [beta]`

#### Note:

During its early development, this condition was named `PodHasNetwork`.

After a Pod gets scheduled on a node, it needs to be admitted by the kubelet and
to have any required storage volumes mounted. Once these phases are complete,
the kubelet works with
a container runtime (using [Container Runtime Interface (CRI)](https://kubernetes.io/docs/concepts/architecture/cri "Protocol for communication between the kubelet and the local container runtime.")) to set up a
runtime sandbox and configure networking for the Pod. If the Pod uses
[Dynamic Resource Allocation](https://kubernetes.io/docs/concepts/scheduling-eviction/dynamic-resource-allocation/),
those resources are also allocated during this phase.
If the `PodReadyToStartContainersCondition`
[feature gate](https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/) is enabled
(it is enabled by default for Kubernetes 1.36), the
`PodReadyToStartContainers` condition will be added to the `status.conditions` field of a Pod.

The `PodReadyToStartContainers` condition is set to `False` by the kubelet when it detects a
Pod does not have a runtime sandbox with networking configured. This occurs in
the following scenarios:

- Early in the lifecycle of the Pod, when the kubelet has not yet begun to set up a sandbox for
  the Pod using the container runtime.
- Later in the lifecycle of the Pod, when the Pod sandbox has been destroyed due to either:
  - the node rebooting, without the Pod getting evicted
  - for container runtimes that use virtual machines for isolation, the Pod
    sandbox virtual machine rebooting, which then requires creating a new sandbox and
    fresh container network configuration.

After sandbox creation, network configuration, volume mounting, and (if requested) dynamic resource
allocation are complete, the kubelet sets the `PodReadyToStartContainers` condition to `True`.
Image pulling and container creation occur after this point.

For a Pod with init containers, the kubelet sets the `Initialized` condition to
`True` after the init containers have successfully completed (which happens
after successful sandbox creation and network configuration by the runtime
plugin). For a Pod without init containers, the kubelet sets the `Initialized`
condition to `True` before sandbox creation and network configuration starts.