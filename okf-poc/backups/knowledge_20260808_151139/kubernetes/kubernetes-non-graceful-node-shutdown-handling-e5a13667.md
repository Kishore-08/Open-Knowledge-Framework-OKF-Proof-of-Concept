---
id: kubernetes-non-graceful-node-shutdown-handling-e5a13667
type: concept
title: Non-graceful node shutdown handling
description: 'FEATURE STATE:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/cluster-administration/node-shutdown/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

## Non-graceful node shutdown handling

FEATURE STATE:
`Kubernetes v1.28 [stable]`(enabled by default)

A node shutdown action may not be detected by kubelet's Node Shutdown Manager,
either because the command does not trigger the inhibitor locks mechanism used by
kubelet or because of a user error, i.e., the ShutdownGracePeriod and
ShutdownGracePeriodCriticalPods are not configured properly. Please refer to above
section [Graceful Node Shutdown](https://kubernetes.io/docs/concepts/cluster-administration/node-shutdown/#graceful-node-shutdown) for more details.

When a node is shutdown but not detected by kubelet's Node Shutdown Manager, the pods
that are part of a [StatefulSet](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/ "A StatefulSet manages deployment and scaling of a set of Pods, with durable storage and persistent identifiers for each Pod.")
will be stuck in terminating status on the shutdown node and cannot move to a new running node.
This is because kubelet on the shutdown node is not available to delete the pods so
the StatefulSet cannot create a new pod with the same name. If there are volumes used by the pods,
the VolumeAttachments will not be deleted from the original shutdown node so the volumes
used by these pods cannot be attached to a new running node. As a result, the
application running on the StatefulSet cannot function properly. If the original
shutdown node comes up, the pods will be deleted by kubelet and new pods will be
created on a different running node. If the original shutdown node does not come up,
these pods will be stuck in terminating status on the shutdown node forever.

To mitigate the above situation, a user can manually add the taint `node.kubernetes.io/out-of-service`
with either `NoExecute` or `NoSchedule` effect to a Node marking it out-of-service.
If a Node is marked out-of-service with this taint, the pods on the node will be forcefully deleted
if there are no matching tolerations on it and volume detach operations for the pods terminating on
the node will happen immediately. This allows the Pods on the out-of-service node to recover quickly
on a different node.

During a non-graceful shutdown, Pods are terminated in the two phases:

1. Force delete the Pods that do not have matching `out-of-service` tolerations.
2. Immediately perform detach volume operation for such pods.

#### Note:

- Before adding the taint `node.kubernetes.io/out-of-service`, it should be verified
  that the node is already in shutdown or power off state (not in the middle of restarting).
- The user is required to manually remove the out-of-service taint after the pods are
  moved to a new node and the user has checked that the shutdown node has been
  recovered since the user was the one who originally added the taint.