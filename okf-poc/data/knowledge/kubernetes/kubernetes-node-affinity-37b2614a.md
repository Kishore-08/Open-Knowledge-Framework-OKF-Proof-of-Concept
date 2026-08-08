---
id: kubernetes-node-affinity-37b2614a
type: concept
title: Node affinity
description: Node affinity is conceptually similar to `nodeSelector`, allowing you
  to constrain which nodes your
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Node affinity

Node affinity is conceptually similar to `nodeSelector`, allowing you to constrain which nodes your
Pod can be scheduled on based on node labels. There are two types of node
affinity:

- `requiredDuringSchedulingIgnoredDuringExecution`: The scheduler can't
  schedule the Pod unless the rule is met. This functions like `nodeSelector`,
  but with a more expressive syntax.
- `preferredDuringSchedulingIgnoredDuringExecution`: The scheduler tries to
  find a node that meets the rule. If a matching node is not available, the
  scheduler still schedules the Pod.

#### Note:

In the preceding types, `IgnoredDuringExecution` means that if the node labels
change after Kubernetes schedules the Pod, the Pod continues to run.

You can specify node affinities using the `.spec.affinity.nodeAffinity` field in
your Pod spec.

For example, consider the following Pod spec:

[`pods/pod-with-node-affinity.yaml`](https://raw.githubusercontent.com/kubernetes/website/main/content/en/examples/pods/pod-with-node-affinity.yaml)![](https://kubernetes.io/images/copycode.svg "Copy pods/pod-with-node-affinity.yaml to clipboard")

```
apiVersion: v1
kind: Pod
metadata:
  name: with-node-affinity
spec:
  affinity:
    nodeAffinity:
      requiredDuringSchedulingIgnoredDuringExecution:
        nodeSelectorTerms:
        - matchExpressions:
          - key: topology.kubernetes.io/zone
            operator: In
            values:
            - antarctica-east1
            - antarctica-west1
      preferredDuringSchedulingIgnoredDuringExecution:
      - weight: 1
        preference:
          matchExpressions:
          - key: another-node-label-key
            operator: In
            values:
            - another-node-label-value
  containers:
  - name: with-node-affinity
    image: registry.k8s.io/pause:3.8
```

In this example, the following rules apply:

- The node *must* have a label with the key `topology.kubernetes.io/zone` and
  the value of that label *must* be either `antarctica-east1` or `antarctica-west1`.
- The node *preferably* has a label with the key `another-node-label-key` and
  the value `another-node-label-value`.

You can use the `operator` field to specify a logical operator for Kubernetes to use when
interpreting the rules. You can use `In`, `NotIn`, `Exists`, `DoesNotExist`,
`Gt` and `Lt`.

Read [Operators](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#operators)
to learn more about how these work.

`NotIn` and `DoesNotExist` allow you to define node anti-affinity behavior.
Alternatively, you can use [node taints](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/)
to repel Pods from specific nodes.

#### Note:

If you specify both `nodeSelector` and `nodeAffinity`, *both* must be satisfied
for the Pod to be scheduled onto a node.

If you specify multiple terms in `nodeSelectorTerms` associated with `nodeAffinity`
types, then the Pod can be scheduled onto a node if one of the specified terms
can be satisfied (terms are ORed).

If you specify multiple expressions in a single `matchExpressions` field associated with a
term in `nodeSelectorTerms`, then the Pod can be scheduled onto a node only
if all the expressions are satisfied (expressions are ANDed).

See [Assign Pods to Nodes using Node Affinity](https://kubernetes.io/docs/tasks/configure-pod-container/assign-pods-nodes-using-node-affinity/)
for more information.

#### Node affinity weight

You can specify a `weight` between 1 and 100 for each instance of the
`preferredDuringSchedulingIgnoredDuringExecution` affinity type. When the
scheduler finds nodes that meet all the other scheduling requirements of the Pod, the
scheduler iterates through every preferred rule that the node satisfies and adds the
value of the `weight` for that expression to a sum.

The final sum is added to the score of other priority functions for the node.
Nodes with the highest total score are prioritized when the scheduler makes a
scheduling