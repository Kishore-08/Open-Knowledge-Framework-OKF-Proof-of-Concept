---
id: kubernetes-horizontal-workload-autoscaling-1d739c98
type: concept
title: Horizontal workload autoscaling
description: Node autoscaling usually works in response to Pods—it provisions new
  Nodes to accommodate
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/cluster-administration/node-autoscaling/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Horizontal workload autoscaling

Node autoscaling usually works in response to Pods—it provisions new Nodes to accommodate
unschedulable Pods, and then consolidates the Nodes once they're no longer needed.

[Horizontal workload autoscaling](https://kubernetes.io/docs/concepts/workloads/autoscaling/#scaling-workloads-horizontally)
automatically scales the number of workload replicas to maintain a desired average resource
utilization across the replicas. In other words, it automatically creates new Pods in response to
application load, and then removes the Pods once the load decreases.

You can use Node autoscaling together with horizontal workload autoscaling to autoscale the Nodes in
your cluster based on the average real resource utilization of your Pods.

If the application load increases, the average utilization of its Pods should also increase,
prompting workload autoscaling to create new Pods. Node autoscaling should then provision new Nodes
to accommodate the new Pods.

Once the application load decreases, workload autoscaling should remove unnecessary Pods. Node
autoscaling should, in turn, consolidate the Nodes that are no longer needed.

If configured correctly, this pattern ensures that your application always has the Node capacity to
handle load spikes if needed, but you don't have to pay for the capacity when it's not needed.