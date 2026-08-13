---
id: kubernetes-backoff-limit-per-index-bc994bad
type: concept
title: Backoff limit per index
description: 'FEATURE STATE:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/controllers/job/
updated_at: '2026-08-13'
created_at: '2026-08-13'
---

### Backoff limit per index

FEATURE STATE:
`Kubernetes v1.33 [stable]`(enabled by default)

When you run an [indexed](https://kubernetes.io/docs/concepts/workloads/controllers/job/#completion-mode) Job, you can choose to handle retries
for pod failures independently for each index. To do so, set the
`.spec.backoffLimitPerIndex` to specify the maximal number of pod failures
per index.

When the per-index backoff limit is exceeded for an index, Kubernetes considers the index as failed and adds it to the
`.status.failedIndexes` field. The succeeded indexes, those with a successfully
executed pods, are recorded in the `.status.completedIndexes` field, regardless of whether you set
the `backoffLimitPerIndex` field.

Note that a failing index does not interrupt execution of other indexes.
Once all indexes finish for a Job where you specified a backoff limit per index,
if at least one of those indexes did fail, the Job controller marks the overall
Job as failed, by setting the Failed condition in the status. The Job gets
marked as failed even if some, potentially nearly all, of the indexes were
processed successfully.

You can additionally limit the maximal number of indexes marked failed by
setting the `.spec.maxFailedIndexes` field.
When the number of failed indexes exceeds the `maxFailedIndexes` field, the
Job controller triggers termination of all remaining running Pods for that Job.
Once all pods are terminated, the entire Job is marked failed by the Job
controller, by setting the Failed condition in the Job status.

Here is an example manifest for a Job that defines a `backoffLimitPerIndex`:

[`/controllers/job-backoff-limit-per-index-example.yaml`](https://raw.githubusercontent.com/kubernetes/website/main/content/en/examples//controllers/job-backoff-limit-per-index-example.yaml)![](https://kubernetes.io/images/copycode.svg "Copy /controllers/job-backoff-limit-per-index-example.yaml to clipboard")

```
apiVersion: batch/v1
kind: Job
metadata:
  name: job-backoff-limit-per-index-example
spec:
  completions: 10
  parallelism: 3
  completionMode: Indexed  # required for the feature
  backoffLimitPerIndex: 1  # maximal number of failures per index
  maxFailedIndexes: 5      # maximal number of failed indexes before terminating the Job execution
  template:
    spec:
      restartPolicy: Never # required for the feature
      containers:
      - name: example
        image: python
        command:           # The jobs fails as there is at least one failed index
                           # (all even indexes fail in here), yet all indexes
                           # are executed as maxFailedIndexes is not exceeded.
        - python3
        - -c
        - |
          import os, sys
          print("Hello world")
          if int(os.environ.get("JOB_COMPLETION_INDEX")) % 2 == 0:
            sys.exit(1)
```

In the example above, the Job controller allows for one restart for each
of the indexes. When the total number of failed indexes exceeds 5, then
the entire Job is terminated.

Once the job is finished, the Job status looks as follows:

```
kubectl get -o yaml job job-backoff-limit-per-index-example
```

```
  status:
    completedIndexes: 1,3,5,7,9
    failedIndexes: 0,2,4,6,8
    succeeded: 5          # 1 succeeded pod for each of 5 succeeded indexes
    failed: 10            # 2 failed pods (1 retry) for each of 5 failed indexes
    conditions:
    - message: Job has failed indexes
      reason: FailedIndexes
      status: "True"
      type: FailureTarget
    - message: Job has failed indexes
      reason: FailedIndexes
      status: "True"
      type: Failed
```

The Job controller adds the `FailureTarget` Job condition to trigger
[Job termination and cleanup](https://kubernetes.io/docs/concepts/workloads/controllers/job/#job-termination-and-cleanup). When all of the
Job Pods are terminated, the Job controller adds the `Failed` condition
with the same values for `reason` and `message` as the `FailureTarget` Job
condition. For