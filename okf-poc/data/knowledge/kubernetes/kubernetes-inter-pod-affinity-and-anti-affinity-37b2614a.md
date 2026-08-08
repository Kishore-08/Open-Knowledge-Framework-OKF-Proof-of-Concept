---
id: kubernetes-inter-pod-affinity-and-anti-affinity-37b2614a
type: concept
title: Inter-pod affinity and anti-affinity
description: Inter-pod affinity and anti-affinity allow you to constrain which nodes
  your
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Inter-pod affinity and anti-affinity

Inter-pod affinity and anti-affinity allow you to constrain which nodes your
Pods can be scheduled on based on the labels of Pods already running on that
node, instead of the node labels.

#### Types of Inter-pod Affinity and Anti-affinity

Inter-pod affinity and anti-affinity take the form "this
Pod should (or, in the case of anti-affinity, should not) run in an X if that X
is already running one or more Pods that meet rule Y", where X is a topology
domain like node, rack, cloud provider zone or region, or similar and Y is the
rule Kubernetes tries to satisfy.

You express these rules (Y) as [label selectors](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#label-selectors)
with an optional associated list of namespaces. Pods are namespaced objects in
Kubernetes, so Pod labels also implicitly have namespaces. Any label selectors
for Pod labels should specify the namespaces in which Kubernetes should look for those
labels.

You express the topology domain (X) using a `topologyKey`, which is the key for
the node label that the system uses to denote the domain. For examples, see
[Well-Known Labels, Annotations and Taints](https://kubernetes.io/docs/reference/labels-annotations-taints/).

#### Note:

Inter-pod affinity and anti-affinity require substantial amounts of
processing which can slow down scheduling in large clusters significantly. We do
not recommend using them in clusters larger than several hundred nodes.

#### Note:

Pod anti-affinity requires nodes to be consistently labeled, in other words,
every node in the cluster must have an appropriate label matching `topologyKey`.
If some or all nodes are missing the specified `topologyKey` label, it can lead
to unintended behavior.

Similar to [node affinity](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#node-affinity) are two types of Pod affinity and
anti-affinity as follows:

- `requiredDuringSchedulingIgnoredDuringExecution`
- `preferredDuringSchedulingIgnoredDuringExecution`

For example, you could use
`requiredDuringSchedulingIgnoredDuringExecution` affinity to tell the scheduler to
co-locate Pods of two services in the same cloud provider zone because they
communicate with each other a lot. Similarly, you could use
`preferredDuringSchedulingIgnoredDuringExecution` anti-affinity to spread Pods
from a service across multiple cloud provider zones.

To use inter-pod affinity, use the `affinity.podAffinity` field in the Pod spec.
For inter-pod anti-affinity, use the `affinity.podAntiAffinity` field in the Pod
spec.

#### Scheduling Behavior

When scheduling a new Pod, the Kubernetes scheduler evaluates the Pod's affinity/anti-affinity rules in the context of the current cluster state:

1. Hard Constraints (Node Filtering):

   - `podAffinity.requiredDuringSchedulingIgnoredDuringExecution` and `podAntiAffinity.requiredDuringSchedulingIgnoredDuringExecution`:
     - The scheduler ensures the new Pod is assigned to nodes that satisfy these required affinity and anti-affinity rules based on existing Pods.
2. Soft Constraints (Scoring):

   - `podAffinity.preferredDuringSchedulingIgnoredDuringExecution` and `podAntiAffinity.preferredDuringSchedulingIgnoredDuringExecution`:
     - The scheduler scores nodes based on how well they meet these preferred affinity and anti-affinity rules to optimize Pod placement.
3. Ignored Fields:

   - Existing Pods' `podAffinity.preferredDuringSchedulingIgnoredDuringExecution`:
     - These preferred affinity rules are not considered during the scheduling decision for new Pods.
   - Existing Pods' `podAntiAffinity.preferredDuringSchedulingIgnoredDuringExecution`:
     - Similarly, preferred anti-affinity rules of existing Pods are ignored during scheduling.

#### Scheduling a Group of Pods with Inter-pod Affinity to Themselves

If the current Pod being scheduled is the first in a series that have affinity to themselves,
it is allowed to be scheduled if i