---
id: kubernetes-deployments-b7b8ba42
type: concept
title: Deployments
description: DaemonSets are similar to [Deployments](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/)
  in that
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

### Deployments

DaemonSets are similar to [Deployments](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/) in that
they both create Pods, and those Pods have processes which are not expected to terminate (e.g. web servers,
storage servers).

Use a Deployment for stateless services, like frontends, where scaling up and down the
number of replicas and rolling out updates are more important than controlling exactly which host
the Pod runs on. Use a DaemonSet when it is important that a copy of a Pod always run on
all or certain hosts, if the DaemonSet provides node-level functionality that allows other Pods to run correctly on that particular node.

For example, [network plugins](https://kubernetes.io/docs/concepts/extend-kubernetes/compute-storage-net/network-plugins/) often include a component that runs as a DaemonSet. The DaemonSet component makes sure that the node where it's running has working cluster networking.