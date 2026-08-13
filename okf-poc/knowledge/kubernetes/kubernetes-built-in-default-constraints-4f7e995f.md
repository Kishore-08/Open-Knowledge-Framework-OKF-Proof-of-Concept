---
id: kubernetes-built-in-default-constraints-4f7e995f
type: concept
title: Built-in default constraints
description: 'FEATURE STATE:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/scheduling-eviction/topology-spread-constraints/
updated_at: '2026-08-13'
created_at: '2026-08-13'
---

### Built-in default constraints

FEATURE STATE:
`Kubernetes v1.24 [stable]`

If you don't configure any cluster-level default constraints for pod topology spreading,
then kube-scheduler acts as if you specified the following default topology constraints:

```
defaultConstraints:
  - maxSkew: 3
    topologyKey: "kubernetes.io/hostname"
    whenUnsatisfiable: ScheduleAnyway
  - maxSkew: 5
    topologyKey: "topology.kubernetes.io/zone"
    whenUnsatisfiable: ScheduleAnyway
```

Also, the legacy `SelectorSpread` plugin, which provides an equivalent behavior,
is disabled by default.

#### Note:

The `PodTopologySpread` plugin does not score the nodes that don't have
the topology keys specified in the spreading constraints. This might result
in a different default behavior compared to the legacy `SelectorSpread` plugin when
using the default topology constraints.

If your nodes are not expected to have **both** `kubernetes.io/hostname` and
`topology.kubernetes.io/zone` labels set, define your own constraints
instead of using the Kubernetes defaults.

If you don't want to use the default Pod spreading constraints for your cluster,
you can disable those defaults by setting `defaultingType` to `List` and leaving
empty `defaultConstraints` in the `PodTopologySpread` plugin configuration:

```
apiVersion: kubescheduler.config.k8s.io/v1
kind: KubeSchedulerConfiguration

profiles:
  - schedulerName: default-scheduler
    pluginConfig:
      - name: PodTopologySpread
        args:
          defaultConstraints: []
          defaultingType: List
```