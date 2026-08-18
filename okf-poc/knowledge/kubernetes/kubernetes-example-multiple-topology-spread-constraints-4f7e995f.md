---
id: kubernetes-example-multiple-topology-spread-constraints-4f7e995f
type: concept
title: 'Example: multiple topology spread constraints'
description: This builds upon the previous example. Suppose you have a 4-node cluster
  where 3
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/scheduling-eviction/topology-spread-constraints/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

### Example: multiple topology spread constraints

This builds upon the previous example. Suppose you have a 4-node cluster where 3
existing Pods labeled `foo: bar` are located on node1, node2 and node3 respectively:

```
graph BT
    subgraph "zoneB"
        p3(Pod) --> n3(Node3)
        n4(Node4)
    end
    subgraph "zoneA"
        p1(Pod) --> n1(Node1)
        p2(Pod) --> n2(Node2)
    end

    classDef plain fill:#ddd,stroke:#fff,stroke-width:4px,color:#000;
    classDef k8s fill:#326ce5,stroke:#fff,stroke-width:4px,color:#fff;
    classDef cluster fill:#fff,stroke:#bbb,stroke-width:2px,color:#326ce5;
    class n1,n2,n3,n4,p1,p2,p3 k8s;
    class p4 plain;
    class zoneA,zoneB cluster;
```

You can combine two topology spread constraints to control the spread of Pods both
by node and by zone:

[`pods/topology-spread-constraints/two-constraints.yaml`](https://raw.githubusercontent.com/kubernetes/website/main/content/en/examples/pods/topology-spread-constraints/two-constraints.yaml)![](https://kubernetes.io/images/copycode.svg "Copy pods/topology-spread-constraints/two-constraints.yaml to clipboard")

```
kind: Pod
apiVersion: v1
metadata:
  name: mypod
  labels:
    foo: bar
spec:
  topologySpreadConstraints:
  - maxSkew: 1
    topologyKey: zone
    whenUnsatisfiable: DoNotSchedule
    labelSelector:
      matchLabels:
        foo: bar
  - maxSkew: 1
    topologyKey: node
    whenUnsatisfiable: DoNotSchedule
    labelSelector:
      matchLabels:
        foo: bar
  containers:
  - name: pause
    image: registry.k8s.io/pause:3.1
```

In this case, to match the first constraint, the incoming Pod can only be placed onto
nodes in zone `B`; while in terms of the second constraint, the incoming Pod can only be
scheduled to the node `node4`. The scheduler only considers options that satisfy all
defined constraints, so the only valid placement is onto node `node4`.