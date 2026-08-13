---
id: kubernetes-what-s-next-8c98aece
type: concept
title: What's next
description: '- [Cloud Controller Manager Administration](https://kubernetes.io/docs/tasks/administer-cluster/running-cloud-controller/#cloud-controller-manager)'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/architecture/cloud-controller/
updated_at: '2026-08-13'
created_at: '2026-08-13'
---

## What's next

- [Cloud Controller Manager Administration](https://kubernetes.io/docs/tasks/administer-cluster/running-cloud-controller/#cloud-controller-manager)
  has instructions on running and managing the cloud controller manager.
- To upgrade a HA control plane to use the cloud controller manager, see
  [Migrate Replicated Control Plane To Use Cloud Controller Manager](https://kubernetes.io/docs/tasks/administer-cluster/controller-manager-leader-migration/).
- Want to know how to implement your own cloud controller manager, or extend an existing project?

  - The cloud controller manager uses Go interfaces, specifically, `CloudProvider` interface defined in
    [`cloud.go`](https://github.com/kubernetes/cloud-provider/blob/release-1.21/cloud.go#L42-L69)
    from [kubernetes/cloud-provider](https://github.com/kubernetes/cloud-provider) to allow
    implementations from any cloud to be plugged in.
  - The implementation of the shared controllers highlighted in this document (Node, Route, and Service),
    and some scaffolding along with the shared cloudprovider interface, is part of the Kubernetes core.
    Implementations specific to cloud providers are outside the core of Kubernetes and implement
    the `CloudProvider` interface.
  - For more information about developing plugins,
    see [Developing Cloud Controller Manager](https://kubernetes.io/docs/tasks/administer-cluster/developing-cloud-controller-manager/).