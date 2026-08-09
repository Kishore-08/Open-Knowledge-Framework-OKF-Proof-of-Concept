---
id: kubernetes-node-isolation-restriction-37b2614a
type: concept
title: Node isolation/restriction
description: Adding labels to nodes allows you to target Pods for scheduling on specific
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Node isolation/restriction

Adding labels to nodes allows you to target Pods for scheduling on specific
nodes or groups of nodes. You can use this functionality to ensure that specific
Pods only run on nodes with certain isolation, security, or regulatory
properties.

If you use labels for node isolation, choose label keys that the [kubelet](https://kubernetes.io/docs/reference/command-line-tools-reference/kubelet "An agent that runs on each node in the cluster. It makes sure that containers are running in a pod.")
cannot modify. This prevents a compromised node from setting those labels on
itself so that the scheduler schedules workloads onto the compromised node.

The [`NodeRestriction` admission plugin](https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers/#noderestriction)
prevents the kubelet from setting or modifying labels with a
`node-restriction.kubernetes.io/` prefix.

To make use of that label prefix for node isolation:

1. Ensure you are using the [Node authorizer](https://kubernetes.io/docs/reference/access-authn-authz/node/) and have *enabled* the `NodeRestriction` admission plugin.
2. Add labels with the `node-restriction.kubernetes.io/` prefix to your nodes, and use those labels in your [node selectors](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#nodeselector).
   For example, `example.com.node-restriction.kubernetes.io/fips=true` or `example.com.node-restriction.kubernetes.io/pci-dss=true`.