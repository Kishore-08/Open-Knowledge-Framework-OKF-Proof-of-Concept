---
id: kubernetes-cluster-level-default-constraints-4f7e995f
type: concept
title: Cluster-level default constraints
description: It is possible to set default topology spread constraints for a cluster.
  Default
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/scheduling-eviction/topology-spread-constraints/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

## Cluster-level default constraints

It is possible to set default topology spread constraints for a cluster. Default
topology spread constraints are applied to a Pod if, and only if:

- It doesn't define any constraints in its `.spec.topologySpreadConstraints`.
- It belongs to a Service, ReplicaSet, StatefulSet or ReplicationController.

Default constraints can be set as part of the `PodTopologySpread` plugin
arguments in a [scheduling profile](https://kubernetes.io/docs/reference/scheduling/config/#profiles).
The constraints are specified with the same [API above](https://kubernetes.io/docs/concepts/scheduling-eviction/topology-spread-constraints/#topologyspreadconstraints-field), except that
`labelSelector` must be empty. The selectors are calculated from the Services,
ReplicaSets, StatefulSets or ReplicationControllers that the Pod belongs to.

An example configuration might look like follows:

```
apiVersion: kubescheduler.config.k8s.io/v1
kind: KubeSchedulerConfiguration

profiles:
  - schedulerName: default-scheduler
    pluginConfig:
      - name: PodTopologySpread
        args:
          defaultConstraints:
            - maxSkew: 1
              topologyKey: topology.kubernetes.io/zone
              whenUnsatisfiable: ScheduleAnyway
          defaultingType: List
```