---
id: kubernetes-node-controller-8c98aece
type: concept
title: Node controller
description: The node controller is responsible for updating [Node](https://kubernetes.io/docs/concepts/architecture/nodes/
  "A node is a worker machine in Kubernetes.") objects
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/architecture/cloud-controller/
updated_at: '2026-08-13'
created_at: '2026-08-13'
---

### Node controller

The node controller is responsible for updating [Node](https://kubernetes.io/docs/concepts/architecture/nodes/ "A node is a worker machine in Kubernetes.") objects
when new servers are created in your cloud infrastructure. The node controller obtains information about the
hosts running inside your tenancy with the cloud provider. The node controller performs the following functions:

1. Update a Node object with the corresponding server's unique identifier obtained from the cloud provider API.
2. Annotating and labelling the Node object with cloud-specific information, such as the region the node
   is deployed into and the resources (CPU, memory, etc) that it has available.
3. Obtain the node's hostname and network addresses.
4. Verifying the node's health. In case a node becomes unresponsive, this controller checks with
   your cloud provider's API to see if the server has been deactivated / deleted / terminated.
   If the node has been deleted from the cloud, the controller deletes the Node object from your Kubernetes
   cluster.

Some cloud provider implementations split this into a node controller and a separate node
lifecycle controller.