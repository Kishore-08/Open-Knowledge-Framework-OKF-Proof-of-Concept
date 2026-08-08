---
id: kubernetes-nodes-to-report-swap-capacity-as-part-of-node-status-9edb5061
type: concept
title: Nodes to report swap capacity as part of node status
description: A new node status field is now added, `node.status.nodeInfo.swap.capacity`,
  to report the swap capacity of a node.
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/cluster-administration/swap-memory-management/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Nodes to report swap capacity as part of node status

A new node status field is now added, `node.status.nodeInfo.swap.capacity`, to report the swap capacity of a node.

As an example, the following command can be used to retrieve the swap capacity of the nodes in a cluster:

```
kubectl get nodes -o go-template='{{range .items}}{{.metadata.name}}: {{if .status.nodeInfo.swap.capacity}}{{.status.nodeInfo.swap.capacity}}{{else}}<unknown>{{end}}{{"\n"}}{{end}}'
```

This will result in an output similar to:

```
node1: 21474836480
node2: 42949664768
node3: <unknown>
```

#### Note:

The `<unknown>` value indicates that the `.status.nodeInfo.swap.capacity` field is not set for that Node.
This probably means that the node does not have swap provisioned, or less likely,
that the kubelet is not able to determine the swap capacity of the node.