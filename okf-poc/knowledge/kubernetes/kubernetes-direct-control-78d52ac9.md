---
id: kubernetes-direct-control-78d52ac9
type: concept
title: Direct control
description: In contrast with Job, some controllers need to make changes to
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/architecture/controller/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Direct control

In contrast with Job, some controllers need to make changes to
things outside of your cluster.

For example, if you use a control loop to make sure there
are enough [Nodes](https://kubernetes.io/docs/concepts/architecture/nodes/ "A node is a worker machine in Kubernetes.")
in your cluster, then that controller needs something outside the
current cluster to set up new Nodes when needed.

Controllers that interact with external state find their desired state from
the API server, then communicate directly with an external system to bring
the current state closer in line.

(There actually is a [controller](https://github.com/kubernetes/autoscaler/)
that horizontally scales the nodes in your cluster.)

The important point here is that the controller makes some changes to bring about
your desired state, and then reports the current state back to your cluster's API server.
Other control loops can observe that reported data and take their own actions.

In the thermostat example, if the room is very cold then a different controller
might also turn on a frost protection heater. With Kubernetes clusters, the control
plane indirectly works with IP address management tools, storage services,
cloud provider APIs, and other services by
[extending Kubernetes](https://kubernetes.io/docs/concepts/extend-kubernetes/) to implement that.