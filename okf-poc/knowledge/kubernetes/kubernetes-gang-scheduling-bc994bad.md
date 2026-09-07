---
id: kubernetes-gang-scheduling-bc994bad
type: concept
title: Gang scheduling
description: The following Job requests gang scheduling for its 8 Pods, co-located
  within a
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/controllers/job/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

### Gang scheduling

The following Job requests gang scheduling for its 8 Pods, co-located within a
single zone, and disrupted together:

```
apiVersion: batch/v1
kind: Job
metadata:
  name: distributed-training
  namespace: training
spec:
  parallelism: 8
  completions: 8
  completionMode: Indexed
  scheduling:
    schedulingPolicy:
      gang: {}                # minCount omitted -> defaults to parallelism (8)
    schedulingConstraints:
      key:
      - level: topology.kubernetes.io/zone
    disruptionMode:
      all: {}                 # the entire group is disrupted together
  template:
    spec:
      restartPolicy: Never
      containers:
      - name: trainer
        image: training-image:latest
        resources:
          limits:
            nvidia.com/gpu: 1
```

When the Job controller processes this Job, it:

1. Creates a [Workload](https://kubernetes.io/docs/concepts/workloads/workload-api/) object in the same
   namespace, containing a `podGroupTemplate` compiled from `.spec.scheduling`
   (here, a [gang policy](https://kubernetes.io/docs/concepts/workloads/workload-api/policies/) with
   `minCount: 8`).
2. Creates a PodGroup object from that template. The PodGroup is the runtime
   scheduling unit and carries an inline copy of the policy.
3. Creates Pods with `.spec.schedulingGroup.podGroupName` set to the PodGroup's
   name, linking each Pod to its scheduling group.

The controller discovers these objects through spec references
(`Workload.spec.controllerRef` and `PodGroup.spec.workloadRef`), not by
name. Objects the controller creates carry an `ownerReferences` entry pointing to
the Job, so they are garbage collected when the Job is deleted.