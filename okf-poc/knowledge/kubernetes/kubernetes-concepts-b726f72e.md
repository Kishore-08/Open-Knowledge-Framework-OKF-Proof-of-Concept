---
id: kubernetes-concepts-b726f72e
type: concept
title: Concepts
description: You add a taint to a node using [kubectl taint](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#taint).
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

## Concepts

You add a taint to a node using [kubectl taint](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#taint).
For example,

```
kubectl taint nodes node1 key1=value1:NoSchedule
```

places a taint on node `node1`. The taint has key `key1`, value `value1`, and taint effect `NoSchedule`.
This means that no pod will be able to schedule onto `node1` unless it has a matching toleration.

To remove the taint added by the command above, you can run:

```
kubectl taint nodes node1 key1=value1:NoSchedule-
```

You specify a toleration for a pod in the PodSpec. Both of the following tolerations "match" the
taint created by the `kubectl taint` line above, and thus a pod with either toleration would be able
to schedule onto `node1`:

```
tolerations:
- key: "key1"
  operator: "Equal"
  value: "value1"
  effect: "NoSchedule"
```

```
tolerations:
- key: "key1"
  operator: "Exists"
  effect: "NoSchedule"
```

The default Kubernetes scheduler takes taints and tolerations into account when
selecting a node to run a particular Pod. However, if you manually specify the
`.spec.nodeName` for a Pod, that action bypasses the scheduler; the Pod is then
bound onto the node where you assigned it, even if there are `NoSchedule`
taints on that node that you selected.
If this happens and the node also has a `NoExecute` taint set, the kubelet will
eject the Pod unless there is an appropriate tolerance set.

Here's an example of a pod that has some tolerations defined:

[`pods/pod-with-toleration.yaml`](https://raw.githubusercontent.com/kubernetes/website/main/content/en/examples/pods/pod-with-toleration.yaml)![](https://kubernetes.io/images/copycode.svg "Copy pods/pod-with-toleration.yaml to clipboard")

```
apiVersion: v1
kind: Pod
metadata:
  name: nginx
  labels:
    env: test
spec:
  containers:
  - name: nginx
    image: nginx
    imagePullPolicy: IfNotPresent
  tolerations:
  - key: "example-key"
    operator: "Exists"
    effect: "NoSchedule"
```

The default value for `operator` is `Equal`.

A toleration "matches" a taint if the keys are the same and the effects are the same, and:

- the `operator` is `Exists` (in which case no `value` should be specified), or
- the `operator` is `Equal` and the values should be equal.

#### Note:

There are two special cases:

If the `key` is empty, then the `operator` must be `Exists`, which matches all keys and values.
Note that the `effect` still needs to be matched at the same time.

An empty `effect` matches all effects with key `key1`.

The above example used the `effect` of `NoSchedule`. Alternatively, you can use the `effect` of `PreferNoSchedule`.

The allowed values for the `effect` field are:

`NoExecute`
:   This affects pods that are already running on the node as follows:

    - Pods that do not tolerate the taint are evicted immediately
    - Pods that tolerate the taint without specifying `tolerationSeconds` in
      their toleration specification remain bound forever
    - Pods that tolerate the taint with a specified `tolerationSeconds` remain
      bound for the specified amount of time. After that time elapses, the node
      lifecycle controller evicts the Pods from the node.

`NoSchedule`
:   No new Pods will be scheduled on the tainted node unless they have a matching
    toleration. Pods currently running on the node are **not** evicted.

`PreferNoSchedule`
:   `PreferNoSchedule` is a "preference" or "soft" version of `NoSchedule`.
    The control plane will *try* to avoid placing a Pod that does not tolerate
    the taint on the node, but it is not guaranteed.

You can put multiple taints on the same node and multiple tolerations on the same pod.
The way Kubernetes processes multiple taints and tolerations is like a filter: start
with all of a node's taints, then ignore the ones for which the pod has a matching toleration; the
remaining un-ignored taints have the indicated effects on the pod. In particular,

- if there is at least one un-ignored taint with e