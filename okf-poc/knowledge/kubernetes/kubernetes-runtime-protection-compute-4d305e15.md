---
id: kubernetes-runtime-protection-compute-4d305e15
type: concept
title: 'Runtime protection: compute'
description: '[Containers](https://kubernetes.io/docs/concepts/containers/ "A lightweight
  and portable executable image that contains software and all of its dependencies.")
  provide two'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/security/cloud-native-security/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Runtime protection: compute

[Containers](https://kubernetes.io/docs/concepts/containers/ "A lightweight and portable executable image that contains software and all of its dependencies.") provide two
things: isolation between applications and a mechanism to combine
those isolated applications to run on the same host computer. Those two
aspects—isolation and aggregation—mean that runtime security involves
identifying trade-offs and finding an appropriate balance.

Kubernetes relies on a [container runtime](https://kubernetes.io/docs/setup/production-environment/container-runtimes "The container runtime is the software that is responsible for running containers.")
to set up and run containers. The Kubernetes project does
not recommend a specific container runtime, and you should make sure that
the runtime(s) you choose meet your information security needs.

To protect your compute at runtime, you can:

1. Enforce [Pod Security Standards](https://kubernetes.io/docs/concepts/security/pod-security-standards/)
   for applications to help ensure they run with only the necessary privileges.
2. Run a specialized operating system on your nodes that is designed specifically
   for running containerized workloads. This is typically based on a read-only
   operating system (*immutable image*) that provides only the services
   essential for running containers.

   Container-specific operating systems help isolate system components and
   present a reduced attack surface in case of a container escape.
3. Define [ResourceQuotas](https://kubernetes.io/docs/concepts/policy/resource-quotas/) to
   fairly allocate shared resources, and use
   mechanisms such as [LimitRanges](https://kubernetes.io/docs/concepts/policy/limit-range/)
   to ensure that Pods specify their resource requirements.
4. Partition workloads across different nodes to improve isolation.
   Use [node isolation](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#node-isolation-restriction)
   mechanisms, either from Kubernetes itself or from the ecosystem, to ensure that
   Pods with different trust contexts run on separate sets of nodes.
5. Use a [container runtime](https://kubernetes.io/docs/setup/production-environment/container-runtimes "The container runtime is the software that is responsible for running containers.")
   that provides security restrictions.
6. On Linux nodes, use a Linux security module such as [AppArmor](https://kubernetes.io/docs/tutorials/security/apparmor/)
   or [seccomp](https://kubernetes.io/docs/tutorials/security/seccomp/).