---
id: kubernetes-manual-node-administration-5445bee6
type: concept
title: Manual Node administration
description: You can create and modify Node objects using
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/architecture/nodes/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Manual Node administration

You can create and modify Node objects using
[kubectl](https://kubernetes.io/docs/reference/kubectl/ "A command line tool for communicating with a Kubernetes cluster.").

When you want to create Node objects manually, set the kubelet flag `--register-node=false`.

You can modify Node objects regardless of the setting of `--register-node`.
For example, you can set labels on an existing Node or mark it unschedulable.

You can set optional node role(s) for nodes by adding one or more `node-role.kubernetes.io/<role>: <role>` labels to the node where characters of `<role>`
are limited by the [syntax](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#syntax-and-character-set) rules for labels.

Kubernetes ignores the label value for node roles; by convention, you can set it to the same string you used for the node role in the label key.

You can use labels on Nodes in conjunction with node selectors on Pods to control
scheduling. For example, you can constrain a Pod to only be eligible to run on
a subset of the available nodes.

Marking a node as unschedulable prevents the scheduler from placing new pods onto
that Node but does not affect existing Pods on the Node. This is useful as a
preparatory step before a node reboot or other maintenance.

To mark a Node unschedulable, run:

```
kubectl cordon $NODENAME
```

See [Safely Drain a Node](https://kubernetes.io/docs/tasks/administer-cluster/safely-drain-node/)
for more details.

#### Note:

Pods that are part of a [DaemonSet](https://kubernetes.io/docs/concepts/workloads/controllers/daemonset "Ensures a copy of a Pod is running across a set of nodes in a cluster.") tolerate
being run on an unschedulable Node. DaemonSets typically provide node-local services
that should run on the Node even if it is being drained of workload applications.