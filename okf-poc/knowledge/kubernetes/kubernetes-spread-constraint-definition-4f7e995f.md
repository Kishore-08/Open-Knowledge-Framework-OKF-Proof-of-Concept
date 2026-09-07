---
id: kubernetes-spread-constraint-definition-4f7e995f
type: concept
title: Spread constraint definition
description: You can define one or multiple `topologySpreadConstraints` entries to
  instruct the
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/scheduling-eviction/topology-spread-constraints/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

### Spread constraint definition

You can define one or multiple `topologySpreadConstraints` entries to instruct the
kube-scheduler how to place each incoming Pod in relation to the existing Pods across
your cluster. Those fields are:

- **maxSkew** describes the degree to which Pods may be unevenly distributed. You must
  specify this field and the number must be greater than zero. Its semantics differ
  according to the value of `whenUnsatisfiable`:

  - if you select `whenUnsatisfiable: DoNotSchedule`, then `maxSkew` defines the
    maximum permitted difference between the number of matching pods in the target
    topology and the *global minimum*
    (the minimum number of matching pods in an eligible domain or zero if the number of eligible domains is less than MinDomains).
    For example, if you have 3 zones with 2, 2 and 1 matching pods respectively,
    `MaxSkew` is set to 1 then the global minimum is 1.
  - if you select `whenUnsatisfiable: ScheduleAnyway`, the scheduler gives higher
    precedence to topologies that would help reduce the skew.
- **minDomains** indicates a minimum number of eligible domains. This field is optional.
  A domain is a particular instance of a topology. An eligible domain is a domain whose
  nodes match the node selector.

  #### Note:

  Before Kubernetes v1.30, the `minDomains` field was only available if the
  `MinDomainsInPodTopologySpread` [feature gate](https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates-removed/)
  was enabled (default since v1.28). In older Kubernetes clusters it might be explicitly
  disabled or the field might not be available.

  - The value of `minDomains` must be greater than 0, when specified.
    You can only specify `minDomains` in conjunction with `whenUnsatisfiable: DoNotSchedule`.
  - When the number of eligible domains with match topology keys is less than `minDomains`,
    Pod topology spread treats global minimum as 0, and then the calculation of `skew` is performed.
    The global minimum is the minimum number of matching Pods in an eligible domain,
    or zero if the number of eligible domains is less than `minDomains`.
  - When the number of eligible domains with matching topology keys equals or is greater than
    `minDomains`, this value has no effect on scheduling.
  - If you do not specify `minDomains`, the constraint behaves as if `minDomains` is 1.
- **topologyKey** is the key of [node labels](https://kubernetes.io/docs/concepts/scheduling-eviction/topology-spread-constraints/#node-labels). Nodes that have a label with this key
  and identical values are considered to be in the same topology.
  We call each instance of a topology (in other words, a <key, value> pair) a domain. The scheduler
  will try to put a balanced number of pods into each domain.
  Also, we define an eligible domain as a domain whose nodes meet the requirements of
  nodeAffinityPolicy and nodeTaintsPolicy.
- **whenUnsatisfiable** indicates how to deal with a Pod if it doesn't satisfy the spread constraint:

  - `DoNotSchedule` (default) tells the scheduler not to schedule it.
  - `ScheduleAnyway` tells the scheduler to still schedule it while prioritizing nodes that minimize the skew.
- **labelSelector** is used to find matching Pods. Pods
  that match this label selector are counted to determine the
  number of Pods in their corresponding topology domain.
  See [Label Selectors](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#label-selectors)
  for more details.
- **matchLabelKeys** is a list of pod label keys to select the group of pods over which
  the spreading skew will be calculated. At a pod creation,
  the kube-apiserver uses those keys to lookup values from the incoming pod labels,
  and those key-value labels will be merged with any existing `labelSelector`.
  The same key is forbidden to exist in both `matchLabelKeys` and `labelSelector`.
  `matchLabelKeys` cannot be set when `labelSelector` isn't set.
  K