---
id: kubernetes-compositepodgroup-98ef819e
type: concept
title: CompositePodGroup
description: 'FEATURE STATE:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/workload-api/disruption-and-priority/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

## CompositePodGroup

FEATURE STATE:
`Kubernetes v1.37 [alpha]`(disabled by default)

A `CompositePodGroup` can also declare a `disruptionMode` in its specification, which controls
how the scheduler disrupts child groups within the composite group during preemption events.

The API supports two disruption modes for `CompositePodGroups`:

- **`Single`**: Allows individual child groups within the `CompositePodGroup` to be disrupted
  independently during preemption.
- **`All`**: Enforces all-or-nothing disruption semantics across the `CompositePodGroup` hierarchy.
  If any Pod contained in the hierarchy below this `CompositePodGroup` has to be preempted, all of
  the Pods from the entire hierarchy must be preempted.

If not specified, the mode defaults to `Single`.

#### Note:

In v1.37, a group can set its disruption mode to `All` and have child groups that have a mode set to
`Single`. In such case, the top-level `All` mode overrides the descendant `Single` modes.

This configuration is discouraged due to unclear semantics.