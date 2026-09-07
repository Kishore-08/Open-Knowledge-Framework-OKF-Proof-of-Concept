---
id: kubernetes-set-references-in-api-objects-0cf968e6
type: concept
title: Set references in API objects
description: Some Kubernetes objects, such as [`services`](https://kubernetes.io/docs/concepts/services-networking/service/)
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

### Set references in API objects

Some Kubernetes objects, such as [`services`](https://kubernetes.io/docs/concepts/services-networking/service/)
and [`replicationcontrollers`](https://kubernetes.io/docs/concepts/workloads/controllers/replicationcontroller/),
also use label selectors to specify sets of other resources, such as
[pods](https://kubernetes.io/docs/concepts/workloads/pods/).

#### Service and ReplicationController

The set of pods that a `service` targets is defined with a label selector.
Similarly, the population of pods that a `replicationcontroller` should
manage is also defined with a label selector.

Label selectors for both objects are defined in `json` or `yaml` files using maps,
and only *equality-based* requirement selectors are supported:

```
"selector": {
    "component" : "redis",
}
```

or

```
selector:
  component: redis
```

This selector (respectively in `json` or `yaml` format) is equivalent to
`component=redis` or `component in (redis)`.

#### Resources that support set-based requirements

Newer resources, such as [`Job`](https://kubernetes.io/docs/concepts/workloads/controllers/job/),
[`Deployment`](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/),
[`ReplicaSet`](https://kubernetes.io/docs/concepts/workloads/controllers/replicaset/), and
[`DaemonSet`](https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/),
support *set-based* requirements as well.

```
selector:
  matchLabels:
    component: redis
  matchExpressions:
    - { key: tier, operator: In, values: [cache] }
    - { key: environment, operator: NotIn, values: [dev] }
```

`matchLabels` is a map of `{key,value}` pairs. A single `{key,value}` in the
`matchLabels` map is equivalent to an element of `matchExpressions`, whose `key`
field is "key", the `operator` is "In", and the `values` array contains only "value".
`matchExpressions` is a list of pod selector requirements. Valid operators include
In, NotIn, Exists, and DoesNotExist. The values set must be non-empty in the case of
In and NotIn. All of the requirements, from both `matchLabels` and `matchExpressions`
are ANDed together -- they must all be satisfied in order to match.

#### Selecting sets of nodes

One use case for selecting over labels is to constrain the set of nodes onto which
a pod can schedule. See the documentation on
[node selection](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/) for more information.