---
id: kubernetes-delayed-creation-of-replacement-pods-bc994bad
type: concept
title: Delayed creation of replacement pods
description: 'FEATURE STATE:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/controllers/job/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

### Delayed creation of replacement pods

FEATURE STATE:
`Kubernetes v1.34 [stable]`(enabled by default)

By default, the Job controller recreates Pods as soon they either fail or are terminating (have a deletion timestamp).
This means that, at a given time, when some of the Pods are terminating, the number of running Pods for a Job
can be greater than `parallelism` or greater than one Pod per index (if you are using an Indexed Job).

You may choose to create replacement Pods only when the terminating Pod is fully terminal (has `status.phase: Failed`).
To do this, set the `.spec.podReplacementPolicy: Failed`.
The default replacement policy depends on whether the Job has a `podFailurePolicy` set.
With no Pod failure policy defined for a Job, omitting the `podReplacementPolicy` field selects the
`TerminatingOrFailed` replacement policy:
the control plane creates replacement Pods immediately upon Pod deletion
(as soon as the control plane sees that a Pod for this Job has `deletionTimestamp` set).
For Jobs with a Pod failure policy set, the default `podReplacementPolicy` is `Failed`, and no other
value is permitted.
See [Pod failure policy](https://kubernetes.io/docs/concepts/workloads/controllers/job/#pod-failure-policy) to learn more about Pod failure policies for Jobs.

```
kind: Job
metadata:
  name: new
  ...
spec:
  podReplacementPolicy: Failed
  ...
```

Provided your cluster has the feature gate enabled, you can inspect the `.status.terminating` field of a Job.
The value of the field is the number of Pods owned by the Job that are currently terminating.

```
kubectl get jobs/myjob -o yaml
```

```
apiVersion: batch/v1
kind: Job
# .metadata and .spec omitted
status:
  terminating: 3 # three Pods are terminating and have not yet reached the Failed phase
```