---
id: kubernetes-node-consolidation-1d739c98
type: concept
title: Node consolidation
description: The main consideration when running a cluster is ensuring that all schedulable
  pods are running,
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/cluster-administration/node-autoscaling/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

## Node consolidation

The main consideration when running a cluster is ensuring that all schedulable pods are running,
whilst keeping the cost of the cluster as low as possible. To achieve this, the Pods' resource
requests should utilize as much of the Nodes' resources as possible. From this perspective, the
overall Node utilization in a cluster can be used as a proxy for how cost-effective the cluster is.

#### Note:

Correctly setting the resource requests of your Pods is as important to the overall
cost-effectiveness of a cluster as optimizing Node utilization.
Combining Node autoscaling with [vertical workload autoscaling](https://kubernetes.io/docs/concepts/cluster-administration/node-autoscaling/#vertical-workload-autoscaling) can
help you achieve this.

Nodes in your cluster can be automatically *consolidated* in order to improve the overall Node
utilization, and in turn the cost-effectiveness of the cluster. Consolidation happens through
removing a set of underutilized Nodes from the cluster. Optionally, a different set of Nodes can
be [provisioned](https://kubernetes.io/docs/concepts/cluster-administration/node-autoscaling/#provisioning) to replace them.

Consolidation, like provisioning, only considers Pod resource requests and not real resource usage
when making decisions.

For the purpose of consolidation, a Node is considered *empty* if it only has DaemonSet and static
Pods running on it. Removing empty Nodes during consolidation is more straightforward than non-empty
ones, and autoscalers often have optimizations designed specifically for consolidating empty Nodes.

Removing non-empty Nodes during consolidation is disruptive—the Pods running on them are
terminated, and possibly have to be recreated (for example by a Deployment). However, all such
recreated Pods should be able to schedule on existing Nodes in the cluster, or the replacement Nodes
provisioned as part of consolidation. **No Pods should normally become pending as a result of
consolidation.**

#### Note:

Autoscalers predict how a recreated Pod will likely be scheduled after a Node is provisioned or
consolidated, but they don't control the actual scheduling. Because of this, some Pods might
become pending as a result of consolidation - if for example a completely new Pod appears while
consolidation is being performed.

Autoscaler configuration may also enable triggering consolidation by other conditions (for example,
the time elapsed since a Node was created), in order to optimize different properties (for example,
the maximum lifespan of Nodes in a cluster).

The details of how consolidation is performed depend on the configuration of a given autoscaler.

#### Note:

Consolidation was formerly known as *scale-down* in Cluster Autoscaler.