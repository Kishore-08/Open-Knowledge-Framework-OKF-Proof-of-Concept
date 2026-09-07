---
id: kubernetes-example-topology-spread-constraints-with-node-affinity-4f7e995f
type: concept
title: 'Example: topology spread constraints with node affinity'
description: 'Suppose you have a 5-node cluster ranging across zones A to C:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/scheduling-eviction/topology-spread-constraints/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

### Example: topology spread constraints with node affinity

Suppose you have a 5-node cluster ranging across zones A to C:

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

```
graph BT
    subgraph "zoneC"
        n5(Node5)
    end

classDef plain fill:#ddd,stroke:#fff,stroke-width:4px,color:#000;
classDef k8s fill:#326ce5,stroke:#fff,stroke-width:4px,color:#fff;
classDef cluster fill:#fff,stroke:#bbb,stroke-width:2px,color:#326ce5;
class n5 k8s;
class zoneC cluster;
```

and you know that zone `C` must be excluded. In this case, you can compose a manifest
as below, so that Pod `mypod` will be placed into zone `B` instead of zone `C`.
Similarly, Kubernetes also respects `spec.nodeSelector`.

[`pods/topology-spread-constraints/one-constraint-with-nodeaffinity.yaml`](https://raw.githubusercontent.com/kubernetes/website/main/content/en/examples/pods/topology-spread-constraints/one-constraint-with-nodeaffinity.yaml)![](https://kubernetes.io/images/copycode.svg "Copy pods/topology-spread-constraints/one-constraint-with-nodeaffinity.yaml to clipboard")

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
  affinity:
    nodeAffinity:
      requiredDuringSchedulingIgnoredDuringExecution:
        nodeSelectorTerms:
        - matchExpressions:
          - key: zone
            operator: NotIn
            values:
            - zoneC
  containers:
  - name: pause
    image: registry.k8s.io/pause:3.1
```