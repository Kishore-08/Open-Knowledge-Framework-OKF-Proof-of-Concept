---
id: kubernetes-assigning-pods-to-nodes-37b2614a
type: concept
title: Assigning Pods to Nodes
description: You can constrain a [Pod](https://kubernetes.io/docs/concepts/workloads/pods/
  "A Pod represents a set of running containers in your cluster.") so that it is
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

# Assigning Pods to Nodes

You can constrain a [Pod](https://kubernetes.io/docs/concepts/workloads/pods/ "A Pod represents a set of running containers in your cluster.") so that it is
*restricted* to run on particular [node(s)](https://kubernetes.io/docs/concepts/architecture/nodes/ "A node is a worker machine in Kubernetes."),
or to *prefer* to run on particular nodes.
There are several ways to do this and the recommended approaches all use
[label selectors](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/) to facilitate the selection.
Often, you do not need to set any such constraints; the
[scheduler](https://kubernetes.io/docs/reference/command-line-tools-reference/kube-scheduler/ "Control plane component that watches for newly created pods with no assigned node, and selects a node for them to run on.") will automatically do a reasonable placement
(for example, spreading your Pods across nodes so as not place Pods on a node with insufficient free resources).
However, there are some circumstances where you may want to control which node
the Pod deploys to, for example, to ensure that a Pod ends up on a node with an SSD attached to it,
or to co-locate Pods from two different services that communicate a lot into the same availability zone.

You can use any of the following methods to choose where Kubernetes schedules
specific Pods:

- [nodeSelector](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#nodeselector) field matching against [node labels](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#built-in-node-labels)
- [Affinity and anti-affinity](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#affinity-and-anti-affinity)
- [nodeName](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#nodename) field
- [Pod topology spread constraints](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#pod-topology-spread-constraints)