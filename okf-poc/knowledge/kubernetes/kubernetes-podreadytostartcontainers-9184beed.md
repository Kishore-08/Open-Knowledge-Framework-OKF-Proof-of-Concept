---
id: kubernetes-podreadytostartcontainers-9184beed
type: concept
title: PodReadyToStartContainers
description: 'FEATURE STATE:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/pods/pod-condition/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

### PodReadyToStartContainers

FEATURE STATE:
`Kubernetes v1.37 [stable]`(enabled by default)

#### Note:

During its early development, this condition was named `PodHasNetwork`.

After a Pod gets scheduled on a node, it needs to be admitted by the kubelet
and to have any required storage volumes mounted. Once these phases are complete,
the kubelet works with a container runtime
(using [Container Runtime Interface (CRI)](https://kubernetes.io/docs/concepts/architecture/cri "Protocol for communication between the kubelet and the local container runtime."))
to set up a runtime sandbox and configure networking for the Pod.
The `PodReadyToStartContainers` condition is added to the `status.conditions` field of a Pod.

The condition is set to `False` by the kubelet when it detects a Pod does not have a runtime sandbox with networking configured. This occurs in the following scenarios:

- Early in the lifecycle of the Pod, when the kubelet has not yet begun to set up a sandbox for the Pod using the container runtime.
- Later in the lifecycle of the Pod, when the Pod sandbox has been destroyed due to either:
  - the node rebooting, without the Pod getting evicted
  - for container runtimes that use virtual machines for isolation, the Pod sandbox virtual machine rebooting, which then requires creating a new sandbox and fresh container network configuration.

The `PodReadyToStartContainers` condition is set to `True` by the kubelet after the successful completion of sandbox creation and network configuration for the Pod by the runtime plugin. The kubelet can start pulling container images and create containers after `PodReadyToStartContainers` condition has been set to `True`.

For a Pod with init containers, the kubelet sets the `Initialized` condition to `True` after the init containers have successfully completed (which happens after successful sandbox creation and network configuration by the runtime plugin). For a Pod without init containers, the kubelet sets the `Initialized` condition to `True` before sandbox creation and network configuration starts.

## Other Pod conditions

The following conditions are not part of the normal Pod lifecycle progression.
They are set in response to specific operations or events.