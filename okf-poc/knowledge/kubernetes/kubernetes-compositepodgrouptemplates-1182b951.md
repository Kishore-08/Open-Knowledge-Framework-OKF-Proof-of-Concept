---
id: kubernetes-compositepodgrouptemplates-1182b951
type: concept
title: CompositePodGroupTemplates
description: 'FEATURE STATE:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/workload-api/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

### CompositePodGroupTemplates

FEATURE STATE:
`Kubernetes v1.37 [alpha]`(disabled by default)

When the [`CompositePodGroup`](https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/#CompositePodGroup)
feature gate and the `scheduling.k8s.io/v1alpha3` [API group](https://kubernetes.io/docs/concepts/overview/kubernetes-api/#api-groups-and-versioning "A set of related paths in the Kubernetes API.")
are enabled, you can use `CompositePodGroupTemplates` to define multi-level, hierarchical scheduling
requirements in a `Workload`. These requirements can include enforcing nested topology constraints
across different layers of cluster infrastructure (multi-level topology-aware scheduling),
all-or-nothing scheduling across child groups (multi-level gang scheduling), or group-level
disruption policies.

`CompositePodGroupTemplates` can be defined using the `spec.compositePodGroupTemplates` field in the
`Workload` API. At runtime, workload controllers create [CompositePodGroup](https://kubernetes.io/docs/concepts/workloads/compositepodgroup-api/)
and [PodGroup](https://kubernetes.io/docs/concepts/workloads/podgroup-api/) objects from these templates to maintain the runtime
scheduling state of the hierarchy. While `PodGroup` objects manage groups of Pods at the leaves,
`CompositePodGroup` objects represent non-leaf groups that enforce scheduling policies across child groups.

#### Note:

In a `Workload` specification, `spec.compositePodGroupTemplates` and `spec.podGroupTemplates`
fields form a union: a `Workload` must define either `spec.podGroupTemplates` (for flat
workloads) or `spec.compositePodGroupTemplates` (for hierarchical workloads), but cannot
specify both.

#### Structure and constraints

The `spec.compositePodGroupTemplates` field defines non-leaf templates in a group-template
hierarchy tree. Each entry represents a template for a `CompositePodGroup` and can contain:

- **Child templates**: Nested `CompositePodGroupTemplates` (for intermediate non-leaf
  groups) or `PodGroupTemplates` (for leaf groups containing Pods).
- **Scheduling policy**: Specifies how child groups within this composite group are
  scheduled:
  - `basic`: Child groups are admitted and scheduled independently.
  - `gang`: Enforces multi-level all-or-nothing scheduling across child groups.
    Requires `minGroupCount`, which specifies the minimum number of child groups
    that must be schedulable simultaneously for the composite group to be feasible.
- **Scheduling constraints**: Optional
  [topology constraints](https://kubernetes.io/docs/concepts/workloads/workload-api/topology-aware-scheduling/)
  for multi-level topology-aware scheduling.
- **Priority, preemption policy and disruption mode**: Optional `priorityClassName`,
  `disruptionMode` (`Single` or `All`) and `preemptionPolicy` for
  [workload-aware preemption](https://kubernetes.io/docs/concepts/workloads/workload-api/disruption-and-priority/).

To ensure cluster stability and control-plane efficiency, the group-template hierarchy
enforces the following limits:

- **Maximum nesting depth**: The group-template hierarchy supports a maximum depth of
  4 levels.
- **List limit**: Every `compositePodGroupTemplates` and `podGroupTemplates` list is strictly
  capped at a maximum of 8 items.

#### Note:

Right now, you cannot add new or remove existing `CompositePodGroupTemplates`. You can only change
the `minCount` value in the gang scheduling policy defined in the leaf `PodGroupTemplates`.

#### Example

The following example defines a hierarchical `Workload` with a `CompositePodGroup` template
that enforces gang scheduling across two child `PodGroup` templates (`minGroupCount: 2`),
each specifying its own gang scheduling policy:

```
apiVersion: scheduling.k8s.io/v1alpha3
kind: Workload
metadata:
  name: gang-of-gangs-workload
  namespace: default
spec:
  compositePodGroupTemplates:
  - name: root
    schedulingPolicy:
      gang:
        # Requires both child PodGroups to be