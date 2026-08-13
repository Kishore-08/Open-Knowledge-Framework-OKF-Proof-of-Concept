---
id: kubernetes-example-one-topology-spread-constraint-4f7e995f
type: concept
title: 'Example: one topology spread constraint'
description: 'Suppose you have a 4-node cluster where 3 Pods labeled `foo: bar` are
  located in'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/scheduling-eviction/topology-spread-constraints/
updated_at: '2026-08-13'
created_at: '2026-08-13'
---

### Example: one topology spread constraint

Suppose you have a 4-node cluster where 3 Pods labeled `foo: bar` are located in
node1, node2 and node3 respectively:

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
    class zoneA,zoneB cluster;
```

If you want an incoming Pod to be evenly spread with existing Pods across zones, you
can use a manifest similar to:

[`pods/topology-spread-constraints/one-constraint.yaml`](https://raw.githubusercontent.com/kubernetes/website/main/content/en/examples/pods/topology-spread-constraints/one-constraint.yaml)![](https://kubernetes.io/images/copycode.svg "Copy pods/topology-spread-constraints/one-constraint.yaml to clipboard")

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
  containers:
  - name: pause
    image: registry.k8s.io/pause:3.1
```

From that manifest, `topologyKey: zone` implies the even distribution will only be applied
to nodes that are labeled `zone: <any value>` (nodes that don't have a `zone` label
are skipped). The field `whenUnsatisfiable: DoNotSchedule` tells the scheduler to let the
incoming Pod stay pending if the scheduler can't find a way to satisfy the constraint.

If the scheduler placed this incoming Pod into zone `A`, the distribution of Pods would
become `[3, 1]`. That means the actual skew is then 2 (calculated as `3 - 1`), which
violates `maxSkew: 1`. To satisfy the constraints and context for this example, the
incoming Pod can only be placed onto a node in zone `B`:

```
graph BT
    subgraph "zoneB"
        p3(Pod) --> n3(Node3)
        p4(mypod) --> n4(Node4)
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

OR

```
graph BT
    subgraph "zoneB"
        p3(Pod) --> n3(Node3)
        p4(mypod) --> n3
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

You can tweak the Pod spec to meet various kinds of requirements:

- Change `maxSkew` to a bigger value - such as `2` - so that the incoming Pod can
  be placed into zone `A` as well.
- Change `topologyKey` to `node` so as to distribute the Pods evenly across nodes
  instead of zones. In the above example, if `maxSkew` remains `1`, the incoming
  Pod can only be placed onto the node `node4`.
- Change `whenUnsatisfiable: DoNotSchedule` to `whenUnsatisfiable: ScheduleAnyway`
  to ensure the incoming Pod to be always schedulable (suppose other scheduling APIs
  are satisfied). However, it's preferred to be placed into the topology domain which
  has fewer matching Pods. (Be aware that this preference is jointly normalized
  with other internal scheduling priorities such as resource usage ratio).