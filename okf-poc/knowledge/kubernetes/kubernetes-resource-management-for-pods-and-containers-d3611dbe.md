---
id: kubernetes-resource-management-for-pods-and-containers-d3611dbe
type: concept
title: Resource Management for Pods and Containers
description: When you specify a [Pod](https://kubernetes.io/docs/concepts/workloads/pods/
  "A Pod represents a set of running containers in your cluster."), you can optionally
  specify how much of each resource a
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

# Resource Management for Pods and Containers

When you specify a [Pod](https://kubernetes.io/docs/concepts/workloads/pods/ "A Pod represents a set of running containers in your cluster."), you can optionally specify how much of each resource a
[container](https://kubernetes.io/docs/concepts/containers/ "A lightweight and portable executable image that contains software and all of its dependencies.") needs. The most common resources to specify are CPU and memory
(RAM); there are others.

When you specify the resource *request* for containers in a Pod, the
[kube-scheduler](https://kubernetes.io/docs/reference/command-line-tools-reference/kube-scheduler/ "Control plane component that watches for newly created pods with no assigned node, and selects a node for them to run on.") uses this information to decide which node to place the Pod on.
When you specify a resource *limit* for a container, the [kubelet](https://kubernetes.io/docs/reference/command-line-tools-reference/kubelet "An agent that runs on each node in the cluster. It makes sure that containers are running in a pod.") enforces those
limits so that the running container is not allowed to use more of that resource
than the limit you set. The kubelet also reserves at least the *request* amount of
that system resource specifically for that container to use.