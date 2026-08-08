---
id: kubernetes-node-selection-in-kube-scheduler-c57f4146
type: concept
title: Node selection in kube-scheduler
description: 'kube-scheduler selects a node for the pod in a 2-step operation:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/scheduling-eviction/kube-scheduler/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Node selection in kube-scheduler

kube-scheduler selects a node for the pod in a 2-step operation:

1. Filtering
2. Scoring

The *filtering* step finds the set of Nodes where it's feasible to
schedule the Pod. For example, the PodFitsResources filter checks whether a
candidate Node has enough available resources to meet a Pod's specific
resource requests. After this step, the node list contains any suitable
Nodes; often, there will be more than one. If the list is empty, that
Pod isn't (yet) schedulable.

In the *scoring* step, the scheduler ranks the remaining nodes to choose
the most suitable Pod placement. The scheduler assigns a score to each Node
that survived filtering, basing this score on the active scoring rules.

Finally, kube-scheduler assigns the Pod to the Node with the highest ranking.
If there is more than one node with equal scores, kube-scheduler selects
one of these at random.

There are two supported ways to configure the filtering and scoring behavior
of the scheduler:

1. [Scheduling Policies](https://kubernetes.io/docs/reference/scheduling/policies/) allow you to configure *Predicates* for filtering and *Priorities* for scoring.
2. [Scheduling Profiles](https://kubernetes.io/docs/reference/scheduling/config/#profiles) allow you to configure Plugins that implement different scheduling stages, including: `QueueSort`, `Filter`, `Score`, `Bind`, `Reserve`, `Permit`, and others. You can also configure the kube-scheduler to run different profiles.