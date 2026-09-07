---
id: kubernetes-example-b35f526f
type: concept
title: Example
description: The following example configures a `Workload` where the parent `CompositePodGroupTemplate`
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/workload-api/topology-aware-scheduling/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

### Example

The following example configures a `Workload` where the parent `CompositePodGroupTemplate`
constrains the entire workload to a single availability zone (`topology.example.com/zone`), while
two child `PodGroupTemplate` entries (`workers` and `driver`) constrain their respective
Pods to server racks (`topology.example.com/rack`) within that zone:

```
apiVersion: scheduling.k8s.io/v1alpha3
kind: Workload
metadata:
  name: example-workload
spec:
  compositePodGroupTemplates:
  - name: root
    schedulingPolicy:
      gang:
        minGroupCount: 2
    schedulingConstraints:
      topology:
      - key: topology.example.com/zone
    podGroupTemplates:
    - name: workers
      schedulingPolicy:
        gang:
          minCount: 8
      schedulingConstraints:
        topology:
        - key: topology.example.com/rack
    - name: driver
      schedulingPolicy:
        gang:
          minCount: 1
      schedulingConstraints:
        topology:
        - key: topology.example.com/rack
```

After creating the `Workload` object, the corresponding group objects are created as follows:

- Root `CompositePodGroup` referencing the `root` template.
- Two child `PodGroup` objects (`workers` and `driver`), each referencing the root
  `CompositePodGroup` as their parent group.

```
apiVersion: scheduling.k8s.io/v1alpha3
kind: CompositePodGroup
metadata:
  name: workload-root
spec:
  workloadRef:
    workloadName: example-workload
    templateName: root
  schedulingPolicy:
    gang:
      minGroupCount: 2
  schedulingConstraints:
    topology:
    - key: topology.example.com/zone
---
apiVersion: scheduling.k8s.io/v1beta1
kind: PodGroup
metadata:
  name: workload-workers
spec:
  parentCompositePodGroupName: workload-root
  workloadRef:
    workloadName: example-workload
    templateName: workers
  schedulingPolicy:
    gang:
      minCount: 8
  schedulingConstraints:
    topology:
    - key: topology.example.com/rack
---
apiVersion: scheduling.k8s.io/v1beta1
kind: PodGroup
metadata:
  name: workload-driver
spec:
  parentCompositePodGroupName: workload-root
  workloadRef:
    workloadName: example-workload
    templateName: driver
  schedulingPolicy:
    gang:
      minCount: 1
  schedulingConstraints:
    topology:
    - key: topology.example.com/rack
```

During scheduling, the scheduler first selects an availability zone for `workload-root`. It then
subdivides the nodes in that zone by rack to find feasible rack placements for `workload-workers`
and `workload-driver` within the selected zone.

For example, consider a cluster with five nodes labeled as follows:

| Node | `topology.example.com/zone` | `topology.example.com/rack` |
| --- | --- | --- |
| `node-a` | `zone-1` | `rack-1` |
| `node-b` | `zone-1` | `rack-1` |
| `node-c` | `zone-1` | `rack-2` |
| `node-d` | `zone-2` | `rack-1` |
| `node-e` | `zone-2` | `rack-3` |

When processing `workload-root`, the scheduler evaluates candidate placements across all cluster
nodes based on the `topology.example.com/zone` topology key:

| Evaluated candidate placement | Nodes in candidate placement |
| --- | --- |
| `zone-1` | `node-a`, `node-b`, `node-c` |
| `zone-2` | `node-d`, `node-e` |

When evaluating candidate placements for `workload-workers`, the scheduler subdivides only the nodes
within the placement assumed by `workload-root` based on the `topology.example.com/rack` topology key:

| Parent placement | Evaluated candidate placement | Nodes in candidate placement |
| --- | --- | --- |
| `zone-1` | `rack-1` | `node-a`, `node-b` |
| `zone-1` | `rack-2` | `node-c` |
| `zone-2` | `rack-1` | `node-d` |
| `zone-2` | `rack-3` | `node-e` |

Candidate placements generated for the sibling `workload-driver` PodGroup are identical to those
generated for `workload-workers`, since both groups specify the same topology key
(`topology.example.com/rack`).