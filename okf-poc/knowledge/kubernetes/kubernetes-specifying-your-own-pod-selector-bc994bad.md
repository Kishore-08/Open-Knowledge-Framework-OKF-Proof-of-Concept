---
id: kubernetes-specifying-your-own-pod-selector-bc994bad
type: concept
title: Specifying your own Pod selector
description: Normally, when you create a Job object, you do not specify `.spec.selector`.
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/controllers/job/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

### Specifying your own Pod selector

Normally, when you create a Job object, you do not specify `.spec.selector`.
The system defaulting logic adds this field when the Job is created.
It picks a selector value that will not overlap with any other jobs.

However, in some cases, you might need to override this automatically set selector.
To do this, you can specify the `.spec.selector` of the Job.

Be very careful when doing this. If you specify a label selector which is not
unique to the pods of that Job, and which matches unrelated Pods, then pods of the unrelated
job may be deleted, or this Job may count other Pods as completing it, or one or both
Jobs may refuse to create Pods or run to completion. If a non-unique selector is
chosen, then other controllers (e.g. ReplicationController) and their Pods may behave
in unpredictable ways too. Kubernetes will not stop you from making a mistake when
specifying `.spec.selector`.

Here is an example of a case when you might want to use this feature.

Say Job `old` is already running. You want existing Pods
to keep running, but you want the rest of the Pods it creates
to use a different pod template and for the Job to have a new name.
You cannot update the Job because these fields are not updatable.
Therefore, you delete Job `old` but *leave its pods
running*, using `kubectl delete jobs/old --cascade=orphan`.
Before deleting it, you make a note of what selector it uses:

```
kubectl get job old -o yaml
```

The output is similar to this:

```
kind: Job
metadata:
  name: old
  ...
spec:
  selector:
    matchLabels:
      batch.kubernetes.io/controller-uid: a8f3d00d-c6d2-11e5-9f87-42010af00002
  ...
```

Then you create a new Job with name `new` and you explicitly specify the same selector.
Since the existing Pods have label `batch.kubernetes.io/controller-uid=a8f3d00d-c6d2-11e5-9f87-42010af00002`,
they are controlled by Job `new` as well.

You need to specify `manualSelector: true` in the new Job since you are not using
the selector that the system normally generates for you automatically.

```
kind: Job
metadata:
  name: new
  ...
spec:
  manualSelector: true
  selector:
    matchLabels:
      batch.kubernetes.io/controller-uid: a8f3d00d-c6d2-11e5-9f87-42010af00002
  ...
```

The new Job itself will have a different uid from `a8f3d00d-c6d2-11e5-9f87-42010af00002`. Setting
`manualSelector: true` tells the system that you know what you are doing and to allow this
mismatch.