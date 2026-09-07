---
id: kubernetes-preemptionpolicy-in-compositepodgroup-98ef819e
type: concept
title: PreemptionPolicy in CompositePodGroup
description: 'FEATURE STATE:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/workload-api/disruption-and-priority/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

### PreemptionPolicy in CompositePodGroup

FEATURE STATE:
`Kubernetes v1.37 [alpha]`(disabled by default)

The `CompositePodGroup` API has the `preemptionPolicy` field as well and its resolution is performed
in the exact same way as for the `PodGroup` API.

The value of `preemptionPolicy` of the root `CompositePodGroup` determines whether
[workload-aware preemption](https://kubernetes.io/docs/concepts/scheduling-eviction/workload-aware-preemption/) can be
invoked to fit its Pods during scheduling if needed:

- `PreemptLowerPriority` policy allows preempting victims with lower priority,
- `Never` policy disables workload-aware preemption for that root `CompositePodGroup`.

All Pods within a single group hierarchy must share the exact same preemption policy which must be
equal to the preemption policy of the root `CompositePodGroup`.

If the feature flag is disabled, the root `CompositePodGroup` will be allowed to perform preemption
unless one of the Pods that belongs to the group hierarchy has `preemptionPolicy` set to `Never`.

#### Note:

In v1.37, when the feature gate is enabled, the scheduler doesn't validate if the non-root groups
have preemption policy that is equal to the preemption policy of the root `CompositePodGroup`.