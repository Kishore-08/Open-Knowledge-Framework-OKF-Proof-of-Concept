---
id: kubernetes-example-conflicting-topology-spread-constraints-4f7e995f
type: concept
title: 'Example: conflicting topology spread constraints'
description: 'Multiple constraints can lead to conflicts. Suppose you have a 3-node
  cluster across 2 zones:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/scheduling-eviction/topology-spread-constraints/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

### Example: conflicting topology spread constraints

Multiple constraints can lead to conflicts. Suppose you have a 3-node cluster across 2 zones:

```
graph BT
    subgraph "zoneB"
        p4(Pod) --> n3(Node3)
        p5(Pod) --> n3
    end
    subgraph "zoneA"
        p1(Pod) --> n1(Node1)
        p2(Pod) --> n1
        p3(Pod) --> n2(Node2)
    end

    classDef plain fill:#ddd,stroke:#fff,stroke-width:4px,color:#000;
    classDef k8s fill:#326ce5,stroke:#fff,stroke-width:4px,color:#fff;
    classDef cluster fill:#fff,stroke:#bbb,stroke-width:2px,color:#326ce5;
    class n1,n2,n3,n4,p1,p2,p3,p4,p5 k8s;
    class zoneA,zoneB cluster;
```

If you were to apply
[`two-constraints.yaml`](https://raw.githubusercontent.com/kubernetes/website/main/content/en/examples/pods/topology-spread-constraints/two-constraints.yaml)
(the manifest from the previous example)
to **this** cluster, you would see that the Pod `mypod` stays in the `Pending` state.
This happens because: to satisfy the first constraint, the Pod `mypod` can only
be placed into zone `B`; while in terms of the second constraint, the Pod `mypod`
can only schedule to node `node2`. The intersection of the two constraints returns
an empty set, and the scheduler cannot place the Pod.

To overcome this situation, you can either increase the value of `maxSkew` or modify
one of the constraints to use `whenUnsatisfiable: ScheduleAnyway`. Depending on
circumstances, you might also decide to delete an existing Pod manually - for example,
if you are troubleshooting why a bug-fix rollout is not making progress.

#### Interaction with node affinity and node selectors

The scheduler will skip the non-matching nodes from the skew calculations if the
incoming Pod has `spec.nodeSelector` or `spec.affinity.nodeAffinity` defined.