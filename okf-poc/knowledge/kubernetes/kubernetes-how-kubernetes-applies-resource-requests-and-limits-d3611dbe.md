---
id: kubernetes-how-kubernetes-applies-resource-requests-and-limits-d3611dbe
type: concept
title: How Kubernetes applies resource requests and limits
description: When the kubelet starts a container as part of a Pod, the kubelet passes
  that container's
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/
updated_at: '2026-08-13'
created_at: '2026-08-13'
---

## How Kubernetes applies resource requests and limits

When the kubelet starts a container as part of a Pod, the kubelet passes that container's
requests and limits for memory and CPU to the container runtime.

On Linux, the container runtime typically configures
kernel [cgroups](https://kubernetes.io/docs/reference/glossary/?all=true#term-cgroup "A group of Linux processes with optional resource isolation, accounting and limits.") that apply and enforce the
limits you defined.

- The CPU limit defines a hard ceiling on how much CPU time the container can use.
  During each scheduling interval (time slice), the Linux kernel checks to see if this
  limit is exceeded; if so, the kernel waits before allowing that cgroup to resume execution.
- The CPU request typically defines a weighting. If several different containers (cgroups)
  want to run on a contended system, workloads with larger CPU requests are allocated more
  CPU time than workloads with small requests.
- The memory request is mainly used during (Kubernetes) Pod scheduling. On a node that uses
  cgroups v2, the container runtime might use the memory request as a hint to set
  `memory.min` and `memory.low`.
- The memory limit defines a memory limit for that cgroup. If the container tries to
  allocate more memory than this limit, the Linux kernel out-of-memory subsystem activates
  and, typically, intervenes by stopping one of the processes in the container that tried
  to allocate memory. If that process is the container's PID 1, and the container is marked
  as restartable, Kubernetes restarts the container.
- The memory limit for the Pod or container can also apply to pages in memory backed
  volumes, such as an `emptyDir`. The kubelet tracks `tmpfs` emptyDir volumes as container
  memory use, rather than as local [ephemeral storage](https://kubernetes.io/docs/concepts/storage/ephemeral-storage/).
  When using memory backed `emptyDir`,
  be sure to check the notes [below](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/#memory-backed-emptydir).

If a container exceeds its memory request and the node that it runs on becomes short of
memory overall, it is likely that the Pod the container belongs to will be
[evicted](https://kubernetes.io/docs/concepts/scheduling-eviction/ "Process of terminating one or more Pods on Nodes").

A container might or might not be allowed to exceed its CPU limit for extended periods of time.
However, container runtimes don't terminate Pods or containers for excessive CPU usage.

To determine whether a container cannot be scheduled or is being killed due to resource limits,
see the [Troubleshooting](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/#troubleshooting) section.