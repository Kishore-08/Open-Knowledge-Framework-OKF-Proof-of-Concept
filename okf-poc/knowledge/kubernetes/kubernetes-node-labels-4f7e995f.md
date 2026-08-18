---
id: kubernetes-node-labels-4f7e995f
type: concept
title: Node labels
description: Topology spread constraints rely on node labels to identify the topology
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/scheduling-eviction/topology-spread-constraints/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

### Node labels

Topology spread constraints rely on node labels to identify the topology
domain(s) that each [node](https://kubernetes.io/docs/concepts/architecture/nodes/ "A node is a worker machine in Kubernetes.") is in.
For example, a node might have labels:

```
  region: us-east-1
  zone: us-east-1a
```

#### Note:

For brevity, this example doesn't use the
[well-known](https://kubernetes.io/docs/reference/labels-annotations-taints/) label keys
`topology.kubernetes.io/zone` and `topology.kubernetes.io/region`. However,
those registered label keys are nonetheless recommended rather than the private
(unqualified) label keys `region` and `zone` that are used here.

You can't make a reliable assumption about the meaning of a private label key
between different contexts.

Suppose you have a 4-node cluster with the following labels:

```
NAME    STATUS   ROLES    AGE     VERSION   LABELS
node1   Ready    <none>   4m26s   v1.16.0   node=node1,zone=zoneA
node2   Ready    <none>   3m58s   v1.16.0   node=node2,zone=zoneA
node3   Ready    <none>   3m17s   v1.16.0   node=node3,zone=zoneB
node4   Ready    <none>   2m43s   v1.16.0   node=node4,zone=zoneB
```

Then the cluster is logically viewed as below:

```
graph TB
    subgraph "zoneB"
        n3(Node3)
        n4(Node4)
    end
    subgraph "zoneA"
        n1(Node1)
        n2(Node2)
    end

    classDef plain fill:#ddd,stroke:#fff,stroke-width:4px,color:#000;
    classDef k8s fill:#326ce5,stroke:#fff,stroke-width:4px,color:#fff;
    classDef cluster fill:#fff,stroke:#bbb,stroke-width:2px,color:#326ce5;
    class n1,n2,n3,n4 k8s;
    class zoneA,zoneB cluster;
```