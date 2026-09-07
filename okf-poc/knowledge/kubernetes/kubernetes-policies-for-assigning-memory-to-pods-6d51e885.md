---
id: kubernetes-policies-for-assigning-memory-to-pods-6d51e885
type: concept
title: Policies for assigning memory to Pods
description: The Kubernetes *Memory Manager* allocates RAM (memory, and optionally
  Linux huge pages) resources
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/resource-management/resource-managers/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

### Policies for assigning memory to Pods

The Kubernetes *Memory Manager* allocates RAM (memory, and optionally Linux huge pages) resources
for pods in the `Guaranteed` [QoS class](https://kubernetes.io/docs/concepts/workloads/pods/pod-qos/ "QoS Class (Quality of Service Class) provides a way for Kubernetes to classify pods within the cluster into several classes and make decisions about scheduling and eviction.").

The Memory Manager employs hint generation protocol to yield the most suitable NUMA affinity for a pod.
The Memory Manager feeds the central manager (*Topology Manager*) with these affinity hints.
Based on both the hints and Topology Manager policy, the pod is rejected or admitted to the node.

Moreover, the Memory Manager ensures that the memory which a pod requests
is allocated from a minimum number of NUMA nodes.

To learn more, read [Control Memory Management Policies on a Node](https://kubernetes.io/docs/tasks/administer-cluster/memory-manager/).