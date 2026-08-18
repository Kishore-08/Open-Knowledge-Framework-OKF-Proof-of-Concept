---
id: kubernetes-lifecycle-pod-conditions-9184beed
type: concept
title: Lifecycle Pod conditions
description: 'As a Pod progresses through its lifecycle, the kubelet sets the following
  conditions roughly in this order:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/pods/pod-condition/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

## Lifecycle Pod conditions

As a Pod progresses through its lifecycle, the kubelet sets the following conditions roughly in this order:

1. `PodScheduled`: the Pod has been scheduled to a node.
2. `PodReadyToStartContainers`: the Pod sandbox has been successfully created and networking configured. The sandbox and network are set up by the [container runtime](https://kubernetes.io/docs/setup/production-environment/container-runtimes "The container runtime is the software that is responsible for running containers.") and [CNI](https://kubernetes.io/docs/concepts/extend-kubernetes/compute-storage-net/network-plugins/ "Container network interface (CNI) plugins are a type of Network plugin that adheres to the appc/CNI specification.") plugin.
3. `Initialized`: all [init containers](https://kubernetes.io/docs/concepts/workloads/pods/init-containers/) have completed successfully. For a Pod without init containers, this is set to `True` before sandbox creation.
4. `ContainersReady`: all containers in the Pod are ready. A container's readiness is determined by its [readiness probe](https://kubernetes.io/docs/concepts/workloads/pods/probes/#readiness-probe), if configured.
5. `Ready`: the Pod is able to serve requests and should be added to the load balancing pools of all matching [Services](https://kubernetes.io/docs/concepts/services-networking/service/). Pods that are not `Ready` are removed from Service endpoints.

#### Note:

The `Ready` condition depends on more than just `ContainersReady`. If the Pod specifies `readinessGates`, all of those custom conditions must also be `True` for the Pod to be `Ready`. See [Pod readiness](https://kubernetes.io/docs/concepts/workloads/pods/pod-condition/#enhanced-pod-readiness) for details.

You can inspect a Pod's conditions using kubectl:

```
kubectl get pod <pod-name> -o yaml
```

The following shows what `status.conditions` looks like for a running Pod:

```
status:
  conditions:
    - type: PodScheduled
      status: "True"
      lastProbeTime: null
      lastTransitionTime: "2026-03-29T08:52:21Z"
      observedGeneration: 1
    - type: PodReadyToStartContainers
      status: "True"
      lastProbeTime: null
      lastTransitionTime: "2026-04-11T06:02:16Z"
      observedGeneration: 1
    - type: Initialized
      status: "True"
      lastProbeTime: null
      lastTransitionTime: "2026-03-29T08:52:21Z"
      observedGeneration: 1
    - type: ContainersReady
      status: "True"
      lastProbeTime: null
      lastTransitionTime: "2026-04-11T06:02:45Z"
      observedGeneration: 1
    - type: Ready
      status: "True"
      lastProbeTime: null
      lastTransitionTime: "2026-04-11T06:02:45Z"
      observedGeneration: 1
```